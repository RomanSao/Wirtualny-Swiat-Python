import random
from Zwierzeta.Zwierze import Zwierze

class Lis(Zwierze):
    def __init__(self,x,y,sila,inicjatywa,swiat):
        Zwierze.__init__(self,sila,inicjatywa,x,y,'L',swiat,"Lis")
        
    def WczytajOrganizm(self,x,y,sila,inicjatywa,swiat):
        Zwierze(sila,inicjatywa,x,y,'L',swiat,"Lis")
        
    def Akcja(self):
        __ruch = random.randint(0,7)
        __x,__y = self.LosujRuch(__ruch)
        __tmp = 0           
        while __tmp<self._swiat.ZwrocRozmiar():
            if self._swiat.organizmZwrocPolozenieX(__tmp) == __x and self._swiat.organizmZwrocPolozenieY(__tmp) == __y:
                if self._sila < self._swiat.organizmZwrocSile(__tmp):
                    print "Lis wycofuje sie"
                    return
                break
            __tmp = __tmp + 1
        self._polozenieX = __x
        self._polozenieY = __y
                
        