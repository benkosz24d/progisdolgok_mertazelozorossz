szam = input("Adj meg egy számot: ")

osszeg = 0
for karakter in szam:
    osszeg += int(karakter)

print("A számjegyek összege:", osszeg)