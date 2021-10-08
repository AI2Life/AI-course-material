"""
Scrivi uno script che trova e stampa i numeri mancanti nella lista x

ESEMPIO:
[1,2,3,5,6,9]
Deve stampare:
4, 7, 8
"""

x = [7,9,20,13,15,16,21,14,51,2,12,67]

for i in range(max(x)):
    if i in x:
        pass
    else:
        print(i)