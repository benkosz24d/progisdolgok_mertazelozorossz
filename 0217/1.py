# Beolvasás
with open("0217/diakok.txt", "r", encoding="utf-8") as file:
    sorok = file.readlines()

diakok_szama = 0
osszes_eletkor = 0
legmagasabb_nev = ""
legmagasabb_magassag = 0

for sor in sorok:
    adatok = sor.strip().split(";")
    
    nev = adatok[0].strip()
    eletkor = int(adatok[1].strip())
    magassag = int(adatok[2].strip())
    
    diakok_szama += 1
    osszes_eletkor += eletkor
    
    if magassag > legmagasabb_magassag:
        legmagasabb_magassag = magassag
        legmagasabb_nev = nev

atlag_eletkor = osszes_eletkor / diakok_szama

with open("0217/valasz.txt", "w", encoding="utf-8") as file:
    file.write(f"A diákok száma: {diakok_szama} fő\n")
    file.write(f"A legmagasabb diák: {legmagasabb_nev} ({legmagasabb_magassag} cm)\n")
    file.write(f"Az osztály átlagéletkora: {atlag_eletkor:.2f} év\n")

print("A valasz.txt fájl sikeresen létrejött!")
