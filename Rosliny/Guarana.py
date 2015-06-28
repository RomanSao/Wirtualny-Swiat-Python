from Rosliny.Roslina import Roslina

class Guarana(Roslina):
    def __init__(self,x,y,sila,inicjatywa,swiat):
        Roslina.__init__(self,0,0,x,y,'G',swiat,"Guarana")
        
    def Kolizja(self,numerOrganizmu,numerOrganizmu2,polozenieX,polozenieY):
        self._swiat.organizmZmienSile(numerOrganizmu, 3);      
        print self._nazwa," zjedzone przez ",self._swiat.organizmZwrocNazwe(numerOrganizmu)
        print self._swiat.organizmZwrocNazwe(numerOrganizmu)," zyskuje +3 do sily "
        self._swiat.UsunOrganizm(numerOrganizmu2)

        