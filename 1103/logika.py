#kérjunk be egy szamot, es vizsgaljuk meg,
#hogy oszthato e 5-el es 3-al

szam=int(input("Szam: "))

if(szam%5==0) and (szam%3==0) :
    print("Osztható 3-al és 5-el is")
else:
    print("Nem osztható mindkét számmal")