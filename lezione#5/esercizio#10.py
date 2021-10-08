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



map_romans = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]


inpu = input()
num = 0
value = 0
for letter in inpu[::-1]:
    preValue = value
    for el in map_romans:
        if el[0] == letter:
            value = el[1]
            break
    if value < preValue:
        num -= value
    else:
        num += value
print(num)