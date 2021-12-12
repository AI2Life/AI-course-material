# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:57:39 2021

@author: Daniele
"""

from os import listdir
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import re

#%%


# BAG OF WORDS RAPRESENTATION

# carica il documento
def load_doc(filename):
    # apri il file per la sola lettura
    file = open(filename, 'r')
    # leggi il testo
    text = file.read()
    # chiudi il file
    file.close()
    return text


# trasforma il documento in token ripuliti
def clean_doc(doc):
    # dividi il testo sulla base degli spazi
    tokens = doc.split()
    # rimuovi punteggiatura
    tokens = [re.sub(r'\W+', "", i) for i in tokens]
    tokens = [re.sub(r'\d+', "", i) for i in tokens]
    # rimuovi token non composti da lettere
    tokens = [word for word in tokens if word.isalpha()]
    # filtra le stopword
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    # filtra i token composti da un solo carattere
    tokens = [word for word in tokens if len(word) > 1]
    return tokens

#%%

# carica e pulisci documento, ritornando una stringa di token
def doc_to_line(filename, vocab):
    # carica il documento
    doc = load_doc(filename)
    # trasforma il documento in token ripuliti
    tokens = clean_doc(doc)
    # filtra attraverso il vocabolario
    tokens = [w for w in tokens if w in vocab]
    return ' '.join(tokens)


# carica tutti i documenti di una directory
def process_docs(directory, vocab, is_train):
    lines = list()
    # itera tutti i file nella directory
    for filename in listdir(directory):
        # sdividi in train e test set
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


#%%

path = 'C:\\Users\Daniele\Desktop\Corsi Python\Lezioni\Lezione 35\\'

# carica il vocabolario
vocab_filename = path + 'txt_sentoken/vocab.txt'
vocab = load_doc(vocab_filename)
vocab = vocab.split()
vocab = set(vocab)

#%%


# MOVIE REVIEWS TO BAG-OF-WORDS VECTORS


# carica tutte le review che costituiranno il training set
positive_lines = process_docs('txt_sentoken/pos', vocab, True)
negative_lines = process_docs('txt_sentoken/neg', vocab, True)
 
# istanzia il tokenizzatore
tokenizer = Tokenizer()
# fitta il tokenizer sui documenti
docs = negative_lines + positive_lines
tokenizer.fit_on_texts(docs)
 
# encoding del training set
X_train = tokenizer.texts_to_matrix(docs, mode='binary')
print(X_train.shape)
 
# carica tutte le review che costituiranno il test set
positive_lines = process_docs('txt_sentoken/pos', vocab, False)
negative_lines = process_docs('txt_sentoken/neg', vocab, False)
docs = negative_lines + positive_lines
# encoding del test set
X_test = tokenizer.texts_to_matrix(docs, mode='binary')
print(X_test.shape)

#%%

# crea i label per il train e per il test

y_train = np.array([0 for _ in range(900)] + [1 for _ in range(900)])
y_test = np.array([0 for _ in range(100)] + [1 for _ in range(100)])

#%%

# definisci l'input shape per la rete neurale
n_words = X_test.shape[1]

# architettura del modello
model = Sequential()
model.add(Dense(50, input_shape=(n_words,), activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compila modello
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#%%

# fit del modello
model.fit(X_train, y_train, epochs=10, verbose=2)

#%%

# valutazione del modello
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print('Test Accuracy: %f' % (acc*100))


