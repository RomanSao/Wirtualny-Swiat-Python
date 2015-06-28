import random
from Zwierzeta.Zwierze import Zwierze

class Antylopa(Zwierze):
    def __init__(self,x,y,sila,inicjatywa,swiat):
        Zwierze.__init__(self,sila,inicjatywa,x,y,'A',swiat,"Antylopa")
        
    def Akcja(self):
        Zwierze.Akcja(self)
        __ruch = random.randint(0,7)
        __x, __y = self.LosujRuch(__ruch)
        __tmp = 0           
        while __tmp<self._swiat.ZwrocRozmiar():
            if self._swiat.organizmZwrocPolozenieX(__tmp) == __x and self._swiat.organizmZwrocPolozenieY(__tmp) == __y:
                if self._swiat.organizmZwrocZnak(__tmp) == 'T' and self._swiat.organizmZwrocZnak(__tmp) == 'M' and self._swiat.organizmZwrocZnak(__tmp) == 'G' and self._swiat.organizmZwrocZnak(__tmp) == 'J':
                    break
                self._polozenieX = __x
                self._polozenieY = __y
                __los = random.randint(0,3)
                if __los < 2:
                    __x,__y = self.ZnajdzBezpieczne()
                    if self._polozenieX != __x or self._polozenieY != __y:
                        print "Antylopa ucieka"
                    else:
                        print "Antylopa nie ma gdzie uciec"
                break
            __tmp = __tmp + 1
        self._polozenieX = __x
        self._polozenieY = __y
    
    def Kolizja(self, numerOrganizmu, numerOrganizmu2, polozenieX, polozenieY):
        __los = random.randint(0,3)
        if __los < 2:
            __x,__y = self.ZnajdzBezpieczne()
            if self._polozenieX != __x or self._polozenieY != __y:
                print "Antylopa ucieka"
                self._polozenieX = __x
                self._polozenieY = __y
            else:
                print "Antylopa nie ma gdzie uciec"
                Zwierze.Kolizja(self, numerOrganizmu, numerOrganizmu2, polozenieX, polozenieY)
       
        
        