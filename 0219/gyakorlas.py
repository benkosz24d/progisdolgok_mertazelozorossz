diakok = []

with open("0219/diak.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        nev, magassag = sor.strip().split(";")
        diakok.append((nev, int(magassag)))

print("A diákok száma:", len(diakok))

legmagasabb = diakok[0]

for diak in diakok:
    if diak[1] > legmagasabb[1]:
        legmagasabb = diak

print("A legmagasabb tanuló:", legmagasabb[0], "-", legmagasabb[1], "cm")

diakok_rendezve = sorted(diakok, key=lambda x: x[1], reverse=True)

with open("0219/rendezve.txt", "w", encoding="utf-8") as fajl:
    for diak in diakok_rendezve:
        fajl.write(f"{diak[0]};{diak[1]}\n")

print("A rendezett lista kiírva a rendezve.txt fájlba.")