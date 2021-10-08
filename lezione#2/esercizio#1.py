"""
 _______  ___     _______    ___      ___   _______  _______
|   _   ||   |   |       |  |   |    |   | |       ||       |
|  |_|  ||   |   |____   |  |   |    |   | |    ___||    ___|
|       ||   |    ____|  |  |   |    |   | |   |___ |   |___
|       ||   |   | ______|  |   |___ |   | |    ___||    ___|
|   _   ||   |   | |_____   |       ||   | |   |    |   |___
|__| |__||___|   |_______|  |_______||___| |___|    |_______|

Coded with love by:
@Francesco Mattioli
@Linda Fiorini
@Daniele Sasso

Lezione #3: Liste e Tuple
"""

#Istanzio una lista
lista = [1, 2, 3, 4, 5, 6]

# Posso creare anche una lista vuota con la funzione list()
lista_vuota = list()
# TIPS: Questo metodo è equivalente a:
altra_lista_vuota = []
# Il metodo precedente aiuta il lettore

#NOTA, ricorda che gli indici di una lista partono da 0
#INDICE:   0 1 2 3 4 5
#LISTA:   [1,2,3,4,5,6]


#Stampo il primo elemento di una lista
print(lista[0])

#Stampo i primi 2 elementi di una lista
print(lista[:2])

#Stampo l'ultimo elemento di una lista
print(lista[-1])

#Stampo dal secondo al quarto elemento di una lista
print(lista[1:5])

#Itero tra gli elemnti di una lista
for elem in lista:
    print(elem)

#Creo una lista di liste
lista_di_liste = [[1,2,3], [4,5,6]]

#Stampo il secondo elemento della seconda lista
print(lista_di_liste[1][1])

#controllo se 7 è nella lista
print(7 in lista)

#Unisco due liste
lista_1 = [1,2,3]
lista_2 = [4,5,6]

print(lista_1 + lista_2)

#Aggiungo un elemento alla fine della lista
lista.append(2)

#Stampo la lunghezza di una lista
print(len(lista))

#Elimino l'ultimo elemento di una lista
lista.pop()

#Inserisco un numero alla posizione 0 di una lista
lista.insert(0, 5)

#Ordino la lista
lista.sort()

#TUPLE

#Creo una tupla
tupla = (1,2,3)
