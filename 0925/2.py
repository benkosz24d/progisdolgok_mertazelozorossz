import math 


r = float(input("Add meg a kör sugarát: "))

kerulet = 2 * math.pi * r
terulet = math.pi * r ** 2

print(f"A kör kerülete: {kerulet:.2f}")
print(f"A kör területe: {terulet:.2f}")