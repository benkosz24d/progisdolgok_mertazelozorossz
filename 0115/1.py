szamok = ["3,24", "1,33", "4,5", "3,33", "4,25"]

javított_szamok = [float(szam.replace(",", ".")) for szam in szamok]

atlag = sum(javított_szamok) / len(javított_szamok)

print("Javított számok:", javított_szamok)
print("Átlag:", atlag)
