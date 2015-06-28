from Rosliny.Roslina import Roslina

class Mlecz(Roslina):
    def __init__(self,x,y,sila,inicjatywa,swiat):
        Roslina.__init__(self,0,0,x,y,'M',swiat,"Mlecz")
        
    def Akcja(self):
        Roslina.Akcja(self)
        Roslina.Akcja(self)
        Roslina.Akcja(self)