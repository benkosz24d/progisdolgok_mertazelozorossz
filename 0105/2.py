lista1 = [3, 7, 1, 9, 5]
lista2 = [2, 5, 8, 3, 6]
# Listák összefésülése, ismétlődések kiszűrése
egyesitett = set(lista1 + lista2)

# Visszaalakítás listává és rendezés
eredmeny = sorted(egyesitett)

print("1. lista:", lista1)
print("2. lista:", lista2)
print("Összefésült, rendezett lista:", eredmeny)