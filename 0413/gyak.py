class Tanulo:
    def __init__(self, sor):

        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.osztaly = adatok[1]
        
        atlag_szoveg = adatok[2].replace(',', '.')
        self.atlag = float(atlag_szoveg)
        
        if adatok[1][0:2].isdigit():
            self.evfolyam = int(adatok[1][0:2])
        else:
            self.evfolyam = int(adatok[1][0])

diakok = []
with open('0413/Diak.txt', 'r', encoding='utf-8') as f:
    for sor in f:
        if sor.strip() != "":
            diakok.append(Tanulo(sor))

letszam = len(diakok)
print("A csoport létszáma:", letszam, "fő")

osszeg = 0
for d in diakok:
    osszeg = osszeg + d.atlag
csoport_atlag = osszeg / letszam
print("A csoportátlag:", round(csoport_atlag, 2))

legjobb = diakok[0]
for i in range(1, len(diakok)):
    if diakok[i].atlag > legjobb.atlag:
        legjobb = diakok[i]
print("A legjobb tanuló:", legjobb.nev, "átlaga:", legjobb.atlag)

hianyzok = []
for keresett_evf in range(9, 13):
    van_ilyen = False
    for d in diakok:
        if d.evfolyam == keresett_evf:
            van_ilyen = True
            break
            
    if van_ilyen == False:
        hianyzok.append(keresett_evf)

if len(hianyzok) == 0:
    print("Minden évfolyamról (9-12) van tanuló a csoportban.")
else:
    print("Nem minden évfolyam szerepel. Hiányzik:", hianyzok)
