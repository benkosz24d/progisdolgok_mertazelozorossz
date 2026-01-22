mondat = "Ez a mondat milyen hosszu"

szavak = mondat.split()
hosszak = []

for szo in szavak:
    hosszak.append(len(szo))

print("Szavak:", szavak)
print("Szavak hossza:", hosszak)