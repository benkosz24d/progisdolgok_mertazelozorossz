Lfiz = [12995, 11786, 21850, 14561, 889, 7600, 6999, 18370, 8120]

# Teljes havi kiadás
osszeg = sum(Lfiz)

# Átlagos költés egy vásárlásra
atlag = osszeg / len(Lfiz)

print("Teljes havi kiadás:", osszeg, "Ft")
print("Átlagos költés egy vásárlásra:", round(atlag, 2), "Ft")