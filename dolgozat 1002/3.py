#3,Szeretnénk a félretett pénzünkket betenni bankba, hogy kamatozzon!
#Kérd be a betett pénzösszeget, mennyi a kamat évente (%-ban) valamint, hogy hány évre szeretnéd lekötni!
#A program számolja ki, mennyi lesz a kamat (megtakarítás)?

összeg = float(input("Adja meg mennyi pénzt tesz be: "))
kamat = float(input("Adja meg a kamatot (%): "))
év = int(input("Adja meg mennyi időre teszi be(év):"))

kamat_összeg = összeg * (kamat /100) * év 

vegösszeg = összeg + kamat_összeg

print(f"kamat (ft): {kamat_összeg:.2f} Ft")
print(f"megtakarítás: {vegösszeg:.2f} Ft")