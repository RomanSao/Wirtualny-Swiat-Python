import random
from Glowny.Organizm import Organizm

SIZE = 20

class Zwierze(Organizm):
    
    def __init__(self,sila, inicjatywa, polozenieX, polozenieY, znak, swiat, nazwa):
        Organizm.__init__(self,sila, inicjatywa, polozenieX, polozenieY, znak, swiat, nazwa)
    
    def LosujRuch(self,los):
        __ruch = los
        
        __x = self._polozenieX
        __y = self._polozenieY
        
        if __ruch == 0:
            if __x>0:
                __x = __x - 1
            else:
                __x = __x + 1                
            pass
        
        elif __ruch == 1:
            if __x<SIZE-1:
                __x = __x + 1
            else:
                __x = __x - 1  
            pass
        
        elif __ruch == 2:
            if __y>0:
                __y = __y - 1
            else:
                __y = __y + 1  
            pass
        
        elif __ruch == 3:
            if __y<SIZE-1:
                __y = __y + 1
            else:
                __y = __y - 1  
            pass
        
        elif __ruch == 4:
            if __x>0 and __y>0:
                __y = __y - 1
                __x = __x - 1
            else:
                __y = __y + 1
                __x = __x + 1  
            pass
        
        elif __ruch == 5:
            if __x<SIZE-1 and __y>0:
                __y = __y - 1
                __x = __x + 1
            else:
                __y = __y + 1
                __x = __x - 1    
            pass
        
        elif __ruch == 6:
            if __x<SIZE-1 and __y<SIZE-1:
                __y = __y + 1
                __x = __x + 1
            else:
                __y = __y - 1
                __x = __x - 1  
            pass
        
        elif __ruch == 7:
            if __x>0 and __y<SIZE-1:
                __y = __y + 1
                __x = __x - 1
            else:
                __y = __y - 1
                __x = __x + 1  
            pass
        
        return (__x,__y)
    
    def Akcja(self):
        __ruch = random.randint(0,7)
        self._polozenieX, self._polozenieY = self.LosujRuch(__ruch)
    
    def ZnajdzBezpieczne(self):
        for __ruch in range(7):
            __x, __y = self.LosujRuch(__ruch)
            __tmp = 0
            __czyPuste = 1              
            while __tmp<self._swiat.ZwrocRozmiar():
                if self._swiat.organizmZwrocPolozenieX(__tmp) == __x and self._swiat.organizmZwrocPolozenieY(__tmp) == __y:
                    __czyPuste = 0
                    break
                __tmp = __tmp + 1                  
            if __czyPuste == 1:
                return (__x,__y)
        return (self._polozenieX,self._polozenieY)
    
    def Rozmnazaj(self):
        __x, __y = self.ZnajdzBezpieczne()
        if self._polozenieX != __x or self._polozenieY != __y:                           
            self._swiat.DodajOrganizm(__x,__y,self._sila,self._inicjatywa,self._znak,self._swiat)           
            print self._nazwa," rozmnaza sie"
        else:
            print self._nazwa," nie ma miejsca na rozmnazanie sie"
            
    def Kolizja(self,numerOrganizmu,numerOrganizmu2,polozenieX,polozenieY):
        if self._znak == self._swiat.organizmZwrocZnak(numerOrganizmu):
            self._swiat.organizmZmienPolozenieX(numerOrganizmu,polozenieX)
            self._swiat.organizmZmienPolozenieY(numerOrganizmu,polozenieY)
            self.Rozmnazaj()
        elif self._sila>self._swiat.organizmZwrocSile(numerOrganizmu):
            print self._nazwa," zjada ",self._swiat.organizmZwrocNazwe(numerOrganizmu)
            self._swiat.UsunOrganizm(numerOrganizmu)   
        else:
            print self._swiat.organizmZwrocNazwe(numerOrganizmu)," zjada ",self._nazwa
            self._swiat.UsunOrganizm(numerOrganizmu2)             