eletkor = int(input("Add meg az életkorod: "))
van_kartya = input("Van belépőkártyád? (igen/nem): ").lower() == "igen"

if eletkor > 18 and van_kartya:
    print("Beléphetsz!")
else:
    print("Nem léphetsz be!")