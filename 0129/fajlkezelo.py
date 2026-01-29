#írás
fajl=open("0129/szoveg.txt","w",encoding="utf-8")

fajl.write("Ez egy szöveg fájl.")
fajl.close()

#olvasás
fajl=open("0129/szoveg.txt","r",encoding="utf-8")
tartalom=fajl.read()
print(tartalom)
fajl.close()