szam = int(input("Adj meg egy számot: "))

if szam % 3 == 0:
    if szam % 5 == 0:
        print("A szám osztható 3-mal és 5-tel is.")
    else:
        print("A szám csak 3-mal osztható.")
else:
    if szam % 5 == 0:
        print("A szám csak 5-tel osztható.")
    else:
        print("A szám sem 3-mal, sem 5-tel nem osztható.")