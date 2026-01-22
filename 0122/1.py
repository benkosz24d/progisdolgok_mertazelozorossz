import random

lista = []
for i in range(10):
    lista.append(random.randint(0, 9))

print("A lista:", lista)

paratlanok_szama = 0
for szam in lista:
    if szam % 2 == 1:
        paratlanok_szama += 1

print("Páratlan számok száma:", paratlanok_szama)

egyedi_lista = []
for szam in lista:
    if szam not in egyedi_lista:
        egyedi_lista.append(szam)

print("Ismétlődés nélkül:", egyedi_lista)

hianyzok = []
for i in range(10):
    if i not in lista:
        hianyzok.append(i)

if len(hianyzok) == 0:
    print("Minden szám szerepel 0 és 9 között.")
else:
    print("Hiányzó számok:", hianyzok)