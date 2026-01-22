mondat = input("Adj meg egy mondatot: ")

if mondat.endswith("?"):
    print("A mondat kérdő.")
elif mondat.endswith("!"):
    print("A mondat felszólító vagy óhajtó.")
elif mondat.endswith("."):
    print("A mondat kijelentő.")
else:
    print("Nem felismerhető a mondat típusa.")