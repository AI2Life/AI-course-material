"""
Determinare se una parola o una frase è un isogramma.
Un isogramma è una parola composta di lettere le quali ricorrono tutte lo stesso numero di volte.
L'isogramma più lungo in italiano è prosciugante.
Un isogramma (noto anche come "nonpattern word") è una parola o una frase senza una lettera ripetuta,
tuttavia gli spazi e i trattini possono apparire più volte.

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

# Leggo una stringa e la converto in maiuscolo
s = input("Inserisci una stringa: ")
grande = s.upper()

# Tutte le lettere maiuscole (sarà string.ascii_uppercase quando faremo i moduli)
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Numero di apparizioni di ciascun carattere
# (posizione 0 per 'A', posizione 1 per 'B'...)
usato = [0] *26

# Conto le occorrenze di ciascun carattere alfabetico
for c in grande:
    if c.isalpha(): # i caratteri non alfabetici vengono ignorati
        usato[ALFABETO.index(c)] += 1

frequenza = 0 # occorrenza della singola lettera
isogramma = True # partiamo ottimisti :-)

for i in usato: # verifico le frequenze delle lettere
    if i and i != frequenza: # lettera presente con nuova frequenza
        if frequenza: # equivalente a occorrenza != 0
            isogramma = False
            break # inutile proseguire...
        else:
            frequenza = i

print("è un isogramma?".capitalize(), isogramma)


