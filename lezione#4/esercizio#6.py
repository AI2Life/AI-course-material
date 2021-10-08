"""
Scrivi uno script che unisce gli elmenti di una lista di liste (x) in una singola lista e la
stampa in ordine crescente.

ESEMPIO:
x = [[1,2],
    [4,5],
    [3,6]]

    OUTPUT:
    [1,2,3,4,5,6]
"""

x = [[28, 28, 26, 26, 24, 22, 25, 22, 27, 24],
     [12, 18, 11, 19, 14, 19, 17, 11, 10, 11],
     [5, 2, 3, 6, 6, 6, 5, 3, 8, 2],
     [32, 34, 32, 32, 33, 38, 33, 34, 33, 30]]

a = list()
for i in x:
     a += i

a.sort()
print(a)
