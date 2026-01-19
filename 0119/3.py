fajl=input("Fájl neve: ")

Lfajl=fajl.split(".")


fajlnev=""
for i in range(len(Lfajl)-1):
    print(Lfajl[i])
    fajlnev+=Lfajl[i]+"."

print("fájlnév:",fajlnev)
print("kiterjesztés:",Lfajl[-1])