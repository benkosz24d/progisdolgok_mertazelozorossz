with open("0212-dolgozat/lotto.txt", "r") as file:
    sorok = file.readlines()

huzasok = []
for sor in sorok:
    szamok = list(map(int, sor.strip().split()))
    huzasok.append(szamok)

print("Sorsolások száma:", len(huzasok))


for i, het in enumerate(huzasok, start=1):
    print(str(i) + ". hét nyerőszámai:", het)


gyakorisag = {}

for het in huzasok:
    for szam in het:
        if szam in gyakorisag:
            gyakorisag[szam] += 1
        else:
            gyakorisag[szam] = 1

leggyakoribb = max(gyakorisag, key=gyakorisag.get)

print("Leggyakoribb szám:", leggyakoribb)
print("Előfordulások száma:", gyakorisag[leggyakoribb])


tippek = list(map(int, input("Adj meg 5 számot szóközzel elválasztva: ").split()))

max_talalat = 0

for het in huzasok:
    talalat = 0
    for szam in tippek:
        if szam in het:
            talalat += 1

    if talalat > max_talalat:
        max_talalat = talalat

print("Ennyi találatod lett volna a legjobb héten:", max_talalat)


rendezett = sorted(gyakorisag.items(), key=lambda x: x[1], reverse=True)

tuti_tipp = []
for i in range(5):
    tuti_tipp.append(rendezett[i][0])

with open("0212-dolgozat/tipp.txt", "a") as file:
    file.write("Tuti tipp: " + " ".join(map(str, tuti_tipp)) + "\n")

print("A tuti tipp hozzáadva a tipp.txt fájlhoz.")
