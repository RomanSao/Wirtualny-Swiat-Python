from Rosliny.Roslina import Roslina

class WilczeJagody(Roslina):
    def __init__(self,x,y,sila,inicjatywa,swiat):
        Roslina.__init__(self,0,0,x,y,'J',swiat,"Wilcze Jagody")
        
    def Kolizja(self, numerOrganizmu, numerOrganizmu2, polozenieX, polozenieY):
        print self._nazwa," zjedzone przez ",self._swiat.organizmZwrocNazwe(numerOrganizmu)
        print self._nazwa," zabijaja ",self._swiat.organizmZwrocNazwe(numerOrganizmu)
        self._swiat.UsunOrganizm(numerOrganizmu)
        if numerOrganizmu<numerOrganizmu2:
            numerOrganizmu2 = numerOrganizmu2 - 1
            self._swiat.UsunOrganizm(numerOrganizmu2);
        else:        
            self._swiat.UsunOrganizm(numerOrganizmu2)
