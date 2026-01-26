"""def koszones(nev):
    print("Hello "+nev+", üdvözöllek a programban!")

def osszead(a,b):
    return a + b
#fő program ->main()
nev=input("Mi a neved? ")
koszones(nev)"""

def osszead(a,b):
    return a + b

def kivon(a,b):
    return a - b

def szoroz(a,b):
    return a * b

def oszt(a,b):
    if b==0:
        return "Nullával nem lehet osztani!"
    return a / b

def gyok(a):
    None
#fő program ->main()
szam1=int(input("Adj meg egy számot: "))
szam2=int(input("Adj meg egy másik számot: "))
muvelet=input("Milyen műveletet szeretnél végezni? (+,-,*,/): ")

if muvelet=="+":
    print(osszead(szam1,szam2))
elif muvelet=="-":
    print(kivon(szam1,szam2))
elif muvelet=="*":
    print(szoroz(szam1,szam2)) 
elif muvelet=="/":
    print(oszt(szam1,szam2))