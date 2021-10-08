"""
Scrivi uno script che rimuove i duplicati dalla lista x
"""
x = [1, 2, 5, 3, 1, 6, 1, 2, 9, 8, 9, 5, 5, 7, 2, 1, 4, 2, 9, 5, 2, 7, 5, 6, 7, 6, 7, 9, 6, 3,
     4, 5, 7, 1, 4, 5, 5, 7, 1, 6, 2, 5, 8, 8, 2, 1, 8, 2, 5, 4, 6, 7, 6, 4, 8, 7, 7, 2, 9, 2]

uniques = list()
for i in range(len(x)):
     if x[i] not in uniques:
          uniques.append(x[i])
print(uniques)


