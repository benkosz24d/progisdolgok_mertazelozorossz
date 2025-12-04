m = int(input("Add meg az m értékét: "))
db = 0

for szam in range(2, m + 1):
    if all(szam % i != 0 for i in range(2, szam)):
        db += 1

print("Prímek száma 2-től", m, "ig:", db)