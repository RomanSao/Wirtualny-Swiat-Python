import linecache
from Zwierzeta.Wilk import Wilk
from Zwierzeta.Owca import Owca
from Zwierzeta.Zolw import Zolw
from Zwierzeta.Lis import Lis
from Zwierzeta.Antylopa import Antylopa
from Zwierzeta.Czlowiek import Czlowiek
from Rosliny.Trawa import Trawa
from Rosliny.WilczeJagody import WilczeJagody
from Rosliny.Guarana import Guarana
from Rosliny.Mlecz import Mlecz
from Wyjatek import WyjatekCzlowieka
SIZE = 20
ORG_SIZE = 20
LIMIT = 100

class Swiat:
    def __init__(self):
        self.__organizmy = [None] * 400
        self.__mapa = [[None]*SIZE for i in range(SIZE)]
        self.__iloscOrganizmow = 0
        self.__czlowiek = None
        self.__licznikTur = 0
        self.DodajOrganizmBazowy(10,10,'W',self)
        self.DodajOrganizmBazowy(10,14,'O',self)
        self.DodajOrganizmBazowy(12,18,'L',self)    
        self.DodajOrganizmBazowy(2,12,'Z',self)
        self.DodajOrganizmBazowy(7,5,'A',self)
        self.DodajOrganizmBazowy(11,10,'W',self)
        self.DodajOrganizmBazowy(10,13,'O',self)
        self.DodajOrganizmBazowy(11,18,'L',self)    
        self.DodajOrganizmBazowy(3,12,'Z',self)
        self.DodajOrganizmBazowy(15,14,'A',self)
        self.DodajOrganizmBazowy(10,8,'G',self)
        self.DodajOrganizmBazowy(14,4,'T',self)
        self.DodajOrganizmBazowy(5,2,'J',self)
        self.DodajOrganizmBazowy(15,13,'M',self)
        self.DodajOrganizmBazowy(1,4,'A',self)
        self.DodajOrganizmBazowy(1,5,'W',self)
        self.DodajOrganizmBazowy(1,1,'O',self)
        self.DodajOrganizmBazowy(1,2,'O',self)
        self.DodajOrganizmBazowy(2,1,'O',self)
        self.DodajOrganizmBazowy(10,10,'C',self)
        
    def ZwrocMape(self,y,x):
        return self.__mapa[y][x]
    
    def ZwrocRozmiar(self):
        return self.__iloscOrganizmow   
     
    def organizmZwrocZnak(self, numerOrganizmu):
        return self.__organizmy[numerOrganizmu].ZwrocZnak()
    
    def organizmZwrocSile(self, numerOrganizmu):
        return self.__organizmy[numerOrganizmu].ZwrocSile()
    
    def organizmZwrocNazwe(self, numerOrganizmu):
        return self.__organizmy[numerOrganizmu].ZwrocNazwe()
    
    def organizmZwrocPolozenieX(self,numerOrganizmu):
        return self.__organizmy[numerOrganizmu].ZwrocPolozenieX()
     
    def organizmZwrocPolozenieY(self,numerOrganizmu):
        return self.__organizmy[numerOrganizmu].ZwrocPolozenieY()
    
    def organizmZmienPolozenieX(self,numerOrganizmu,polozenieX):
        self.__organizmy[numerOrganizmu].ZmienPolozenieX(polozenieX)
        
    def organizmZmienPolozenieY(self,numerOrganizmu,polozenieY):
        self.__organizmy[numerOrganizmu].ZmienPolozenieY(polozenieY)
    
    def organizmZmienSile(self,numerOrganizmu,sila):
        self.__organizmy[numerOrganizmu].ZmienSile(sila) 
            
    def czlowiekZmienKierunek(self,kierunek):
        self.__czlowiek.ZmienKierunek(kierunek)
            
    def czlowiekUzyjMiksture(self):
        self.__czlowiek.UzyjMiksturyPanoramiksa()
            
    def WykonajTure(self):
        self.__licznikTur = self.__licznikTur + 1
        print "Tura nr ", self.__licznikTur
        
        for x in range(SIZE):
            for y in range(SIZE):
                self.__mapa[y][x] = ' '
                   
        for i in range(10):
            for j in range(self.__iloscOrganizmow):
                if j<self.__iloscOrganizmow:
                    if self.__organizmy[j].ZwrocInicjatywe() == i:
                        polozenieX =  self.__organizmy[j].ZwrocPolozenieX()
                        polozenieY = self.__organizmy[j].ZwrocPolozenieY()
                        self.__organizmy[j].Akcja()
                        z = 0
                        while(z<self.__iloscOrganizmow):
                            if z != j:
                                if self.__organizmy[j].ZwrocPolozenieX() == self.__organizmy[z].ZwrocPolozenieX() and self.__organizmy[j].ZwrocPolozenieY() == self.__organizmy[z].ZwrocPolozenieY():
                                    self.__organizmy[z].Kolizja(j,z,polozenieX,polozenieY)
                                    #print self.__iloscOrganizmow
                                    break
                            z = z + 1
                                
        self.RysujSwiat()
        
    
    def RysujSwiat(self):
        for i in range(self.__iloscOrganizmow):
            self.__organizmy[i].Rysowanie(self.__mapa) 
      
    def DodajOrganizm(self, polozenieX, polozenieY, sila, inicjatywa, znak, swiat):
        if znak == 'W':
            wilk = Wilk(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = wilk
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass 
        elif znak == 'O':
            owca = Owca(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = owca
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass           
        elif znak == 'L':
            lis = Lis(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = lis
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass        
        elif znak == 'Z':
            zolw = Zolw(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = zolw
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass          
        elif znak == 'A':
            antylopa = Antylopa(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = antylopa
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass       
        elif znak == 'G':
            guarana = Guarana(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = guarana
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass          
        elif znak == 'T':
            trawa = Trawa(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = trawa
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass           
        elif znak == 'J':
            jagody = WilczeJagody(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = jagody
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass
        elif znak == 'M':
            mlecz = Mlecz(polozenieX,polozenieY,sila,inicjatywa,swiat)
            self.__organizmy[self.__iloscOrganizmow] = mlecz
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass
        elif znak == 'C':
            try:
                if self.__czlowiek != None:
                    raise WyjatekCzlowieka
                self.DodajCzlowieka(polozenieX,polozenieY,5,4,swiat)
            except WyjatekCzlowieka:
                print "Mozliwy tyllko 1 Czlowiek na mapie"
                return
        
    def DodajOrganizmBazowy(self, polozenieX, polozenieY, znak, swiat):
        if znak == 'W':
            wilk = Wilk(polozenieX,polozenieY,9,5,swiat)
            self.__organizmy[self.__iloscOrganizmow] = wilk
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass 
        elif znak == 'O':
            owca = Owca(polozenieX,polozenieY,4,4,swiat)
            self.__organizmy[self.__iloscOrganizmow] = owca
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass           
        elif znak == 'L':
            lis = Lis(polozenieX,polozenieY,3,7,swiat)
            self.__organizmy[self.__iloscOrganizmow] = lis
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass        
        elif znak == 'Z':
            zolw = Zolw(polozenieX,polozenieY,2,1,swiat)
            self.__organizmy[self.__iloscOrganizmow] = zolw
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass          
        elif znak == 'A':
            antylopa = Antylopa(polozenieX,polozenieY,4,4,swiat)
            self.__organizmy[self.__iloscOrganizmow] = antylopa
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass       
        elif znak == 'G':
            guarana = Guarana(polozenieX,polozenieY,0,0,swiat)
            self.__organizmy[self.__iloscOrganizmow] = guarana
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass          
        elif znak == 'T':
            trawa = Trawa(polozenieX,polozenieY,0,0,swiat)
            self.__organizmy[self.__iloscOrganizmow] = trawa
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass           
        elif znak == 'J':
            jagody = WilczeJagody(polozenieX,polozenieY,99,0,swiat)
            self.__organizmy[self.__iloscOrganizmow] = jagody
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass
        elif znak == 'M':
            mlecz = Mlecz(polozenieX,polozenieY,0,0,swiat)
            self.__organizmy[self.__iloscOrganizmow] = mlecz
            self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
            self.__iloscOrganizmow = self.__iloscOrganizmow + 1
            pass
        elif znak == 'C':
            try:
                if self.__czlowiek != None:
                    raise WyjatekCzlowieka
                self.DodajCzlowieka(polozenieX,polozenieY,5,4,swiat)
            except WyjatekCzlowieka:
                print "Mozliwy tyllko 1 Czlowiek na mapie"
                return
        
    def DodajCzlowieka(self, polozenieX, polozenieY, sila, inicjatywa, swiat,  cooldown = 0):
        czlowiek = Czlowiek(polozenieX,polozenieY,sila,inicjatywa,cooldown,swiat)
        self.__organizmy[self.__iloscOrganizmow] = czlowiek
        self.__organizmy[self.__iloscOrganizmow].Rysowanie(self.__mapa)
        self.__iloscOrganizmow = self.__iloscOrganizmow + 1
        self.__czlowiek = czlowiek
        
    def DodajOrganizmKliknieciem(self, znak, __x, __y, swiat):
        try:
            if znak == 'C':
                if self.__czlowiek != None:
                    raise WyjatekCzlowieka
        except WyjatekCzlowieka:
            print "Mozliwy tyllko 1 Czlowiek na mapie"
            return -1
        #print __x,__y
        __wolne=1
        for i in range(self.__iloscOrganizmow):
            if self.__organizmy[i].ZwrocPolozenieX() == __x and self.__organizmy[i].ZwrocPolozenieY() == __y:
                __wolne = 0
                break
        if __wolne == 0:
            print "Miejsce zajete przez",self.__organizmy[i].ZwrocNazwe()
            return -1
        elif znak != 'B':
            self.DodajOrganizmBazowy(__y, __x, znak, swiat)
            return 0
        else:
            print "Nie wybrano organizmu"
            return -1
        
    def ZapiszStan(self):
        plik = open('plik.txt','w')
        for i in range(self.__iloscOrganizmow):
            plik.write("%d" % (self.__organizmy[i].ZwrocPolozenieX()))
            plik.write(' ')
            plik.write("%d" % (self.__organizmy[i].ZwrocPolozenieY()))
            plik.write(' ')
            plik.write("%d" % (self.__organizmy[i].ZwrocSile()))
            plik.write(' ')
            plik.write("%d" % (self.__organizmy[i].ZwrocInicjatywe()))
            plik.write(' ')
            plik.write("%c" % (self.__organizmy[i].ZwrocZnak()))
            plik.write(' ') 
            if self.__organizmy[i].ZwrocZnak() == 'C':
                plik.write("%d" % (self.__czlowiek.ZwrocCooldown()))
                plik.write(' ')
            
    def WczytajStan(self,swiat):
        for i in range(self.__iloscOrganizmow):
            self.UsunOrganizm(i)
            
        for x in range(SIZE):
            for y in range(SIZE):
                self.__mapa[y][x] = ' '
            
        plik = open('plik.txt')
        try:
            linia = linecache.getline('plik.txt',1)
            lista = linia.split()
            i = 0
            numerLinii = 1
            polozenieX = 0
            polozenieY = 0 
            sila = 0
            inicjatywa = 0
            cooldown = 0
            znak = ' '
            while i<len(lista):
                if numerLinii == 1:
                    polozenieX = int(lista[i])
                elif numerLinii == 2:
                    polozenieY = int(lista[i])
                elif numerLinii == 3:
                    sila = int(lista[i])
                elif numerLinii == 4:
                    inicjatywa = int(lista[i])
                elif numerLinii == 5:
                    znak = lista[i]
                    if znak == 'C':
                        i = i + 1
                        cooldown = int(lista[i])
                        self.DodajCzlowieka(polozenieX, polozenieY, sila, inicjatywa, swiat, cooldown)
                    else:
                        self.DodajOrganizm(polozenieX, polozenieY, sila, inicjatywa, znak, swiat)
                    numerLinii = 0
                numerLinii = numerLinii + 1       
                i = i + 1       
        finally:
            self.RysujSwiat()
            plik.close() 
                  
                      
    def UsunOrganizm(self,numerOrganizmu):
        __i = numerOrganizmu
        if self.organizmZwrocZnak(numerOrganizmu) == 'C':
            self.__czlowiek = None
        while __i+1<self.__iloscOrganizmow:
            self.__organizmy[__i] = self.__organizmy[__i + 1]
            __i = __i + 1                
        self.__iloscOrganizmow = self.__iloscOrganizmow - 1

        