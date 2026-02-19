with open("0219/diak.txt", "r", encoding="utf-8") as file:
    sorok = file.readlines()

diakok_szama = 0
legmagasabb_nev = ""
legmagasabb_magassag = 0
for sor in sorok:
    adatok = sor.strip().split(";")
    
    nev = adatok[0].strip()
    magassag = int(adatok[1].strip())
    
    diakok_szama += 1
    
    if magassag > legmagasabb_magassag:
        legmagasabb_magassag = magassag
        legmagasabb_nev = nev

with open("0219/valasz.txt", "w", encoding="utf-8") as file:
    file.write(f"A diákok száma: {diakok_szama} fő\n")
    file.write(f"A legmagasabb diák: {legmagasabb_nev} ({legmagasabb_magassag} cm)\n")
print("A valasz.txt fájl sikeresen létrejött!")
