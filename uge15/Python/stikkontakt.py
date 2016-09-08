
class Stikkontakt(object):
    """Modellere en stikkontakt"""
    
    def __init__(self):
        self.tilstand = 0 # Default: Slukket
            
    def skift(self):
        """Metode ansvarlig for tilstandsskift"""
        if self.tilstand==0: # Tilstand er slukket
            self.tilstand=1 # Skift til taendt
        else: # Tilstand er taendt
            self.tilstand=0 # Skift til slukket

    def __str__(self):
        if self.tilstand==0:
            return "Kontakten er slukket"
        else:
            return "Kontakten er taendt"



kontakt = Stikkontakt()
print kontakt
for i in range(5):
    kontakt.skift()
    print kontakt
