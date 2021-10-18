"""
Qui ci si diverte! Scegli uno degli esercizi precedenti e trasformalo utilizzando le funzioni!
"""
"""
Unisci un numero variabile di dizionari di lunghezza variabile in un singolo dizionario

"""


def prendi_dizionario():
    N = int(input("Quanti elementi ha questo dizionario?"))
    i = 0
    diz = {}
    while i < N:
        key = input("Dammi chiave:")
        value = input("Dammi valore:")
        diz.setdefault(key, value)
        i += 1

    return diz


def unisci_dizionari(lista, dizionario):
    new_diz = {}
    lista.append(dizionario)
    for diz in lista:
        for key, value in zip(diz.keys(), diz.values()):
            new_diz.setdefault(key, value)
    return new_diz


N_MAX = int(input("Quanti dizionari vuoi unire?"))
lista = []
for n in range(N_MAX):
    diz = prendi_dizionario()
    diz_uniti = unisci_dizionari(lista, diz)

print(diz_uniti)