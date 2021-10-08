"""
Data una lista di interi e un numero intero target, scrivi uno script che stampa gli indici di due numeri che sommano
a target nella lista di interi.
"""

x = [7,15,2,25,9,73,34,52,67,89,8,56,121,66]
target = 125

for i1 in range(len(x)):
    for i2 in range(len(x)):
        if x[i1] + x[i2] == 125:
            print(i1, i2)
            break