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
            ("CATCTATCTAT" , "CTGATCTTATA"),
            ("TATATATATATA", "TATATATAT"),
            ("TGAGTAGTAGTA", "TGACCATGT"),
            ("CATTACCATTAC", "CATTACCATTAC"),
            ("CATTACCATTAC", "CATTACCATTAC"),
            ("CAACCATTAG", "CAACCATTAG")]