import random

szam = None

while szam is None or szam % 2 != 0:
    szam = random.randint(1, 100)
    print("Kapott szám:", szam)

print("Megálltunk, mert páros számot kaptunk:", szam)