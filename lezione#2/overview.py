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

Lezione #2: Strutture dati e Operatori
"""

"""
Assegnare una variabile e stampare il valore
"""
x = "e"
print(x)

"""
3 tipi di ogetti in python
"""
# Un int
a = 10
# Un float
b = 5.3

# Una stringa
c = "qualsiasi cosa che sia tra apostrofi o apici"

"""
Conversioni dei tipi
"""
# Creo una variabile e gli assegno un valore intero
a = "2"
b = 2

#Trasformo un int in un float
print(float(b))

"""
Operatori Aritmetici, Ogni tipo di ogetto somma divide ecc. in modo diverso
"""
#Puoi usare il "+" per unire due stringhe!
print("prima stringa " + "seconda stringa")

#Puoi usare il "+" anche per sommare int e float
a = 1
b = 3.5
print(a + b)

#Naturalmente con int e float puoi usare tutti i classi operatori aritmetici:
a = 56
b = 45.8

# / per dividere
print(a / b)
# - per sottrarre
print(a - b)
# per elevare a potenza
print(a ** b)
# per clacolare il module (il resto della divisione)
print(a % b)
# per moltiplicare
print(a * b)
# per dividere senza resto (da intero a intero)
print(a // b)

#Le parentesi in python funzionano come nell'aritmetica classica
a = 1
b = 4
c = 6
print(a + (b - c))

#Allo stesso modo l'ordine delle operazioni seguono l'aritmetica classica (prima moltiplicazione poi addizione)
a = 1
b = 4
c = 6
print(a + b * c)

"""
Operazioni di Assegnazione
Puoi modificare il valore di una variabile attraverso gli operatori di assegnazione
"""
# Creo una variabile
a = 5

print(a)
# La incremento di uno
a += 1
# Dividere per 3
a /= 3 # equivale a -> a = a / 3
a *= 3
print(a)

"""
Algebra di Boole e Operatori Logici
Vero o Falso?
"""
# Creo una variabile booleana
freddo = True
caldo = not freddo

# Uso l'operatore logico AND che ritorna vero se entrambi sono veri, falso in tutti gli altri casi
print(freddo and caldo)

# Uso l'operatore logico or che ritorna vero se almeno un valore è vero
print(freddo or caldo)

# Uso not che inverte il valore booleano
print(not caldo)

"""
Gli Operatori di Comparazione servono a comparare valori tra di loro
"""
# Chiedo se due vaori sono uguali?
a = "5"
b = 5
print(a == b)



