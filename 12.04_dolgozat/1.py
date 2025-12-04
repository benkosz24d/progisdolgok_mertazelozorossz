import math

n = int(input("Adjon meg egy n értéket: "))

darab = 0
osszeg = 0

for i in range(1, n + 1):
    if math.sqrt(i) > 5:
        darab += 1
        osszeg += i

print(f"Azon számok darabszáma, amelyeknek a négyzetgyöke nagyobb, mint 5: {darab}")
print(f"Az ilyen számok összege: {osszeg}")
