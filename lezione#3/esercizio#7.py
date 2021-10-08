"""
ESERCIZIO 7
Scrivi uno script che prende come input un numero intero n e stampa questo pattern:
ESEMPIO n = 99:

1-----99

2-----98

3-----97

. .

. .

. .

98-----2

99-----1
"""

n = int(input())

for i in range(n):
    print(i, "------------", n-i)