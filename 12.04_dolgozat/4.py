db_negativ = 0
osszeg_negativ = 0

for i in range(5):
    szam = float(input("Adj meg egy számot: "))
    if szam < 0:
        db_negativ += 1
        osszeg_negativ += szam

print("Negatív számok száma:", db_negativ)
if db_negativ > 0:
    print("Negatív számok átlaga:", osszeg_negativ / db_negativ)
else:
    print("Nincs negatív szám.")