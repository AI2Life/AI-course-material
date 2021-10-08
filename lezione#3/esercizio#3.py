"""
ESERCIZIO 3
Scrivi uno script che prende come input 2 interi e stampa tutti i numeri primi all'interno dell'intervallo

NOTA:
	Un numero primo è un numero che non può essere ottenuto moltiplicando altri numeri interi. Un numero primo è un numero naturale maggiore di 1 che non è il prodotto di due numeri naturali più piccoli.
	6 non è un numero primo perché può essere scomposto in 2×3 = 6
	37 è un numero primo perché non è divisibile per nessun altro intero

ESEMPIO:
	INPUT:
		2, 7
	OUTPUT:
		2
		3
		5
		7

"""

inp1 = int(input())
inp2 = int(input())

for num in range(inp1,inp2):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)