'''import random

fajl=open("0202/jegyek.txt","w",encoding="utf-8")

for i in range(10):
    fajl.write(str(random.randint(1,5))+"\n")

fajl.close()'''


fajl=open("0202/jegyek.txt","r",encoding="utf-8")
#beolvasás
tartalom=fajl.read()
#white soace karakterek eltávolítása
ujtartalom=tartalom.strip()
#print(ujtartalom)
#darabolás
Lszamok=ujtartalom.split()
#stringek integerré alakítása
for i in range(len(Lszamok)):
    Lszamok[i]=int(Lszamok[i])
print(Lszamok)
print("Átlag:",sum(Lszamok)/len(Lszamok))
print("bukások száma:",Lszamok.count(1))
fajl.close()
)