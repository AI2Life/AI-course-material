"""
BRUTE FORCE ATTACK
Un attacco di forza bruta è un tentativo di decifrare una password  utilizzando l'approccio della prova e dell'errore
con la speranza di indovinare. Si tratta di un vecchio metodo di attacco, ma è ancora efficace e molto usato
dagli hacker. A seconda della lunghezza e complessità della password, la sua individuazione può richiedere da pochi
secondi a molti anni.

Scrivi uno script che stampa tutte le possibili permutazioni di 3 numeri della lista x.
Esempio:
Input: [1,2,3]
Output:
   1 1 1
   1 1 2
   1 1 3
   1 2 1
   . . .
   . . .
   3 2 2
   3 2 3
   3 3 1
   3 3 2
   3 3 3

"""
x = [8, 9, 2]


for i in range(3):
   for j in range(3):
      for k in range(3):
         print(x[i], x[j], x[k])