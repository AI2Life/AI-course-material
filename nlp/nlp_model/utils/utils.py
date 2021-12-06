import wget
import tarfile
import sys
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os
from nltk.corpus import stopwords
import re
from collections import Counter

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


def get_data():
    def bar_progress(current, total, width=80):
      progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
      sys.stdout.write(Fore.GREEN + "\r" + progress_message)
      sys.stdout.flush()

    save_to = os.path.join(os.getcwd(), "data")
    if os.path.exists(save_to):
        print(Fore.RED + "Data directory exist, skip download")
        return save_to
    else:
        os.mkdir("data")
        url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/review_polarity.tar.gz"
        filename = wget.download(url, out=save_to, bar=bar_progress)
        my_tar = tarfile.open(filename)
        my_tar.extractall(save_to)
        my_tar.close()
        os.remove(filename)
        return save_to


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

# Generate vocabualry

def generate_vocabulary():
    data_path = os.path.join(os.getcwd(), "data")
    voc_path = os.path.join(data_path,'vocab.txt')

    if os.path.exists(voc_path):
        print(Fore.RED + "Vocabulary exist")
        return voc_path
    else:
        print(Fore.GREEN + "Generating Vocabulary")
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
        return os.path.join(data_path,'vocab.txt')