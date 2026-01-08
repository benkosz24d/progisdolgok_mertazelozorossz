import random

honapok = ["Január", "Február", "Március", "Április", "Május", "Június", 
           "Július", "Augusztus", "Szeptember", "Október", "November", "December"]

homersekletek = []
for i in range(12):
    homersekletek.append(random.randint(-20, 40)) 

print("Havi átlaghőmérsékletek:", homersekletek)

fagyos_honapok = 0
for h in homersekletek:
    if h < 0:
        fagyos_honapok += 1
print("Fagyos hónapok száma:", fagyos_honapok)

osszeg = 0
for h in homersekletek:
    osszeg += h
atlag_homerseklet = osszeg / len(homersekletek)
print("Éves átlaghőmérséklet:", round(atlag_homerseklet, 1), "°C")

max_homerseklet = homersekletek[0]
min_homerseklet = homersekletek[0]
max_index = 0
min_index = 0

for i in range(1, len(homersekletek)):
    if homersekletek[i] > max_homerseklet:
        max_homerseklet = homersekletek[i]
        max_index = i
    if homersekletek[i] < min_homerseklet:
        min_homerseklet = homersekletek[i]
        min_index = i

print(f"Legmelegebb hónap: {honapok[max_index]} ({max_homerseklet} °C)")
print(f"Leghidegebb hónap: {honapok[min_index]} ({min_homerseklet} °C)")

for i in range(len(homersekletek)):
    if homersekletek[i] >= 30:
        print(f"Hőség volt {honapok[i]} hónapban!")