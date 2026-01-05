"""Lnevek=["andi","Tamás","Réka","Aladár","Tímea"]

Lnevek.sort()
print(Lnevek)"""


import locale
locale.setlocale(locale.LC_COLLATE, 'hu_HU.UTF-8')

Lnevek=["Andi","Tamás","Réka","Ákos","Aladár","Tímea","2","100","40"]

Lnevek.sort(key=locale.strxfrm)
print(Lnevek)
