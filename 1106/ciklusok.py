osszeg=0
for i in range(1,4,1):
    print(i,".jegy: ",end=" ")
    jegy=int(input())
    osszeg+=jegy

print("Átlag: ",round(osszeg/3,2))