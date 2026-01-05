import random

nevek = []

for i in range(5):
    nev = input("Adj meg egy nevet: ")
    nevek.append(nev)

gyoztes = random.choice(nevek)
print("A sorsolás nyertese:", gyoztes)