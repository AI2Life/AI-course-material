"""
Scrivi uno script che prende come input una stringa e calcola il punteggio di quella stringa a Scrabble.
    Letter                           Value
    A, E, I, O, U, L, N, R, S, T       1
    D, G                               2
    B, C, M, P                         3
    F, H, V, W, Y                      4
    K                                  5
    J, X                               8
    Q, Z                               10
Esempio:
    Input:
        "pianta"
    Output:
        3(p) + 1(i) + 1(a) + 1(n) + 1(t) + 1(a) = 8
Punti Bonus:
    Crea ua visualizzazione interessante
"""
# Crea una lista di tuple con il punteggio di ogni carattere
pScrabble=[('A', 1),('E', 1), ('I', 1), ('O', 1),
('U', 1), ('L', 1), ('N', 1), ('R', 1), ('S', 1),
('T', 1),
    ('D', 2), ('G',2),
    ('B', 3), ('C', 3), ('M', 3), ('P', 3),
    ('F', 4), ('H', 4), ('V', 4), ('W', 4), ('Y', 4),
    ('K', 5),
    ('J', 8), ('X', 8),
    ('Q', 10), ('Z', 10)]
print(pScrabble)
#Inserisco la parola
parola=input("inserisci parola ").upper()
# accumulatore punteggio
pnt=0
#Ciclo sulle lettere della parola
for c in parola:
	# ciclo sulle lettere
  for lettera, peso in pScrabble:
	  #Prendo il valore della lettera corispondente
      if(c==lettera):
		  # Lo aggiungo all'accumulatore
        pnt+=peso

print("punteggio Scrabble ", pnt)