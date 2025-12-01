i=1
while(i<=5):
    print(i,end="")

i+=1

print()
for i in range (1,6,1):
    print(i,end="")

    szam=int (input("szam"))
    while (szam!=0):
        szam=int(input("szam:"))


        osszeg=0

        while (osszeg<100):
            szam=int(input("szam:"))
            osszeg=osszeg+szam