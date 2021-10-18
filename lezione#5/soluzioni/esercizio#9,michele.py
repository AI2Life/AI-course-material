"""
Da numeri romani a interi
Scrivi uno script che prende come input un numero romano e lo converte in numero intero

Simbolo   Valore
[
("I",    1),
("V",    5),
("X",    10),
("L",    50),
("C",    100),
("D",    500),
("M",    1000)
]

Per esempio, 2 si scrive come II in numero romano, solo due 1 sommati insieme.
Il 12 si scrive come XII, che è semplicemente X + II.
Il numero 27 si scrive come XXVII, che è XX + V + II.
I numeri romani sono di solito scritti dal più grande al più piccolo da sinistra a destra. Tuttavia, il numero quattro
non è IIII. Invece, il numero quattro si scrive IV. Dato che l'uno è prima del cinque, lo sottraiamo facendo il
quattro. Lo stesso principio si applica al numero nove, che si scrive IX.
Ci sono sei casi in cui si usa la sottrazione:

I può essere messo prima di V (5) e X (10) per fare 4 e 9.
X può essere messo prima di L (50) e C (100) per fare 40 e 90.
C può essere messo prima di D (500) e M (1000) per fare 400 e 900.
Dato un numero romano, convertirlo in un numero intero.

Esempio:
Input: "III"
Output: 3

Input: "IV"
Output: 4

Input: "IX"
Output: 9

Input: "LVIII"
Output: 58
Perchè? -> L = 50, V= 5, III = 3.

Input: "MCMXCIV"
Output: 1994
Perchè? -> M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# L'algoritmo poggia sulla constatazione che i 'pesi'
# dei simboli nei numeri romani sono decrescenti.
# Si rispecchia tale ordinamento in SIMBOLO e VALORE.

# SIMBOLI ROMANI E LORO VALORE
SIMBOLO = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
VALORE = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

romano = input("Inserisci un numero romano: ")

numero = 0  # valore accumulato
pos = 0  # indice della posizione in esame

# scansiona i simboli in ordine decrescente di valore
for i in range(len(SIMBOLO)):
    parte = SIMBOLO[i]  # simbolo in esame

    # fino a quando il simbolo è presente
    # ne incremento il numero del valore
    # e avanzo la posizione da controllare
    while romano.startswith(parte, pos):
        numero += VALORE[i]
        pos += len(parte)

    if pos == len(romano):
        # Numero terminato: uscita rapida
        break

print("Il numero corrisponde a ", numero)