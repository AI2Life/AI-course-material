"""
Determinare se una parola o una frase è un isogramma.
Un isogramma è una parola composta di lettere le quali ricorrono tutte lo stesso numero di volte.
L'isogramma più lungo in italiano è "prosciugante".
Un isogramma (noto anche come "nonpattern word") è una parola o una frase senza una lettera ripetuta,tuttavia gli spazi e i trattini possono apparire più volte.

Esempi di isogrammi:
 -> PATHFINDER
 -> BLACKHORSE

Curiosità (wikipedia):

    Gli isogrammi possono essere utili come chiavi di cifratura dato che la corrispondenza fra lettere è univoca.
    Isogrammi di 10 lettere, per esempio PATHFINDER, DUMBWAITER o BLACKHORSE, sono utilizzate da venditori di beni
    il cui prezzo può essere negoziato, come macchine usate, gioielli e antichità.

    Per esempio le cifre decimali possono essere mappate secondo questo schema:

    P	A	T	H	F	I	N	D	E	R
    1	2	3	4	5	6	7	8	9	0

    Ammettiamo che il prezzo indicato fosse 1200 € ma nel cartellino ci fossero anche le lettere FRR,
    il venditore saprebbe che il prezzo originale era 500 € in modo da non scendere sotto quella soglia.

Scrivi uno script che accetta una stringa come input e determina se quella stringa è un isogramma.
"""
# Prendo come input una parola
word = input("enter a word: ")
letters = []
# Prendo ogni carattere
for alphabet in word:
    # Se non c'è nella lista
    if alphabet not in letters:
        a = True
        # Aggiungo il carattere alla lista
        letters.append(alphabet)
    # Se il carattere è nella lista
    else:
        # Non è un isogramma
        a = False
        print("word is not an isogram")
        break

# Se a è vero stampo è un isogramma
if a:
    print("isogram")


