from Zwierzeta.Zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self,x,y,sila,inicjatywa,swiat):
        Zwierze.__init__(self,sila,inicjatywa,x,y,'O',swiat,"Owca")
        
        