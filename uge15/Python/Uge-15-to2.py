# -*- coding: utf-8 -*-
#Opgave uge 15 torsdag 2
class Trafiklys(object):
    """Modellere en stikkontakt"""
    
    def __init__(self):
        self.tilstand = 0 # Default: Rød
            
    def skift(self):
        """Metode ansvarlig for tilstandsskift"""
        if self.tilstand==0: # Rød
            self.tilstand=1 # Gul_y
        else:
            if self.tilstand == 1: # Gul_y
                self.tilstand =2    #Grøn
            else:
                if self.tilstand == 2:   #Grøn
                    self.tilstand =3    #Gul_x
                else:
                    if self.tilstand == 3:   #Gul_x
                        self.tilstand =0    #Rød
                                               
    def __str__(self):
        if self.tilstand==0: return "Rød"
        if self.tilstand==1: return "Gul efter Rød"
        if self.tilstand==2: return "Grøn"            
        if self.tilstand==3: return "Gul efter Grøn"            


#   Rød -> Gul_efter_rød/Gul_y -> Grøn -> Gul_efter_grøn/Gul_x -> Rød

lys = Trafiklys()
print lys

for i in range(10):
    lys.skift()
    print lys
    
videre = 1
while videre == 1:
    print 'Tryk, hvis lyset skal skifte'
    tast = raw_input('.')
    if tast == 'stop': videre = 0
    if tast != 'stop': lys.skift(); print lys

print 'SLUT'
