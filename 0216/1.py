class HíresNő:
    def __init__(self, név, foglalkozás,nemzetiség):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzetiség = nemzetiség
    def elotag(self):    
        if self.nemzetiség=="a":
            return "MS."
        else:
            return "Frau"

        
#---------MAIN----------

hires_nok=[] 

for i in range(3):
    név=input("Név: ")
    foglalkozás=input("Foglalkozás: ")
    nemzetiség=input("Nemzetiség (a/n): ")
    nő=HíresNő(név,foglalkozás,nemzetiség)
    hires_nok.append(nő)

for nő in hires_nok:
    print(nő.elotag(),nő.név, "egy híres", nő.foglalkozás)