class Auto:
    def __init__(self, tipus, szin, ar):
        self.tipus = tipus
        self.szin = szin
        self.ar = int(ar)

autok_listaja = []

print("Kérlek, add meg 3 autó adatait!")
for i in range(3):
    print(str(i + 1) + ". autó megadása:")
    be_tipus = input("  Típus: ")
    be_szin = input("  Szín: ")
    be_ar = int(input("  Ár (Ft): "))
    
    uj_auto = Auto(be_tipus, be_szin, be_ar)
    autok_listaja.append(uj_auto)

legdragabb_auto = autok_listaja[0] 
for i in range(1, len(autok_listaja)):
    if autok_listaja[i].ar > legdragabb_auto.ar:
        legdragabb_auto = autok_listaja[i]

fajl = open("0420/draga.txt", "w", encoding="utf-8")
kiirando_szoveg = str(legdragabb_auto.tipus) + " típusú " + str(legdragabb_auto.szin) + " színű autó a legdrágább: " + str(legdragabb_auto.ar) + " Ft"
fajl.write(kiirando_szoveg)
fajl.close()

print("\nA legdrágább autó kiírva a fájlba.")

print("\n--- Keresés ---")
keresett = input("Milyen színű autót keresel? ")
van_talalat = False

for auto in autok_listaja:
    if auto.szin.lower() == keresett.lower():
        print("Találtunk: " + auto.tipus + " (" + str(auto.ar) + " Ft)")
        van_talalat = True

if van_talalat == False:
    print("Nincs ilyen színű autó a listában.")

osszeg = 0
for auto in autok_listaja:
    osszeg = osszeg + auto.ar

print("\nAz autók összértéke a kereskedésben: " + str(osszeg) + " Ft")