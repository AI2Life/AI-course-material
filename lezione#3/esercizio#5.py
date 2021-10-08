"""
ESERCIZIO 5
Scrivi uno script che controlla se il numero di sigari a disposizione è consono per una festa di scoiattoli.

Lo script prende come input:
1. Il numero di scoiattoli che partecipano alla festa
2. Il numero di sigari a disposizione
3. Se è un giorno feriale o festivo

e stampa "Festa!!!" se ci sono abbastanza sigari "Cippppp, festa annullataaaaaaa!" in caso contrario.

Ad una festa di scoiattoli ci deve essere almeno un sigaro a scoiattolo e non ci possono essere più di 3
sigari a scoiattolo (altrimenti c'è troppa puzza). Se il giorno è festivo non c'è un limite ai sigari.
"""

n_scoiattoli = int(input())
n_sigri = int(input())
giorno_feriale = bool(input())


if giorno_feriale:
    if (n_sigri >= n_scoiattoli) and (n_sigri * 3) >= n_scoiattoli:
        print("Festa!!!")
    else:
        print("Cippppp, festa annullataaaaaaa!")
else:
    if (n_sigri >= n_scoiattoli):
        print("Festa!!!")
    else:
        print("Cippppp, festa annullataaaaaaa!")




