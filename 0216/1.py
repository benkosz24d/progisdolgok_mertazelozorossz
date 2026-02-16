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
   
