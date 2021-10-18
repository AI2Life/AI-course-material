"""
Crea un'implementazione del cifrario atbash, un antico sistema di crittografia creato in Medio Oriente.

Il cifrario Atbash è un semplice cifrario a sostituzione che si basa sulla trasposizione di tutte le lettere
dell'alfabeto in modo che l'alfabeto risultante sia al contrario. La prima lettera viene sostituita con l'ultima,
la seconda con la penultima e così via.

Un cifrario Atbash per l'alfabeto latino sarebbe il seguente:

Testo:     abcdefghijklmnopqrstuvwxyz
Cifratura: zyxwvutsrqponmlkjihgfedcba

È un cifrario molto debole perché ha solo una chiave possibile, ed è un semplice cifrario a sostituzione monoalfabetica.
Tuttavia, questo potrebbe non essere stato un problema ai tempi del cifrario.
Il testo cifrato è scritto in gruppi di lunghezza fissa, la dimensione tradizionale del gruppo è di 5 lettere,
e la punteggiatura è esclusa. Questo per rendere più difficile indovinare le cose basandosi sui confini delle parole.

Scrivi uno script che prende in input una stringa e la cifra o la decifra

"""

# #metodo 1, didattico
# # Chiedo se l'utente vuole inserire la formattazione standard
# a=input("dimensione gruppo standard 5: vuoi cambiarla? si/no ")

# if a=="si":
# 	b=int(input("inserisci nuova dimensione gruppo: "))
# else:
# 	b=5

# # Inserisco il testo da cifrare
# testo=input("Inserisci testo da cifrare: ").upper()
# # Vado a eliminare la punteggiatura
# divisori=[' ',',',';','.',':']

# for i in divisori:
# 	testo_diviso=str(testo).split(f'{i}')
# 	testo_unito="".join(testo_diviso)
# 	testo=testo_unito
# print(testo)

# # Creo una variabile per conservare il nuovo testo
# sequenza=""

# # Divido in gruppi sulla base della scelta dell'utente
# for k in range(0,len(testo),b):
# 	gruppo_k=""
# 	for j in range(k,k+b if k+b<len(testo) else len(testo)):
# 		gruppo_k+=testo[j]
# 	sequenza+=gruppo_k+" "
# print(sequenza)

# #Testo: abcdefghijklmnopqrstuvwxyz
# #Cifratura: zyxwvutsrqponmlkjihgfedcba

# # Creo il cifrario
# cifrario=[ ('A','Z'), ('B','Y'), ('C','X'), ('D','W'),
# ('E','V'), ('F','U'), ('G','T'), ('H','S'), ('I','R'),
# ('J','Q'), ('K','P'), ('L','O'), ('M','N'), ('N','M'), ('O','L'), ('P','K'), ('Q','J'), ('R','I'), ('S','H'), ('T','G'), ('U','F'), ('V','E'), ('W','D'), ('X','C'), ('Y','B'), ('Z','A'), ('0','9'), ('1','8'), ('2','7'),('3','6'), ('4','5'), ('5','4'), ('6','3'), ('7','2'),('8','1'), ('9','0'), (' ',' '),
# ('!','!'), ('"','"'), ('£','£'), ('%','%'), ('&','&'),
# ('/','/'), ('(','('), (')',')'), ('=','='), ('^','^'),
# ('é','é'), ('è','è'), ('[','['), ('{','{'), ('+','+'), ('*','*'), (']',']'), ('}','}'), ('ò','ò'), ('ç','ç'), ('@','@'), ('à','à'), ('#','#'), ('°','°'), ('X','C'), ('ù','ù'), ('§','§'), ('-','-'), ('_','_'), ('|','|')]


# #print(cifrario)

# # Creo una variabile per consrvare il testo
# cripto=""

# for let in sequenza:
# 	for ing,usc in cifrario:
# 			if let==ing:
# 				cripto+=usc

# print(cripto)


# metodo 2, ottimizzazione del metodo 1

a = input("dimensione gruppo standard 5: vuoi cambiarla? si/no ")

if a == "si":
    b = int(input("inserisci nuova dimensione gruppo: "))
else:
    b = 5

testo = input("Inserisci testo da cifrare: ").upper()

# Testo: abcdefghijklmnopqrstuvwxyz
# Cifratura: zyxwvutsrqponmlkjihgfedcba

cifrario = [('A', 'Z'), ('B', 'Y'), ('C', 'X'), ('D', 'W'),
            ('E', 'V'), ('F', 'U'), ('G', 'T'), ('H', 'S'), ('I', 'R'),
            ('J', 'Q'), ('K', 'P'), ('L', 'O'), ('M', 'N'), ('N', 'M'), ('O', 'L'), ('P', 'K'), ('Q', 'J'), ('R', 'I'),
            ('S', 'H'), ('T', 'G'), ('U', 'F'), ('V', 'E'), ('W', 'D'), ('X', 'C'), ('Y', 'B'), ('Z', 'A'), ('0', '9'),
            ('1', '8'), ('2', '7'), ('3', '6'), ('4', '5'), ('5', '4'), ('6', '3'), ('7', '2'), ('8', '1'), ('9', '0'),
            # (' ',' '),
            ('!', '!'), ('"', '"'), ('£', '£'), ('%', '%'), ('&', '&'),
            ('/', '/'), ('(', '('), (')', ')'), ('=', '='), ('^', '^'),
            ('é', 'é'), ('è', 'è'), ('[', '['), ('{', '{'), ('+', '+'), ('*', '*'), (']', ']'), ('}', '}'), ('ò', 'ò'),
            ('ç', 'ç'), ('@', '@'), ('à', 'à'), ('#', '#'), ('°', '°'), ('X', 'C'), ('ù', 'ù'), ('§', '§'), ('-', '-'),
            ('_', '_'), ('|', '|')]
# print(cifrario)

cripto = ""
for let in testo:
    for ing, usc in cifrario:
        if let == ing:
            cripto += usc

print(cripto)

sequenza = ""
for k in range(0, len(cripto), b):
    gruppo_k = ""
    for j in range(k, k + b if k + b < len(cripto) else len(cripto)):
        gruppo_k += cripto[j]
    sequenza += gruppo_k + " "
print(sequenza)

# note
# #print(type(testo))
# #print(type(testo[3]))
# #print(range(0,len(testo)+1,b))
# #print(range (k,k+b))
# #print(gruppo_k)
# 		#print(testo[j])
# 		#elemento=testo[j]
# 		#gruppo.append(testo[elemento])
# """
# """
# for j in range(len(testo)):
# 	for k in range(b):
# 		gruppo_diviso=testo.split(" ")
# 		gruppo=" ".join(gruppo_diviso)
# print(gruppo)


# FATTO IO