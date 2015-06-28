from abc import ABCMeta

SIZE = 20

class Organizm:
    
    __metaclass__ = ABCMeta
    
    def Akcja(self):
        pass
    
    def Kolizja(self,numerOrganizmu,numerOrganizmu2,polozenieX,polozenieY):
        pass
    
    def __init__(self, sila, inicjatywa, polozenieX, polozenieY, znak, swiat, nazwa):
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._polozenieX = polozenieX
        self._polozenieY = polozenieY
        self._znak = znak
        self._swiat = swiat
        self._nazwa = nazwa
               
    def ZwrocInicjatywe(self):
        return self._inicjatywa
    
    def ZwrocPolozenieX(self):
        return self._polozenieX
    
    def ZwrocPolozenieY(self):
        return self._polozenieY
    
    def ZwrocZnak(self):
        return self._znak
    
    def ZwrocSile(self):
        return self._sila
    
    def ZwrocNazwe(self):
        return self._nazwa
    
    def ZmienPolozenieX(self,x):
        self._polozenieX = x
    
    def ZmienPolozenieY(self,y):
        self._polozenieY = y
        
    def ZmienSile(self,sila):
        self._sila = self._sila + sila
     
    def Rysowanie(self,mapa):
        if self._polozenieX<SIZE and self._polozenieY>=0 and self._polozenieY<SIZE and self._polozenieX>=0:
            mapa[self._polozenieY][self._polozenieX] = self._znak
            
        