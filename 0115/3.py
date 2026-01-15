szo = input("Adj meg egy szót: ")

palindrom = True
hossz = len(szo)

for i in range(hossz // 2):
    if szo[i] != szo[hossz - 1 - i]:
        palindrom = False
        break

if palindrom:
    print("A szó palindrom.")
else:
    print("A szó nem palindrom.")