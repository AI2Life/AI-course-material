# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:57:39 2021

@author: Daniele
"""
import os
import wget
import re
import tarfile
import sys
from os import listdir
from collections import Counter
from nltk.corpus import stopwords

#%%

# GET DATA

def get_data():
    def bar_progress(current, total, width=80):
      progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
      sys.stdout.write("\r" + progress_message)
      sys.stdout.flush()

    save_to = os.path.join(os.getcwd(), "data")
    if os.path.exists(save_to):
        print("Data directory exist, skip download")
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

 
# LOADING AND CLEANING REVIEWS


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
    # rimuovi punteggiatura e numeri
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

# carica e ripulisci un documento
path = 'C:\\Users\Daniele\Desktop\Corsi Python\Lezioni\Lezione 35\\'
filename = path + 'txt_sentoken\pos\cv000_29590.txt'
text = load_doc(filename)
tokens = clean_doc(text)
print(tokens)

#%%

# DEFINE A VOCABULARY

# carica un documento e aggiungilo ad un vocabolario
def add_doc_to_vocab(filename, vocab):
	# carica il documento
	doc = load_doc(filename)
	# trasforma il documento in token ripuliti
	tokens = clean_doc(doc)
	# aggiorna il vocabolario
	vocab.update(tokens)
 
# carica tutti i documenti di una directory
def process_docs(directory, vocab):
    # itera tutti i file nella directory
	for filename in listdir(directory):
		# scarta il 10% dei file
		if filename.startswith('cv9'):
			continue
		# crea il path del file da aprire
		path = directory + '/' + filename
		# aggiungi al vocabolario
		add_doc_to_vocab(path, vocab)
        
#%%
 
# definisci vocabolario
vocab = Counter()
# aggiungi tutti i documenti al vocabolario
process_docs(path + 'txt_sentoken/pos', vocab)
process_docs(path + 'txt_sentoken/neg', vocab)

# size del vocabolario
print(len(vocab))
# parole più comuni nel vocabolario
print(vocab.most_common(50))

#%%

# tieni token che sono presenti almeno 2 volte
min_occurane = 2
tokens = [k for k,c in vocab.items() if c >= min_occurane]
print(len(tokens))

#%%

# salva vocabolario in un file di testo
def save_list(lines, filename):
	# converti lista in un elenco di parole
	data = '\n'.join(lines)
	# apri il file
	file = open(filename, 'w')
	# inserisci il testo
	file.write(data)
	# chiudi il file
	file.close()
    
#%%
 
# save tokens to a vocabulary file
save_list(tokens, path + 'txt_sentoken/vocab.txt')

