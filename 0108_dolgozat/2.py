Lkoltesek = ["1200", "1500", "0", "900", "1400", "3150", "0"]
napok = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]

koltesek = []
for x in Lkoltesek:
    koltesek.append(int(x))

atlag = sum(koltesek) / len(koltesek)
kerekitett_atlag = int(atlag + 0.5)
print("Napi átlagos költés:", kerekitett_atlag, "Ft")

db = 0
for k in koltesek:
    if k > 2000:
        db += 1
print("2000 Ft felett volt a költés", db, "alkalommal.")

max_koltes = max(koltesek)
nap = napok[koltesek.index(max_koltes)]
print("A legtöbbet", nap, "nap költötte.")

zsebpenz = int(input("Add meg a heti zsebpénzt (Ft): "))
marad = zsebpenz - sum(koltesek)

if marad > 0:
    print("Maradt pénz a következő hétre:", marad, "Ft")
elif marad == 0:
    print("Pont elfogyott a pénz.")
else:
    print("Nem volt elég a zsebpénz,", -marad, "Ft hiányzott.")