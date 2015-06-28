from Zwierzeta.Zwierze import Zwierze

SIZE = 20

class Czlowiek(Zwierze):
    def __init__(self,x,y,sila,inicjatywa,cooldown,swiat):
        Zwierze.__init__(self,sila,inicjatywa,x,y,'C',swiat,"Czlowiek")
        self._kierunek = 0
        self._cooldown = cooldown
        
    def ZmienKierunek(self,kierunek):
        self._kierunek = kierunek
        
    def ZwrocCooldown(self):
        return self._cooldown
        
    def Akcja(self):
        if self._cooldown>0:
            if self._cooldown>5:
                self._sila=self._sila - 1
            self._cooldown = self._cooldown - 1
        if self._kierunek == 1:
            if self._polozenieX>0:
                self._polozenieX = self._polozenieX - 1
        elif self._kierunek == 2:
            if self._polozenieX<SIZE-1:
                self._polozenieX = self._polozenieX + 1
        elif self._kierunek == 3:
            if self._polozenieY>0:
                self._polozenieY = self._polozenieY - 1
        elif self._kierunek == 4:
            if self._polozenieY<SIZE-1:
                self._polozenieY = self._polozenieY + 1
        self._kierunek = 0
        
    def UzyjMiksturyPanoramiksa(self):
        if self._cooldown == 0:
            self._sila = self._sila + 5
            self._cooldown = 10
            print "Czlowiek wypil Miksture Panoramiksa"
        else:
            print "Czlowiek nie moze wypic Mikstury Panoramiksa"