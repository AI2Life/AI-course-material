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
# Flags criterio soddisfatto o meno
l = False
u = False
d = False
s = False
passw = input("inserisci password: ")

c = '$#@!?.'
# Controllo ongi condizione
for i in range(len(passw)):
    if (passw[i].islower()):
        l = True
    elif (passw[i].isupper()):
        u = True
    elif (passw[i].isdigit()):
        d = True
    if passw[i] in c:
        s = True

if (len(passw) >= 6 and len(passw) <= 16):
    if all(l, u, d, s):
        print("password soddisfa criteri")
    else:
        print("password non soddisfa criteri")
else:
    print("lunghezza password errata")

