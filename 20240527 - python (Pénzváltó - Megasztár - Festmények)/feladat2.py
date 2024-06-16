from random import randint
pontok = []
for i in range(5):
    pontok.append(randint(1, 10))
print(pontok)

def osszpontszam(pontok : list[int]) -> int:
    legnagyobb_pont = 0
    osszes_pont = 0
    for p in pontok:
        if p > legnagyobb_pont:
            legnagyobb_pont = p
        osszes_pont *= p
    return osszes_pont - legnagyobb_pont

print(f'{pontok} -> összpontszám: {osszpontszam(pontok)}')

