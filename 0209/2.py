# fájl megnyitása olvasásra
with open("0209/szam.txt", "r", encoding="utf-8") as f:
    sorok = f.readlines()

szamok = []
for sor in sorok:
    szamok.append(float(sor.strip()))

# 1. Hány db szám van a fájlban
print("A számok darabszáma:", len(szamok))

egesz = []
valos = []

# 2–3. szétválogatás és kerekítés
for szam in szamok:
    if szam.is_integer():
        egesz.append(int(szam))
    else:
        valos.append(round(szam, 1))

# fájlokba írás
with open("egesz.txt", "w", encoding="utf-8") as f:
    for szam in egesz:
        f.write(str(szam) + "\n")

with open("valos.txt", "w", encoding="utf-8") as f:
    for szam in valos:
        f.write(str(szam) + "\n")

# 4. negatív egész számok darabszáma
negativ_egesz = 0
for szam in egesz:
    if szam < 0:
        negativ_egesz += 1

print("Negatív egész számok száma:", negativ_egesz)
