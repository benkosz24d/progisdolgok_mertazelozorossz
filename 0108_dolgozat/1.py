jegyek = [2, 2, 4, 5, 5, 3]


atlag = sum(jegyek) / len(jegyek)
print("Átlag:", atlag)

if atlag % 1 == 0.5:
    valasz = input("Az átlag x.5. Szeretnél javítani? (igen/nem): ")

    if valasz == "igen":
        uj_jegy = int(input("Add meg a javítás jegyét: "))
        jegyek.append(uj_jegy)
        atlag = sum(jegyek) / len(jegyek)
        print("Új átlag:", atlag)
    else:
        print("Nem javított, marad az eredmény.")

if atlag > 4.5:
    felevi = 5
elif atlag > 3.5:
    felevi = 4
elif atlag > 2.5:
    felevi = 3
elif atlag > 1.5:
    felevi = 2
else:
    felevi = 1
print("Félévi jegy:", felevi)