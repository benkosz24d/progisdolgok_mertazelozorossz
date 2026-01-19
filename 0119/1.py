nev=input("Név: ")
knev=nev.lower()

lnev=knev.split()

for i in range(len(lnev)):
    lnev[i]=lnev[i].capitalize()
    print(lnev[i])


print(lnev)