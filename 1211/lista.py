'''import random

Lszam=[]

for i in range(10):
    Lszam.append(random.randint(0,20))

print(Lszam)


vane=False
for i in range(0,9,1):
    if((Lszam[i])*2 == Lszam[i+1]):
        vane=True
        
if(vane==True): 
    print("Van olyan elem a listában, amelyiknek a kétszerese is szerepel utána.")
else: 
    print("Nincs olyan elem a listában, amelyiknek a kétszerese is szerepel utána.")'''


'''import random


szam=int(input("Hány számot szeretnél megadni? "))
Lszam=[]
for i in range(szam):
    Lszam.append(random.randint(0,100))

print(Lszam)
print("legnagyobb szám és a legkisebb szám különbsége: ", max(Lszam)-min(Lszam))'''