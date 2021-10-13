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
isbn = input('Inserisci ISBN-10 della forma X-XXX-XXXXX-X: ')
isbn = isbn.split('-')
isbn = ''.join(isbn)
sum = 0

is_correct = [
	len(isbn) == 10,
	isbn[0:9].isdigit(),
	(isbn[9].isdigit() or isbn[-1].upper() == 'X')
]
print(is_correct)

if len(isbn) == 13:
	print('inserisci un codce ISBN-10')
# 1. se l'isbn è lungo 10
# 2. Se i primi 9 caratteri sono numerici
# 3. se l'ultimo carattere è un numero or "X"
elif all(is_correct):
	# (3 * 10 + 5 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 1 * 5 + 5 * 4 + 0 * 3 + 8 * 2 + 8 * 1) mod 11 == 0
	for i in range(len(isbn)):
		if isbn[i].upper() == 'X':
			sum += 10
		else:
			sum += int(isbn[i])*(10-i)

	if sum % 11 == 0:
		print('ISBN-10 valido')
	else:
		print('ISBN-10 non valido')
else:
	print('ISBN non valido')