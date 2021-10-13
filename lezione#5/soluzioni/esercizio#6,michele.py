"""
Scrivi uno script che controlla se una password passata come input soddisfa queste condizioni:
1. Almeno 1 lettera tra [a-z]
2. Almeno una lettera tra [A-Z].
3. Almeno 1 numero tra [0-9].
4. Almeno 1 carattere tra [$#@!?.].
5. Lunghezza minima 6 caratteri.
6. Lunghezza massima 16 caratteri.

Punti Bonus:
    Scrivi uno script che genera una password random che soddisfa i criteri elencati sopra


"""
# Importiamo un modulo built-in (random)
# DOCS -> https://docs.python.org/3/library/random.html
import random

password = input("Inserisci una password: ")

# condizione 0 => tutti i caratteri immessi sono validi
# lista delle condizioni da 0 a 4
# TUTTE le condizioni sono inizialmente false
cond = [False]*5
cond[0] = True # ... tranne la 0 che si suppone vera

#Queste costanti mi permettono di cambiare più facilmente le condizioni
# Le costanti si mettono i Maiuscolo
SPECIALI = "$#@!?."
MAIUSCOLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MINUSCOLE = MAIUSCOLE.lower()
CIFRE = "0123456789"
MINLEN= 6
MAXLEN= 16

for c in password:
    if c in MINUSCOLE:
        cond[1] = True
    elif c in MAIUSCOLE:
        cond[2] = True
    elif c.isdigit():
        cond[3] = True
    elif c in SPECIALI:
        cond[4] = True
    else:
        cond[0] = False

# cond -> [True, True, True, True, True]

if MINLEN <= len(password) <= MAXLEN and all(cond):
    print("La password risulta valida")
else:
    print("Non ci siamo")

"""
Generatore di password
"""
#creo una tupla con le "regolette"
GRUPPI = (MINUSCOLE, MAIUSCOLE, CIFRE, SPECIALI)

# Parto con una stringa vuota
casuale = ""

# Assegna un carattere per ogni gruppo mandatorio
for i in range(len(GRUPPI)):
    casuale += random.choice(GRUPPI[i])

# Estraggo una lunghezza per la password
lunghezza = random.randint(MINLEN, MAXLEN)
lunghezza -= len(casuale) # tolgo quanto fatto fino ad ora

for i in range(lunghezza):
    # Aggiunge altri caratteri a caso tra i GRUPPI
    casuale += random.choice(GRUPPI[random.randrange(len(GRUPPI))])

# mischia le carte e dichiara la password generata
password = random.sample(casuale, k=len(casuale))
password = "_".join(password)[::2]
print(f'Ho generato la password "{password}"')