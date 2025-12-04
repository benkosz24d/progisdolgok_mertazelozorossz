x = int(input("Add meg az x értékét: "))
osszeg = 0

for szam in range(1, x + 1):
    if szam % 3 == 0 and szam % 4 == 0:
        osszeg += szam

print("Az 1-től", x, "ig terjedő számok összege, amelyek oszthatók 3-mal és 4-gyel:", osszeg)