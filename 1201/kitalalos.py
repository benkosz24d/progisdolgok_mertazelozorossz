import random


gondolt = random.randint(1, 100)

tipp=int(input("1.Tpped: "))
db=1

while (tipp!=gondolt):
    if (tipp<gondolt):
        print("Nagyobb")
    if (tipp>gondolt):
        print("Kisebb")
    print(db+1,". Tipped: ",end=" ")
    tipp=int(input())
    db+=1

print("Eltaláltad!")