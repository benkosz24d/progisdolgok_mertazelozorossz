szamok = ["3,24", "1,33", "4,5", "3,33", "4,25"]
ujszamok = []

for elem in szamok:
    ujszamok.append(float(elem.replace(",", ".")))

atlag = round(sum(ujszamok) / len(ujszamok), 2)

print("Javított számok:", ujszamok)
print("Átlag:", atlag)
