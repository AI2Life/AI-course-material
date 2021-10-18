"""
Scrivi uno script che data una stringa conta i caratteri Uppercase (e.g. A), Lowercase (e.g. a),
caratteri speciali (e.g. ?) e valori numerici (e.g. 3)

Esempio:
    stringa = "Ho trovato 2 città di mattoni!"

    Output:
        Uppercase = 1
        Lowercase = 22
        Caratteri Speciali = 1
        Valori numerici = 1

"""
stringa =  """
La Guida galattica per autostoppisti è un libro decisamente notevole, forse il più notevole, sicuramente quello di 
maggiore successo, mai pubblicato dalle grandi case editrici dell'Orsa Minore. Più popolare del "Manuale di economia 
domestica celeste", più venduto di "Altre 53 cose da fare a gravità zero" e più discusso della trilogia di bestseller 
filosofici di Oolon Colluphid "Dove ha sbagliato Dio", "Ancora alcuni tra i più grandi sbagli di Dio" e 
"Ma chi è questo Dio, in fin dei conti?". La Guida ha già soppiantato la grande Enciclopedia galattica, come 
l'indiscussa depositaria di tutta la conoscenza e la saggezza, per due importanti ragioni. Primo, costa un po' meno; 
secondo, reca la scritta, DON'T PANIC, niente panico, in grandi e rassicuranti caratteri sulla copertina.
"""

testo=input("inserisci il testo: ")
special=['|','!','"','£','$','%','&','/','(',')','=','?','^','é','è','*','+','[',']','{','}','ò','@','ç','à','°','#','ù','§',';',',','.',':','-','_','<','>']

# metodo 1 peggiore
count_U=0
count_l=0
count_s=0
count_n=0

for let_U in testo:
	if let_U.isupper():
		count_U+=1
print("Uppercase: ",count_U)

for let_l in testo:
	if let_l.islower():
		count_l+=1
print("Lowercase: ",count_l)

for let_s in testo:
	if let_s in special:
		count_s+=1
print("Special: ",count_s)

for let_n in testo:
	if let_n.isdigit():
		count_n+=1
print("Numbers: ",count_n)
print(" ")

#metodo 2 medio
count_U=0
count_l=0
count_s=0
count_n=0

for let in testo:
	if let.isupper():
		count_U+=1

	elif let.islower():
		count_l+=1

	elif let in special:
		count_s+=1

	elif let.isdigit():
		count_n+=1

print("Uppercase: ",count_U)
print("Lowercase: ",count_l)
print("Special: ",count_s)
print("Numbers: ",count_n)

print(" ")

#Metodo 3 - migliore
count_U=0
count_l=0
count_s=0
count_n=0

for let in testo:
	count_U+=1 if let.isupper()==True else 0
	count_l+=1 if let.islower()==True else 0
	count_s+=1 if let in special else 0
	count_n+=1 if let.isdigit()==True else 0

print("Uppercase: ",count_U)
print("Lowercase: ",count_l)
print("Special: ",count_s)
print("Numbers: ",count_n)

