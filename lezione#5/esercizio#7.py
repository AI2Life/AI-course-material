"""
Crea un'implementazione del cifrario atbash, un antico sistema di crittografia creato in Medio Oriente.

Il cifrario Atbash è un semplice cifrario a sostituzione che si basa sulla trasposizione di tutte le lettere
dell'alfabeto in modo che l'alfabeto risultante sia al contrario. La prima lettera viene sostituita con l'ultima,
la seconda con la penultima e così via.

Un cifrario Atbash per l'alfabeto latino sarebbe il seguente:

Testo: abcdefghijklmnopqrstuvwxyz
Cifratura: zyxwvutsrqponmlkjihgfedcba

È un cifrario molto debole perché ha solo una chiave possibile, ed è un semplice cifrario a sostituzione monoalfabetica.
Tuttavia, questo potrebbe non essere stato un problema ai tempi del cifrario.
Il testo cifrato è scritto in gruppi di lunghezza fissa, la dimensione tradizionale del gruppo è di 5 lettere,
e la punteggiatura è esclusa. Questo per rendere più difficile indovinare le cose basandosi sui confini delle parole.

Scrivi uno script che prende in input una stringa e la cifra o la decifra

"""