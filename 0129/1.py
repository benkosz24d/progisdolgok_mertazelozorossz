import random

def lista_feltolt():
    lista = []
    for i in range(10):
        lista.append(random.randint(0, 9))
    return lista

def paratlan_db(lista):
    db = 0
    for szam in lista:
        if szam % 2 == 1:
            db += 1
    return db

def egyedi(lista):
    uj_lista = []
    for szam in lista:
        if szam not in uj_lista:
            uj_lista.append(szam)
    return uj_lista

def hianyzo(lista):
    hianyzo_szamok = []
    for i in range(10):
        if i not in lista:
            hianyzo_szamok.append(i)
    return hianyzo_szamok


lista = lista_feltolt()
print("Lista:", lista)

print("Páratlan számok száma:", paratlan_db(lista))

print("Ismétlődések nélkül:", egyedi(lista))

hianyzoak = hianyzo(lista)
if len(hianyzoak) > 0:
    print("Hiányzó számok:", hianyzoak)
else:
    print("Nincs hiányzó szám 0–9 között.")
