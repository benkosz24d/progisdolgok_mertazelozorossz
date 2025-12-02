"""import random

dobas=random.randint(1,6)
db=1
print("Dobásod: ",dobas)

while (dobas!=6):
    print("Nem 6-os, ENTER-rel dobj újra!")
    input()
    dobas=random.randint(1,6)
    db+=1
    print("Dobásod: ",dobas)

print(db,"dobásból sikerült 6-ost dobni!")"""

import random

p1dobas=random.randint(1,6)
p2dobas=random.randint(1,6)
p1db=0
p2db=0
print("1. játékos dobása: ",p1dobas)
print("2. játékos dobása: ",p2dobas)   


while (p1db!=3) or (p2db!=3):
    if (p1dobas>p2dobas):
        print("1. játékos dobta nagyobbat!")
        p1db+=1
        print(p1db,"-",p2db)
    elif (p2dobas>p1dobas):
        print("2. játékos dobta nagyobbat!")
        p2db+=1
        print(p1db,"-",p2db)
    else:
        print("Döntetlen!")
        print(p1db,"-",p2db)
print("Következő kör, üss ENTER-t!")
p1dobas=random.randint(1,6)
p2dobas=random.randint(1,6)
print("1. játékos dobása: ",p1dobas)
print("2. játékos dobása: ",p2dobas)        