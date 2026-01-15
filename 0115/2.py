szoveg = input("Adj meg egy szöveget: ")

osszeg = 0
szam = ""

for karakter in szoveg:
    if '0' <= karakter <= '9':
        szam += karakter
    else:
        if szam != "":
            osszeg += int(szam)
            szam = ""

if szam != "":
    osszeg += int(szam)

print("A szövegben található számok összege:", osszeg)
