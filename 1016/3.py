'''import random

szam=0
penz=random.randint(1,2) #fej=1, iras=2
tipp=input("Fej vagy írás: ")

if(tipp=="Fej"):
    tippszam=1
else:
    tippszam=2

if(tipp==penz):
    print("Eltalaltad, fej!")
elif(tippszam==penz):
    print("Nem talált, írás volt!")
else:
    print("Nem talált, fej volt!")'''

import random

penz=["fej","írás"]
feldob=random.choice(penz)
tipp=input("Fej vagy írás?(csupa kis betűvel írd) ")
tipp.lower()

if(tipp==feldob):
    print("Eltaláltad")
else:
    print("Nem találtad el")