szoveg = input("Adj meg egy szöveget: ")

db = 0
for betu in szoveg:
    if betu == "s":
        db += 1

print(db)