szamok = []

while True:
    adat = input("Adj meg egy számot (stop a kilépéshez): ")

    if adat == "stop":
        break

    szamok.append(int(adat))

print("Beolvasott számok száma:", len(szamok))

legnagyobb = max(szamok)
legkisebb = min(szamok)
kulonbseg = legnagyobb - legkisebb

print("Legnagyobb és legkisebb különbsége:", kulonbseg)

harommal_oszthato = []

for szam in szamok:
    if szam % 3 == 0:
        harommal_oszthato.append(szam)

print("3-mal osztható számok:", harommal_oszthato)