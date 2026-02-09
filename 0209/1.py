import locale
locale.setlocale(locale.LC_ALL, 'hu_HU.UTF-8')
fajl=open("0209/nevek.txt","r",encoding="UTF-8")

tartalom=fajl.read()


Lnev=tartalom.split("\n")
print("Nevek:",Lnev)
print("Nevek száma:",len(Lnev)-1) # -1 mert az utolsó üres sor miatt egyel több elem van a listában
rendezettnevek=sorted(Lnev, key=locale.strxfrm)
print("Rendezett lista:",rendezettnevek)

nev=input("Adj meg egy nevet: ")
if nev in Lnev:
    print("A név szerepel a listában.")
else:
    print("A név nem szerepel a listában.")




fajl.close()