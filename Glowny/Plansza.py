import pygame
from Glowny.Swiat import Swiat          
from pygame.locals import *  
from sys import exit

SIZE = 20
OR_SIZE = 20

screen_size = (SIZE*OR_SIZE,(SIZE*OR_SIZE)+100)
 
class Wirtualny__swiat():
    def __init__(self):
        pygame.init()
        flag = DOUBLEBUF
        self.__surface = pygame.display.set_mode(screen_size,flag)
        self.__gamestate = 1 
        self.__wilk = pygame.image.load('wilk.jpg')
        self.__owca = pygame.image.load('owca.jpg')
        self.__lis = pygame.image.load('lis.png')
        self.__zolw = pygame.image.load('zolw.jpg')
        self.__antylopa = pygame.image.load('antylopa.jpg')
        self.__guarana = pygame.image.load('guarana.jpg')
        self.__jagody = pygame.image.load('jagody.jpg')
        self.__trawa = pygame.image.load('trawa.jpg')
        self.__mlecz = pygame.image.load('mlecz.jpg')
        self.__czlowiek = pygame.image.load('czlowiek.jpg')
        self.__tura = pygame.image.load('tura.jpg')
        self.__wczytaj = pygame.image.load('wczytaj.jpg')
        self.__zapisz = pygame.image.load('zapisz.jpg')
        self.__wybor = pygame.image.load('wybor.jpg')
        self.loop()
        
    def game_exit(self):
        exit()
    
    def rysujZwierze(self,znak,i,j):
        if znak == 'W':
            self.__surface.blit(self.__wilk, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'O':
            self.__surface.blit(self.__owca, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'L':
            self.__surface.blit(self.__lis, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'Z':
            self.__surface.blit(self.__zolw, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'A':
            self.__surface.blit(self.__antylopa, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'G':
            self.__surface.blit(self.__guarana, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'T':
            self.__surface.blit(self.__trawa, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'J':
            self.__surface.blit(self.__jagody, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'M':
            self.__surface.blit(self.__mlecz, (i*OR_SIZE,j*OR_SIZE))
        elif znak == 'C':
            self.__surface.blit(self.__czlowiek, (i*OR_SIZE,j*OR_SIZE))
    
    def wczytajMape(self,__swiat):
        self.__surface.fill((255,255,255))
        self.__surface.blit(self.__tura, (0,SIZE*OR_SIZE+5))
        self.__surface.blit(self.__wczytaj, (140,SIZE*OR_SIZE+5))
        self.__surface.blit(self.__zapisz, (280,SIZE*OR_SIZE+5))
        self.__surface.blit(self.__wybor, (100,SIZE*OR_SIZE+50))
        self.__surface.blit(self.__trawa, (100,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__mlecz, (120,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__guarana, (140,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__jagody, (160,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__czlowiek, (180,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__wilk, (200,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__owca, (220,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__zolw, (240,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__lis, (260,SIZE*OR_SIZE+75))
        self.__surface.blit(self.__antylopa, (280,SIZE*OR_SIZE+75))
        for i in range(SIZE):
            for j in  range(SIZE):
                if __swiat.ZwrocMape(i,j)>='A' and __swiat.ZwrocMape(i,j)<='Z':
                    self.rysujZwierze(__swiat.ZwrocMape(i,j), i, j)
 
    def loop(self):
        __swiat = Swiat()
        __organizm = 'B'
        self.__surface.fill((255,255,255))
        __przycisk1 = self.__surface.blit(self.__tura, (0,SIZE*OR_SIZE+5))
        __przycisk2 = self.__surface.blit(self.__wczytaj, (140,SIZE*OR_SIZE+5))
        __przycisk3 = self.__surface.blit(self.__zapisz, (280,SIZE*OR_SIZE+5))
        __przyciskT = self.__surface.blit(self.__trawa, (100,SIZE*OR_SIZE+75))
        __przyciskM = self.__surface.blit(self.__mlecz, (120,SIZE*OR_SIZE+75))
        __przyciskG = self.__surface.blit(self.__guarana, (140,SIZE*OR_SIZE+75))
        __przyciskJ = self.__surface.blit(self.__jagody, (160,SIZE*OR_SIZE+75))
        __przyciskC = self.__surface.blit(self.__czlowiek, (180,SIZE*OR_SIZE+75))
        __przyciskW = self.__surface.blit(self.__wilk, (200,SIZE*OR_SIZE+75))
        __przyciskO = self.__surface.blit(self.__owca, (220,SIZE*OR_SIZE+75))
        __przyciskZ = self.__surface.blit(self.__zolw, (240,SIZE*OR_SIZE+75))
        __przyciskL = self.__surface.blit(self.__lis, (260,SIZE*OR_SIZE+75))
        __przyciskA = self.__surface.blit(self.__antylopa, (280,SIZE*OR_SIZE+75))
        self.wczytajMape(__swiat)
        pygame.display.flip()
        while self.__gamestate == 1:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.__gamestate = 0
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    klikX,klikY = event.pos
                    if klikX>=0 and klikX<SIZE*OR_SIZE and klikY>=0 and klikY<SIZE*OR_SIZE:
                        __x = (klikX-(klikX%OR_SIZE))/OR_SIZE
                        __y = (klikY-(klikY%OR_SIZE))/OR_SIZE
                        if __swiat.DodajOrganizmKliknieciem(__organizm,__x,__y,__swiat) == 0:
                            self.rysujZwierze(__organizm, __x, __y)
                    if __przycisk1.collidepoint(event.pos):
                        __swiat.WykonajTure()
                        self.wczytajMape(__swiat)
                    elif __przycisk2.collidepoint(event.pos):
                        __swiat.WczytajStan(__swiat)
                        self.wczytajMape(__swiat)
                    elif __przycisk3.collidepoint(event.pos):
                        __swiat.ZapiszStan()
                    elif __przyciskT.collidepoint(event.pos):
                        print "Wybrales Trawe"
                        __organizm = 'T'
                    elif __przyciskM.collidepoint(event.pos):
                        print "Wybrales Mlecz"
                        __organizm = 'M'
                    elif __przyciskG.collidepoint(event.pos):
                        print "Wybrales Guarane"
                        __organizm = 'G'
                    elif __przyciskJ.collidepoint(event.pos):
                        print "Wybrales Wilcze jagody"
                        __organizm = 'J'
                    elif __przyciskC.collidepoint(event.pos):
                        print "Wybrales Czlowieka"
                        __organizm = 'C'
                    elif __przyciskW.collidepoint(event.pos):
                        print "Wybrales Wilka"
                        __organizm = 'W'
                    elif __przyciskO.collidepoint(event.pos):
                        print "Wybrales Owce"
                        __organizm = 'O'
                    elif __przyciskZ.collidepoint(event.pos):
                        print "Wybrales Zlowia"
                        __organizm = 'Z'
                    elif __przyciskL.collidepoint(event.pos):
                        print "Wybrales Lisa"
                        __organizm = 'L'
                    elif __przyciskA.collidepoint(event.pos):
                        print "Wybrales Antylope"
                        __organizm = 'A'
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        __swiat.czlowiekZmienKierunek(3)
                        print "Czlowiek planuje isc w lewo"
                    elif event.key == K_RIGHT:
                        __swiat.czlowiekZmienKierunek(4)
                        print "Czlowiek planuje isc w prawo"
                    elif event.key == K_UP:
                        __swiat.czlowiekZmienKierunek(1)
                        print "Czlowiek planuje isc w gore"
                    elif event.key == K_DOWN:
                        __swiat.czlowiekZmienKierunek(2)
                        print "Czlowiek planuje isc w dol"
                    elif event.key == K_SPACE:
                        __swiat.czlowiekUzyjMiksture()
                pygame.display.flip()                          
        self.game_exit()
  
if __name__ == '__main__':
    Wirtualny__swiat()
        