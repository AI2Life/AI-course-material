"""
T9
Il T9 (abbreviazione di Text on 9 [Keys]) è un software, inventato da Tegic Communication e utilizzato principalmente
su dispositivi mobili (nello specifico quelli che dispongono di un tastierino numerico 3×4), che consente una
composizione guidata nella digitazione di stringhe alfanumeriche.

Il codice T9 è il nome dato all'algoritmo di predizione che usa un dizionario per indovinare la parola che l'utente sta
cercando di scrivere. Per esempio: '2' per 'A' o 'B' o 'C', '222' per 'BAC' o 'ABC'.

Per default, su una tastiera mobile (smartphone, iphone), le lettere sono associate alle cifre secondo
questa disposizione:

2	ABC
3	DEF
4	GHI
5	JKL
6	MNO
7	PQRS
8	TUV
9	WXYZ

https://www.dcode.fr/tools/phone-keypad/images/keypad.png

T9 ha numeri brevi, la cui lunghezza è uguale al numero di lettere nella parola.
Questo è il modo più veloce per scrivere SMS senza abbreviazioni.

Esempio: https://www.sainsmograf.com/labs/t9-emulator/

Esempio di parole:
    testing: 8378464
    super: 78737
    mario: 62746
    legend: 534363


"""

