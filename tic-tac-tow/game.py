
# That was my first project, after learning python for about.. 1.5 months
# im just saying, try not to judge too harsh :D

import random
print("zagramy w kółko i krzyzyk!")
print("")
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "

print("|" + a + "|" + b + "|" + c + "|")
print("|" + d + "|" + e + "|" + f + "|")
print("|" + g + "|" + h + "|" + i + "|")
lista_ruchów_gracza = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = "x"
o = "o"
while (a and b and c and d and e and f and g and h and i) != 0:
    print(" ")
    ruch_gracza = int(input("podaj pozycje od 1 do 9: "))
    print(" ")

    if ruch_gracza == 1:
        a = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_gracza == 2:
        b = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_gracza == 3:
        c = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_gracza == 4:
        d = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_gracza == 5:
        e = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_gracza == 6:
        f = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_gracza == 7:
        g = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_gracza == 8:
        h = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_gracza == 9:
        i = x
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")

    if a == x and d == x and g == x:
        print("Wygrałeś!!")
        break
    if b == x and e == x and h == x:
        print("Wygrałeś!!")
        break
    if c == x and f == x and i == x:
        print("Wygrałeś!!")
        break
    if a == x and b == x and c == x:
        print("Wygrałeś!!")
        break
    if d == x and e == x and f == x:
        print("Wygrałeś!!")
        break
    if g == x and h == x and i == x:
        print("Wygrałeś!!")
        break
    if a == x and e == x and i == x:
        print("Wygrałeś!!")
        break
    if g == x and e == x and c == x:
        print("Wygrałeś!!")
        break

    lista_ruchów_gracza.remove(ruch_gracza)
    if lista_ruchów_gracza == []:
        print("remis")
        break
    ruch_komputera = random.choice(lista_ruchów_gracza)
    lista_ruchów_gracza.remove(ruch_komputera)

    print(" ")
    print(" ruch komputera: ")
    print(" ")

    if ruch_komputera == 1:
        a = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_komputera == 2:
        b = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_komputera == 3:
        c = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_komputera == 4:
        d = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_komputera == 5:
        e = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_komputera == 6:
        f = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_komputera == 7:
        g = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_komputera == 8:
        h = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")
    if ruch_komputera == 9:
        i = o
        print("|" + a + "|" + b + "|" + c + "|")
        print("|" + d + "|" + e + "|" + f + "|")
        print("|" + g + "|" + h + "|" + i + "|")

    if a == o and d == o and g == o:
        print("Wygrałeś!!")
        break
    if b == o and e == o and h == o:
        print("Przegrałeś!!")
        break
    if c == o and f == o and i == o:
        print("Przegrałeś!!")
        break
    if a == o and b == o and c == o:
        print("Przegrałeś!!")
        break
    if d == o and e == o and f == o:
        print("Przegrałeś!!")
        break
    if g == o and h == o and i == o:
        print("Przegrałeś")
        break
    if a == o and e == o and i == o:
        print("Przegrałeś")
        break
    if g == o and e == o and c == o:
        print("Przegrałeś")
        break

    print(" ")
