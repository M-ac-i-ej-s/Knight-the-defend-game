import pygame
from sys import exit

from pygame import display


pygame.init()
screen = pygame.display.set_mode((250, 300))  # wysokość i szerokość okna gry
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Pixeltype.ttf", 50)
game_active = True
start_time = 0
score = 0
uzytkownik = "0"
color = (255, 255, 255)
wynik = 0


zero_surface = pygame.image.load("images/0.png").convert_alpha()
zero_rect = zero_surface.get_rect(midbottom=(90, 290))
jeden_surface = pygame.image.load("images/1.png").convert_alpha()
jeden_rect = jeden_surface.get_rect(midbottom=(30, 150))
dwa_surface = pygame.image.load("images/2.png").convert_alpha()
dwa_rect = dwa_surface.get_rect(midbottom=(90, 150))
trzy_surface = pygame.image.load("images/3.png").convert_alpha()
trzy_rect = trzy_surface.get_rect(midbottom=(150, 150))
cztery_surface = pygame.image.load("images/4.png").convert_alpha()
cztery_rect = cztery_surface.get_rect(midbottom=(30, 200))
piec_surface = pygame.image.load("images/5.png").convert_alpha()
piec_rect = piec_surface.get_rect(midbottom=(90, 200))
szesc_surface = pygame.image.load("images/6.png").convert_alpha()
szesc_rect = szesc_surface.get_rect(midbottom=(150, 200))
siedem_surface = pygame.image.load("images/7.png").convert_alpha()
siedem_rect = siedem_surface.get_rect(midbottom=(30, 250))
osiem_surface = pygame.image.load("images/8.png").convert_alpha()
osiem_rect = osiem_surface.get_rect(midbottom=(90, 250))
dziewiec_surface = pygame.image.load("images/9.png").convert_alpha()
dziewiec_rect = dziewiec_surface.get_rect(midbottom=(150, 250))
dodawanie_surface = pygame.image.load("images/dodawanie.png").convert_alpha()
dodawanie_rect = dodawanie_surface.get_rect(midbottom=(210, 150))
odejmowanie_surface = pygame.image.load(
    "images/odejmowanie.png").convert_alpha()
odejmowanie_rect = odejmowanie_surface.get_rect(midbottom=(210, 200))
mnozenie_surface = pygame.image.load("images/mnozenie.png").convert_alpha()
mnozenie_rect = mnozenie_surface.get_rect(midbottom=(210, 250))
dzielenie_surface = pygame.image.load("images/dzielenie.png").convert_alpha()
dzielenie_rect = dzielenie_surface.get_rect(midbottom=(210, 290))
rowna_surface = pygame.image.load("images/rowna_sie.png").convert_alpha()
rowna_rect = rowna_surface.get_rect(midbottom=(30, 290))
c_surface = pygame.image.load("images/c.png").convert_alpha()
c_rect = c_surface.get_rect(midbottom=(150, 290))
wynik_surf = test_font.render(f"{wynik}", False, (189, 189, 189))
wynik_surf = pygame.transform.scale2x(wynik_surf)
wynik_rect = wynik_surf.get_rect(center=(170, 50))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if jeden_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "1":
                    uzytkownik = "1"
                elif jeden_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "1"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dwa_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "2":
                    uzytkownik = "2"
                elif dwa_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "2"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if trzy_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "3":
                    uzytkownik = "3"
                elif trzy_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "3"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cztery_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "4":
                    uzytkownik = "4"
                elif cztery_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "4"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piec_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "5":
                    uzytkownik = "5"
                elif piec_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "5"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piec_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "6":
                    uzytkownik = "6"
                elif piec_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "6"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piec_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "7":
                    uzytkownik = "7"
                elif piec_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "7"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piec_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "8":
                    uzytkownik = "8"
                elif piec_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "8"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piec_rect.collidepoint(event.pos) and len(uzytkownik) == 1 and uzytkownik != "9":
                    uzytkownik = "9"
                elif piec_rect.collidepoint(event.pos) and len(uzytkownik) >= 1:
                    uzytkownik += "9"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dodawanie_rect.collidepoint(event.pos):
                    uzytkownik += "+"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if odejmowanie_rect.collidepoint(event.pos):
                    uzytkownik += "-"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mnozenie_rect.collidepoint(event.pos):
                    uzytkownik += "*"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dzielenie_rect.collidepoint(event.pos):
                    uzytkownik += "/"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if c_rect.collidepoint(event.pos):
                    uzytkownik = "0"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rowna_rect.collidepoint(event.pos):
                    if "+" in uzytkownik:
                        liczba = ""
                        if wynik > 0:
                            for i in range(1, len(uzytkownik)):
                                if uzytkownik[i] != "+":
                                    liczba += str(uzytkownik[i])
                            wynik += int(liczba)
                            uzytkownik = str(wynik)
                        else:
                            i = 0
                            while uzytkownik[i] != "+":
                                liczba += str(uzytkownik[i])
                                i += 1
                            wynik += int(liczba)
                            i += 1
                            liczba = ""
                            while i < len(uzytkownik):
                                liczba += str(uzytkownik[i])
                                i += 1
                            wynik += int(liczba)
                            uzytkownik = str(wynik)
                    if "-" in uzytkownik:
                        liczba = ""
                        if wynik > 0:
                            for i in range(1, len(uzytkownik)):
                                if uzytkownik[i] != "-":
                                    liczba += str(uzytkownik[i])
                            wynik -= int(liczba)
                            uzytkownik = str(wynik)
                        else:
                            i = 0
                            while uzytkownik[i] != "-":
                                liczba += str(uzytkownik[i])
                                i += 1
                            wynik -= int(liczba)
                            i += 1
                            liczba = ""
                            while i < len(uzytkownik):
                                liczba += str(uzytkownik[i])
                                i += 1
                            wynik -= int(liczba)
                            uzytkownik = str(wynik)
                    if "*" in uzytkownik:
                        wynik = 1
                        liczba = ""
                        if wynik > 1:
                            for i in range(1, len(uzytkownik)):
                                if uzytkownik[i] != "*":
                                    liczba += str(uzytkownik[i])
                            wynik *= int(liczba)
                            uzytkownik = str(wynik)
                        else:
                            i = 0
                            while uzytkownik[i] != "*":
                                liczba += str(uzytkownik[i])
                                i += 1
                            wynik *= int(liczba)
                            i += 1
                            liczba = ""
                            while i < len(uzytkownik):
                                liczba += str(uzytkownik[i])
                                i += 1
                            wynik *= int(liczba)
                            uzytkownik = str(wynik)
                    if "/" in uzytkownik:
                        liczba = ""
                        if wynik > 0:
                            for i in range(1, len(uzytkownik)):
                                if uzytkownik[i] != "/":
                                    liczba += str(uzytkownik[i])
                            wynik = round(wynik/int(liczba))
                            uzytkownik = str(wynik)
                        else:
                            i = 0
                            while uzytkownik[i] != "/":
                                liczba += str(uzytkownik[i])
                                i += 1
                            wynik = round(wynik/int(liczba))
                            i += 1
                            liczba = ""
                            while i < len(uzytkownik):
                                liczba += str(uzytkownik[i])
                                i += 1
                            wynik = round(wynik/int(liczba))
                            uzytkownik = str(wynik)

    screen.fill(color)
    if game_active:
        screen.blit(zero_surface, zero_rect)
        screen.blit(jeden_surface, jeden_rect)
        screen.blit(dwa_surface, dwa_rect)
        screen.blit(trzy_surface, trzy_rect)
        screen.blit(cztery_surface, cztery_rect)
        screen.blit(piec_surface, piec_rect)
        screen.blit(szesc_surface, szesc_rect)
        screen.blit(siedem_surface, siedem_rect)
        screen.blit(osiem_surface, osiem_rect)
        screen.blit(dziewiec_surface, dziewiec_rect)
        screen.blit(dodawanie_surface, dodawanie_rect)
        screen.blit(odejmowanie_surface, odejmowanie_rect)
        screen.blit(mnozenie_surface, mnozenie_rect)
        screen.blit(dzielenie_surface, dzielenie_rect)
        screen.blit(c_surface, c_rect)
        screen.blit(rowna_surface, rowna_rect)

        screen.blit(wynik_surf, wynik_rect)
        wynik_surf = test_font.render(f"{uzytkownik}", False, (189, 189, 189))
        wynik_surf = pygame.transform.scale2x(wynik_surf)

    pygame.display.update()
    clock.tick(60)
