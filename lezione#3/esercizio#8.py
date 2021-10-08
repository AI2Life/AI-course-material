"""
ESERCIZIO 8
Scrivi uno script che prende 8 input (8 numeri interi o float) e calcola la media.
"""

a = 0
for i in range(8):
    a += int(input())
print(a/8)