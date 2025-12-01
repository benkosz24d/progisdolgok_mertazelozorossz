#1, Írj programot, mely beolvassa egy derékszögű háromszög két befogóját,
#és megadja az átfogójának a hosszát! 
#Az átfogót 2 tizedesjeggyel add meg!
import math

a = float(input("Add meg a derékszögű háromszög első befogóját"))
b = float(input("Add meg a derékszögű háromszög második befogóját"))

c = math.sqrt(a**2 + b**2)

print(f"Az átfogó hossza: {c:.2f}")