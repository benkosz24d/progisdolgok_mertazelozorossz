import math

a=float(input("termék ára: "))
b=float(input("kedvezmény százalékban: "))

kedvezmeny = a * (b / 100)
eredmény= a - kedvezmeny
print("Ára most: ", round(eredmény, 2))