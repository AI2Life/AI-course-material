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

testo = input("Inserisci numero romano: ").upper()  # è già stringa

indici = [0, 1, 2, 3, 4, 5, 6]
romani = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabi = [1, 5, 10, 50, 100, 500, 1000]

tot_ara = 0  # risultato in numeri arabi
i = 0  # indice della lettera su cui sto operando

# Itero su ogni lettera
for let in testo:
    ind_txt = i  # quindi bisogna far contare gli indici progress.
    ind_txt_s = i - 1
    let_s = testo[ind_txt_s]
    i += 1

    val_ara = arabi[romani.index(let)]  # Mi prendo il numero arabo corrispondente
    val_ara_s = arabi[
        romani.index(let_s)] if ind_txt_s >= 0 else 0  # Mi prendo il numero arabo corrispondente precente alla lettera

    if (ind_txt == 0 or val_ara_s >= val_ara):
        tot_ara += val_ara
    else:  # elif val_ara_s<val_ara:
        tot_ara += val_ara - 2 * val_ara_s

    """print("indice let",ind_txt)
    print("valore let",val_ara)
    print("valore let_s",val_ara_s,'\n')"""

print('tot_ara', tot_ara)

