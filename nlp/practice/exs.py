import re
import os
import nltk
# download tokenizer
import nltk.stem.snowball

nltk.download("punkt")
# download stopwords dict
nltk.download("stopwords")
#Dizionario
nltk.download('wordnet')


with open(os.path.join(os.getcwd(), "sample.txt"), "r") as file:
    text = file.read()

print(text)

# Rimuove i numeri
# \d "Matches any Unicode decimal digit." (source: https://docs.python.org/3/library/re.html)
print(re.sub(r"\d+", "", text))

#Rimuove la punteggiatura
# \W "Matches any character which is not a word character. "(source: https://docs.python.org/3/library/re.html)
print(re.sub(r"\W+", " ", text))

#Rimuove le parentesi
print(re.sub(r"[\(\[].*?[\)\]]", "", text))

# Tutto in lowewrcase
print(text.lower())

# Tokenizzazione in frasi
sent_tokenized = nltk.tokenize.sent_tokenize(text=text,language="italian")
print(sent_tokenized)
# Tokenizzazione in patole
word_tokenized = nltk.tokenize.word_tokenize(text=text,language="italian")
print(word_tokenized)

# Eliminazione delle stopwords
filtered_words = [token for token in word_tokenized if token not in nltk.corpus.stopwords.words("italian")]
print(filtered_words)

# Stemming
stemmer = nltk.stem.SnowballStemmer("italian")
corsa = ["insegnare", "insegno", "insegnamento", "insegnando"]
for parola in corsa:
    print(stemmer.stem(parola))

# Lemmatizzazione
lemmatizer = nltk.stem.WordNetLemmatizer()
lemma = lemmatizer.lemmatize("taught", nltk.corpus.wordnet.VERB)
print(lemma)








