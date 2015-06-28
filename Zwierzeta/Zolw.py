import random
from Zwierzeta.Zwierze import Zwierze

class Zolw(Zwierze):
    def __init__(self,x,y,sila,inicjatywa,swiat):
        Zwierze.__init__(self,sila,inicjatywa,x,y,'Z',swiat,"Zolw")

    def Akcja(self):
        __ruch = random.randint(0,7)
        if __ruch<2:
            Zwierze.Akcja(self)
            
    def Kolizja(self,numerOrganizmu, numerOrganizmu2, polozenieX, polozenieY):
        if self._znak == self._swiat.organizmZwrocZnak(numerOrganizmu):
            self._swiat.organizmZmienPolozenieX(numerOrganizmu,polozenieX)
            self._swiat.organizmZmienPolozenieY(numerOrganizmu,polozenieY)
            self.Rozmnazaj()               
        elif self._swiat.organizmZwrocSile(numerOrganizmu)<5:
            self._swiat.organizmZmienPolozenieX(numerOrganizmu,polozenieX)
            self._swiat.organizmZmienPolozenieY(numerOrganizmu,polozenieY)
            print "Zolw odpiera atak ",self._swiat.organizmZwrocNazwe(numerOrganizmu)
        elif self._swiat.organizmZwrocSile(numerOrganizmu)>=self._sila:
            print self._swiat.organizmZwrocNazwe(numerOrganizmu2)," zjada ",self._nazwa
            self._swiat.UsunOrganizm(numerOrganizmu2)
        else:
            print self._nazwa," zjada ",self._swiat.organizmZwrocNazwe(numerOrganizmu)
            self._swiat.UsunOrganizm(numerOrganizmu)

        