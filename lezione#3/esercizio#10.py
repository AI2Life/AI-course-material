"""
ESERCIZIO 10
Scrivi uno script che prende un nuemro variabile di input e calcola la media.
ESEMPIO:

	INPUT:
		Inserisci un numero: 1
		Vuoi inserire un altro numero? s
		Insercisci un numero: 5
		Vuoi inserire un altro numero? n

	OUTPUT:
		La media è: 3.0

"""

stop = True
cum_sum = 0
count = 0

while stop:
    cum_sum += int(input("Inserisci un numero: "))
    count += 1
    stop = True if input("Vuoi inserire un altro numero? ") == "s" else False
    if not stop:
        print("La media è: ", cum_sum/count)
        break