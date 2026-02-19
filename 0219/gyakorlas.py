class Diak:
    def __init__(self, nev, magassag):
        self.nev = nev
        self.magassag = magassag

#fájl feldolgozás
fajl=open("0219/diak.txt","r",encoding="UTF-8")
Ltartalom=fajl.read().split("\n")

#üres lista létrehozása
Ldiakok=[]

#; mentén szétválasztjuk a sort
for sor in Ltartalom:
    darabok=sor.split(";")
    nev=darabok[0]
    magassag=int(darabok[1])
    #példányosítás - osztály   
    diak=Diak(nev,magassag)
    Ldiakok.append(diak)

#1. feladat
print("Diákok száma:",len(Ldiakok),"fő")

#2.feladat
legmagasabb=max(Ldiakok,key=lambda m: m.magassag)
print("Legmagasabb diák:",legmagasabb.nev,"magassága:",legmagasabb.magassag,"cm")

#3.feladat
Lrendezett=sorted(Ldiakok,key=lambda m: m.magassag)