a = float(input("Add meg az első számot: "))
b = float(input("Add meg a második számot: "))
c = float(input("Add meg a harmadik számot: "))


if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b


print("A számok növekvő sorrendben:", a, b, c)