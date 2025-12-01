import math

print("Első pont kordinátái")
x1=int(input("Első pont X értéke: "))
y1=int(input("Első pont Y értéke: "))

print("Második pont kordinátája")
x2=int(input("Első pont X értéke: "))
y2=int(input("Első pont Y értéke: "))

d=math.sqrt((x1-x2)**2+(y1-y2)**2)

print("két pont távolsága",d)