"""
Unisci un numero variabile di dizionari (x) in un singolo dizionario

"""

dizionari = [
    {"uno": 1, "due": 2, "tre": 3, "quattro": 4},
    {"cinque": 5, "sei": 6, "sette": 7, "otto" : 8},
    {"nove": 9, "dieci": 10, "undici": 11,"dodici": 12},
    {"tredici": 13, "sei": 6, "sette": 7, "quindici": 15}
]

#soluzione 1

nuovo = dict()

for c in dizionari:
	nuovo.update(c)
print(nuovo)


print('---------------------------------------------')

#soluzione 2

a = dizionari[0]
b = dizionari[1]
c = dizionari[2]
d = dizionari[3]

a.update(b)
a.update(c)
a.update(d)
print(a)
