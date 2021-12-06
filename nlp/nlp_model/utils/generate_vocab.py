import os
from nltk.corpus import stopwords
import re
from collections import Counter
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np

"""
Prima volta che usi nltk? 
    Leggi qui amic*

Devi scaricare i dizionari, per farlo segui ligiamente questi step:
1. Apri una console python
2. scrivi -> import nltk [premi invio]
3. scrivi -> nltk.download() [premi invio]
4. Comparirà una finestra. Non compare?
    a. Controlla che sei nell'ambinente corretto
    b. Controlla che nltk è installata
    c. Chiedi aiuto.
5. Nella finestra che appare seleziona la tab "Corpora"
6. Cerca "stopwords" nella colonna "Identifiers"
7. Seleziona "stopwords"
8. Premi su "Download"
9. Chiudi tutto
10. Ottimo lavoro, sei pronto per utilizzare il tuo nuovo fantastico dizionario!
"""


# load doc into memory
def load_doc(filename):
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text


# turn a doc into clean tokens
def clean_doc(doc):
    # split into tokens by white space
    tokens = doc.split()
    # remove punctuation from each token
    tokens = [re.sub(r'\W+', "", i) for i in tokens]
    tokens = [re.sub(r'\d+', "", i) for i in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    # filter out stop words
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    # filter out short tokens
    tokens = [word for word in tokens if len(word) > 1]
    return tokens

# load doc and add to vocab
def add_doc_to_vocab(filename, vocab):
    # load doc
    doc = load_doc(filename)
    # clean doc
    tokens = clean_doc(doc)
    # update counts
    vocab.update(tokens)


# load all docs in a directory
def process_docs(directory, vocab):
    # walk through all files in the folder
    for filename in os.listdir(directory):
        # skip any reviews in the test set
        if filename.startswith('cv9'):
            continue
        # create the full path of the file to open
        path = directory + '/' + filename
        # add doc to vocab
        add_doc_to_vocab(path, vocab)

# save list to file
def save_list(lines, filename):
    # convert lines to a single blob of text
    data = '\n'.join(lines)
    # open file
    file = open(filename, 'w')
    # write text
    file.write(data)
    # close file
    file.close()


data_path = os.path.join(os.getcwd(), "data")
dataset_path = os.path.join(data_path, "txt_sentoken")
# define vocab
vocab = Counter()
# add all docs to vocab
process_docs(os.path.join(dataset_path, "pos"), vocab)
process_docs(os.path.join(dataset_path, "neg"), vocab)
# print the size of the vocab
print(len(vocab))
# print the top words in the vocab
print(vocab.most_common(50))

min_occurane = 2
tokens = [k for k,c in vocab.items() if c >= min_occurane]
print(len(tokens))

# save tokens to a vocabulary file
save_list(tokens, os.path.join(data_path,'vocab.txt'))

# load doc, clean and return line of tokens
def doc_to_line(filename, vocab):
    # load the doc
    doc = load_doc(filename)
    # clean doc
    tokens = clean_doc(doc)
    # filter by vocab
    tokens = [w for w in tokens if w in vocab]
    return ' '.join(tokens)

def process_docs(directory, vocab, is_train):
    lines = list()
    # walk through all files in the folder
    lines = list()
    # walk through all files in the folder
    for filename in os.listdir(directory):
        # skip any reviews in the test set
        if is_train and filename.startswith('cv9'):
            continue
        if not is_train and not filename.startswith('cv9'):
            continue
        # create the full path of the file to open
        path = directory + '/' + filename
        # load and clean the doc
        line = doc_to_line(path, vocab)
        # add to list
        lines.append(line)
    return lines


vocab = load_doc(os.path.join(data_path,'vocab.txt'))
vocab = vocab.split()
vocab = set(vocab)
# load all training reviews
positive_lines = process_docs(os.path.join(dataset_path, "pos"), vocab, True)
negative_lines = process_docs(os.path.join(dataset_path, "neg"), vocab, True)
# summarize what we have
print(len(positive_lines), len(negative_lines))

# create the tokenizer
tokenizer = Tokenizer()
# fit the tokenizer on the documents
docs = negative_lines + positive_lines
tokenizer.fit_on_texts(docs)

# encode training data set
Xtrain = tokenizer.texts_to_matrix(docs, mode='freq')

# load all test reviews
positive_lines = process_docs(os.path.join(dataset_path, "pos"), vocab, False)
negative_lines = process_docs(os.path.join(dataset_path, "neg"), vocab, False)
docs = negative_lines + positive_lines
# encode training data set
Xtest = tokenizer.texts_to_matrix(docs, mode='freq')

n_words = Xtest.shape[1]
ytrain = np.array([0 for _ in range(900)] + [1 for _ in range(900)])
ytest = np.array([0 for _ in range(100)] + [1 for _ in range(100)])

# define network
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(100, input_shape=(n_words,), activation='relu'))
model.add(tf.keras.layers.Dense(50, input_shape=(n_words,), activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
# compile network
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(Xtrain, ytrain, epochs=50, verbose=2)

# evaluate
loss, acc = model.evaluate(Xtest, ytest, verbose=0)
print('Test Accuracy: %f' % (acc*100))