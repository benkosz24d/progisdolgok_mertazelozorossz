"""osszeg=0

for i in range(3):
    szam=int(input("Szám: "))
    osszeg=osszeg+szam

print(osszeg)
print(i)"""


szam=int(input("Melyik szozó táblát szeretnéd: "))

for i in range(1,11,1):
    print(i,'*',szam,'=',i*szam)
