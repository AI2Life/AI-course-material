"""
ESERCIZIO 2
Scrivi uno script che prende come input un numero intero e stampa la tabellina di quel numero

ESEMPIO:
input = 2
    OUTPUT:
    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
"""

inp = int(input())
c = 0

for i in range(10):
    c += inp
    print(c)