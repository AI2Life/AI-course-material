"""
Calcolare la distanza di Hamming tra due filamenti di DNA.

Il tuo corpo è fatto di cellule che contengono DNA. Queste cellule si consumano regolarmente
e devono essere sostituite, cosa che fanno dividendosi in cellule figlie.
Il corpo umano sperimenta mediamente circa 10 quadrilioni di divisioni cellulari in un'intera vita!

Quando le cellule si dividono, anche il loro DNA si replica. A volte durante questo processo accadono degli
errori e singoli pezzi di DNA vengono codificati con informazioni errate. Se confrontiamo due filamenti di
DNA e contiamo le differenze tra loro, possiamo vedere quanti errori si sono verificati.
Questo è noto come "distanza di Hamming".

Leggiamo il DNA usando le lettere C, A, G e T. Due filamenti potrebbero avere questo aspetto:

    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    ^ ^ ^  ^ ^    ^^

Ci sono 7 differenze quindi la distanza di Hamming è 7
La distanza di Hamming è utile per molte cose nella scienza, non solo per la biologia,
quindi è una bella cosa da conoscere :)
La distanza di Hamming è definita solo per sequenze di lunghezza uguale, quindi un tentativo di calcolarla tra
sequenze di lunghezza diversa non dovrebbe funzionare.
Scrivi uno script che trova la distanza di Hamming di due sequenze e stampa le differenze.
Per testare il funzionamento del tuo script puoi usare la lista test_seq.

Punti Bonus:
    1. Usa input() per permettere all'utente di inserire due stringhe
    2. Stampa le differenze in modo spettacolare

"""

test_seq = [("CAGTGATTTTAG", "CAGTGATTGTAG"),
            ("AAAAGGTCGAT", "AATTGATCGAA"),
            ("CATTACCATTAC", "CATTACCATTAC"),
            ("CATCTATCTAT", "CTGATCTTATA"),
            ("TATATATATATA", "TATATATAT"),
            ("TGAGTAGTAGTA", "TGACCATGT"),
            ("CATTACCATTAC", "CATTACCATTAC"),
            ("CATTACCATTAC", "CATTACCATTAC"),
            ("CAACCATTAG", "CAACCATTAG")]

confronto = test_seq

# Permette all'utente di scegliere la modalità manuale o automatica
# Automatica: analizza la lista test_seq
# Manuale: analizza due strimghe passate dall'utente
modo = "X"
while modo not in "AM":
    modo = input(
        "Input (A)utomatico o (M)anuale? ").upper()  # lo convertiamo in maiuscolo per prendere in esame anche i casi in cui l'utente inserisce una lettera minuscola

# Se la modalità è manuale
if modo == "M":
    # Creiamo una lista di due stringhe vuote
    dna = [""] * 2
    # Cicla per due volte
    for i in range(2):
        # creo una variabile ripeti che controlla la corretteza dell'input
        ripeti = True
        while ripeti:
            # Inseriamo l'input
            quale = "prima" if i == 0 else "seconda"
            dna[i] = input(f"Inserisci la {quale} sequenza di DNA: ").upper()
            ripeti = False  # Suppongo che l'inserimento si corretto
            # Per ogni carattera della sequenza
            for c in dna[i]:
                # Controllo che i caratteri siano validi
                if c not in "ACTG":
                    # Se il carattere non è valido
                    print("La sequenza contiene un carattere non valido", c)
                    # Forzo la ripetizione
                    ripeti = True
                    break

            # impone la stessa lunghezza per le sequenze
            # Nel caso in cui ho immesso le due stringhe,
            # la loro lunghezza sia differente e icaratteri immessi validi
            if (i == 1) and len(dna[0]) != len(dna[1]) and not ripeti:
                print("Le due sequenze devono avere la stessa lunghezza")
                ripeti = True

    # Assegno alla lista di confronto le due sequenze inserite manualmente
    confronto = [(dna[0], dna[1])]
# Questo mi permette di usare un singolo blocco di istruzioni per il confronto


# Inizio confronto
for seq in confronto:
    print('\n', '-' * 7, "Avvio confronto", '-' * 7)
    # Se hanno lunghezze differenti avverto l'utente
    if len(seq[0]) != len(seq[1]):
        print("ATTENZIONE: lunghezze differenti, confronto parziale")
    # Creo la stringa che evidenzia le differenze (se presenti)
    out = ""
    # e un accumulatore della distanza di Hamming
    dist = 0
    # Ciclo su i caratteri utilizzando zip
    # Zip: https://www.programiz.com/python-programming/methods/built-in/zip
    for c1, c2 in zip(seq[0], seq[1]):
        if c1 != c2:
            out += '^'
            dist += 1
        else:
            out += ' '

    # controllo che ci siano delle differenze
    # Questa può essere riscritta con un operatore ternario

    # if dist:
    if '^' in out:
        out = f"{out} => distanza di Hamming = {dist}"
    else:
        out = "\nLe parti confrontate risultano uguali"
    print(f"\n{seq[0]}\n{seq[1]}\n{out}")