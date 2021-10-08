"""
ESERCIZIO 9
Scrivi uno script che prende come input 2 numeri interi e stampa tutti i numeri interi in
quell'intervallo specificando se sono pari o dispari.

INPUT:
	1
	5

OUTPUT:
	1 -> dispari
	2 -> pari
	3 -> dispari
	4 -> pari
	5 -> dispari
"""

n1 = int(input())
n2 = int(input())

for i in range(n1, n2):
    print(i, "pari" if i % 2 == 0 else "dispari")