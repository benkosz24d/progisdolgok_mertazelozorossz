while True:
    n = float(input("Adj egy számot: "))
    if n ** 2 < 100:
        print("A szám négyzete kisebb mint 100,próbáld újra.")
    else:
        print("A szám négyzete nem kisebb mint 100, kilépés.")
        break