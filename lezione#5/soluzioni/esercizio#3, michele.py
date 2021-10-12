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

punti = ((1, "AEIOULNRST"), (2, "DG"),
         (3, "BCMP"), (4, "FHVWY"),
         (5, "K"), (6, "JX"), (7, "QZ"))

parola = input("Inserisci una parola: ")

atomi = []
tot = 0

#Se ilc arattere non è alfabetico (e.g. spazio " ")
for c in parola:
    if not c.isalpha(): # filtro i caratteri spuri
        continue

    for peso, car in punti:
        if c.upper() in car: #(e.g. "AEIOULNRST")
            tot += peso #(e.g. (1, "AEIOULNRST"))
            atomi.append(f"{peso}({c})")
            break

print(" + ".join(atomi), "=", tot)