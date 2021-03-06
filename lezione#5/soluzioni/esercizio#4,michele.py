"""

Scrivi uno script che prende una frase come input e conta le occorrenze di ogni parola in quella frase.

Ai fini di questo esercizio si può prevedere che una parola sarà sempre una delle seguenti:
    1. Un numero composto da una o più cifre ASCII (cioè "0" o "1234")
    2. Una parola semplice composta da una o più lettere ASCII (cioè "a" o "loro")
    3. Una contrazione di due parole semplici unite da un singolo apostrofo (cioè "s'è" o "l'ha")

Quando si contano le parole si possono assumere le seguenti regole:
    1. Il conteggio è insensibile alle maiuscole (cioè "You", "you", e "YOU" sono 3 usi della stessa parola)
    2. A parte l'apostrofo in una contrazione, tutte le forme di punteggiatura sono ignorate
    3. Le parole possono essere separate da qualsiasi forma di spazio bianco (cioè "\t", "\n", " ")

Esempio:
    Input: "La mia nuova casa è una bella casa"

Output:
    "La" -> 1
    "mia" -> 1
    "nuova" -> 1
    "casa" -> 2
    "è" -> 1
    "una" -> 1
    "bella" -> 1


"""

frase = input("Inserisci una frase: ")

# separa in singoli token (parole)
parti = frase.split()

# parole contiene l'elenco delle parole, occorrenze il numero di ripetizioni
parole =[]
occorrenze = []
grezze = [] # elenco di parole in forma grezza (es. "La")

for p in parti:
    # Ripulisce dai caratteri spuri
    grezza = ""
    for i in range(len(p)):
        if p[i].isalnum() or (p[i] == "'" and 0 < i < len(p)-1):
            grezza+=p[i]

    pulita = grezza.lower()

    if pulita in parole: # Se già incontrata incremento il contatore
        occorrenze[parole.index(pulita)] += 1
    else:
        # altrimenti aggiungo la nuova parola
        parole.append(pulita)
        grezze.append(grezza)
        occorrenze.append(1)

for testo, volte in zip(grezze, occorrenze):
    print(f'"{testo}" -> {volte}')

