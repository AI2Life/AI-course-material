"""
ISBN (wikipedia)
Il codice ISBN (dall'inglese International Standard Book Number, "numero di riferimento internazionale del libro") è
una sequenza numerica di 13 cifre usata internazionalmente per la classificazione dei libri (è ancora utilizzata anche
la codifica antecedente il 2007, costituita da un numero di cifre pari a 10, in cui l'ultima cifra può eventualmente
contenere la lettera maiuscola X). È definito da uno standard dell'ISO, derivato dalla codifica SBN inglese del 1967.
Sebbene non obbligatorio, il suo uso però è ormai diventato essenziale per l'immissione del prodotto librario nei canali
della grande distribuzione.

Ogni codice ISBN identifica in modo univoco ogni specifica edizione di un libro (non però le semplici ristampe,
che mantengono lo stesso codice dell'edizione cui si riferiscono) e, una volta assegnato, non può più essere riutilizzato.

Il formato ISBN-10 è di 9 cifre (da 0 a 9) più un carattere di controllo (o una cifra o solo una X).
Nel caso in cui il carattere di controllo sia una X, questo rappresenta il valore "10".
Questi possono essere comunicati con o senza trattini, e la loro validità può essere verificata con la formula seguente:

(x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0

Se il risultato è 0, allora è un ISBN-10 valido, altrimenti non è valido.
Esempio:
    prendiamo l'ISBN-10 3-598-21508-8. Lo inseriamo nella formula e otteniamo:
    (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
    Poiché il risultato è 0, questo prova che il nostro ISBN è valido.

Scrivi uno script che prede come input un ISBN 10 e controlla se questo è valido.

Punti Bonus:
    Scrivi uno script che prende come input un ISBN 10 o 13 e controlla che questo sia valido


"""
# Elenco delle cifre valide
CIFRE = "0123456789X"

# Prendo un input
ingresso = input("Inserisci un codice ISBN (13 o 10): ")

buono = False

# Rimuove i caratteri '-'
numeri = ""
for c in ingresso:
    if c != "-":
        numeri += c

# Controllo se è tutto corretto
tipo = len(numeri)
if (tipo == 10 and numeri[0:9].isdigit() and numeri[9] in CIFRE) or (tipo == 13 and numeri.isdigit()):
    buono = True
else:
    print("Formato non valido")

# CIFRE = "0123456789X"
if buono:
    sum = 0
    for c in range(tipo):
        sum += CIFRE.index(numeri[c]) * (tipo - c)

    if sum % 11 == 0:
        print("Codice ISBN corretto!")
    else:
        print("Verifica sul carattere di controllo fallita!")