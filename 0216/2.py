class Diak:
    def __init__(self, nev, magassag):
        self.nev = nev
        self.magassag = magassag

    def __str__(self):
        return f"{self.nev} - {self.magassag} cm"


diakok = []

for i in range(3):
    nev = input(f"{i+1}. diák neve: ")
    magassag = float(input(f"{nev} magassága (cm): "))
    diak = Diak(nev, magassag)  
    diakok.append(diak)

legmagasabb = diakok[0]

for diak in diakok:
    if diak.magassag > legmagasabb.magassag:
        legmagasabb = diak

# Eredmény kiírása
print("\nA legmagasabb diák:")
print(legmagasabb)
