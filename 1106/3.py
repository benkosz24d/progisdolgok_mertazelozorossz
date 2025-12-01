maxpont=int(input("Dolgozat max pontszáma: "))
elert=float(input("Elért pontszám: "))

szazalék=(elert/maxpont)*100

if (szazalék<=39):
    print("1-elégtelen")
elif(szazalék<=54):
    print("2-elégséges")
elif(szazalék<=69):
    print("3-közepes")
elif(szazalék<=84):
    print("4-jó")
else:
    print("5-példás")