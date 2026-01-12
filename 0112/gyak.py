"""Készíts 2db 5 elemű tetszőleges számokból álló listát, melyben csak 1 jegyű pozitív számok vannak.
Fésüld össze a két listát egybe úgy, hogy minden elem csak egyszer szerepeljen, és növekvő
sorrendben legyenek!"""

import random

lista1 = []
lista2 = []

for i in range(5):
    lista1.append(random.randint(0, 9))
    lista2.append(random.randint(0, 9))

print(lista1)
print(lista2)

osszefuzott=[]
for elem in lista1:
    if elem not in osszefuzott:
        osszefuzott.append(elem)

for elem in lista2:
    if elem not in osszefuzott:
        osszefuzott.append(elem)
osszefuzott.sort()
print(osszefuzott)