"""szoveg=input("Kérek egy szöveget: ")

nagyszoveg=szoveg.upper()
print(szoveg)
print(nagyszoveg)"""


kor=input("Nagykorú vagy e? (igen/nem) ")
ujkor=kor.lower()

while(ujkor!="igen" and ujkor!="nem" and 
      ujkor!="i" and ujkor!="n"):
    print("Hibás adat!")
    kor=input("Nagykorú vagy e? (igen/nem) ")
    ujkor=kor.lower()

if (ujkor=="igen") or (ujkor[0]=="i"):
    print("Nagykorú vagy.")
else:
    print("Kiskorú vagy.")