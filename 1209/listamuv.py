"""Lszam=[]
szam=int(input("Adj meg egy szamot: "))
Lszam.append(szam)

print(Lszam)
szam=int(input("Adj meg egy szamot: "))
Lszam.append(szam)
print(Lszam)"""

"""import random

Lszam=[] #Üres lista létrehozása

for i in range(10):
    Lszam.append(random.randint(1,100)) #10 véletlen szám hozzáadása 1 és 100 között

print(Lszam)"""

"""import random

Lszamok=[]
osszeg=0
for i in range(10):
    szam=random.randint(1,100)
    Lszamok.append(szam)
    osszeg+=szam   

print("A listában lévő számok:" , Lszamok )
print("A számok összege:", osszeg) """

import random
Lszamok=[] #Üres lista létrehozása
for i in range(10):
    Lszamok.append(random.randint(1,100)) #10 véletlen szám hozzáadása 1 és 100 között

print("A listában lévő számok:" , Lszamok )
#print(sum(Lszamok)/len(Lszamok))  #Összeg kiszámítása a beépített sum() függvénnyel
#print(min(Lszamok))  #Legkisebb elem kiíratása a beépített min() függvénnyel
#print(max(Lszamok))  #Legnagyobb elem kiíratása a beépített max() függvénnyel
Lszamok.sort()  #Lista rendezése növekvő sorrendbe a beépített sort() metódussal
print("Rendezett lista:", Lszamok)