a = float(input("Add meg az első oldalt (a): "))
b = float(input("Add meg a második oldalt (b): "))
c = float(input("Add meg a harmadik oldalt (c): "))

if a + b > c and a + c > b and b + c > a:
    print("Ezekből az oldalakból szerkeszthető háromszög.")
else:
    print("Ezekből az oldalakból NEM szerkeszthető háromszög.")