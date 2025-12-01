szam = int(input("Adj meg egy számot: "))

if szam > 0 and szam % 2 == 0:
    print("pozitív páros")
elif szam <= 0:
    print("nem pozitív")
else:
    print("pozitív, de páratlan")