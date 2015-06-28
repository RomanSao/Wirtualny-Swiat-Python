import random
from Glowny.Organizm import Organizm

SIZE = 20

class Roslina(Organizm):
    
    def __init__(self, sila, inicjatywa, polozenieX, polozenieY, znak, swiat, nazwa):
        Organizm.__init__(self,sila, inicjatywa, polozenieX, polozenieY, znak, swiat, nazwa)
        
    def Akcja(self):
        __x = 0
        __y = 0
        __tmp = 0
        __czyPuste = 1
        __prawdopodobienstwo = random.randint(0,100)
        
        if __prawdopodobienstwo>95:
            losuj = random.randint(0,2)
            if losuj == 0:
                __x = self.losujPolozenieX(self._polozenieX,self._polozenieY)
                __y = self._polozenieY
            elif losuj == 1:
                __y = self.losujPolozenieY(self._polozenieY,self._polozenieX)
                __x = self._polozenieX
            elif losuj == 2:
                __x = self.losujPolozenieX(self._polozenieX,self._polozenieY)
                __y = self.losujPolozenieY(self._polozenieY,self._polozenieX)
                
            __tmp = 0
            __czyPuste = 1              
            while __tmp<self._swiat.ZwrocRozmiar():
                if self._swiat.organizmZwrocPolozenieX(__tmp) == __x and self._swiat.organizmZwrocPolozenieY(__tmp) == __y:
                    __czyPuste = 0
                    break
                __tmp = __tmp + 1                  
            if __czyPuste == 1:
                self._swiat.DodajOrganizm(__x,__y,0,0,self._znak,self._swiat)  
                print self._nazwa, " rozprzestrzenia sie"
                    
    def losujPolozenieX(self,x,y):
        __strona = random.randint(0,1)
        
        if x>0 and x<SIZE-1:
            if __strona == 0:
                x = x + 1
            else:
                x = x - 1
                
        return x
    
    def losujPolozenieY(self,y,x):
        __strona = random.randint(0,1)
        
        if y>0 and y<SIZE-1:
            if __strona == 0:
                y = y + 1
            else:
                y = y - 1
                
        return y
    
    def Kolizja(self,numerOrganizmu, numerOrganizmu2, polozenieX, polozenieY):
        print self._nazwa," zjedzone przez ",self._swiat.organizmZwrocNazwe(numerOrganizmu)
        self._swiat.UsunOrganizm(numerOrganizmu2)
        