wynik = 0
proces = True
while proces:
    uzytkownik = input()
    if uzytkownik == "=":
        proces = False
    if "+" in uzytkownik:
        liczba = ""
        if uzytkownik[0] == "+":
            for i in range(1, len(uzytkownik)):
                if uzytkownik[i] != "+":
                    liczba += str(uzytkownik[i])
            wynik += int(liczba)
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

    if "-" in uzytkownik:
        liczba = ""
        if uzytkownik[0] == "-":
            for i in range(1, len(uzytkownik)):
                if uzytkownik[i] != "-":
                    liczba += str(uzytkownik[i])
            wynik -= int(liczba)
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

    if "*" in uzytkownik:
        liczba = ""
        if uzytkownik[0] == "*":
            for i in range(1, len(uzytkownik)):
                if uzytkownik[i] != "+":
                    liczba += str(uzytkownik[i])
            wynik *= int(liczba)
        else:
            wynik = 1
            i = 0
            while uzytkownik[i] != "*":
                liczba += str(uzytkownik[i])
                i += 1
            pierwsza = int(liczba)
            i += 1
            liczba = ""
            while i < len(uzytkownik):
                liczba += str(uzytkownik[i])
                i += 1
            wynik = round(pierwsza*int(liczba))

    if "/" in uzytkownik:
        liczba = ""
        if uzytkownik[0] == "/":
            for i in range(1, len(uzytkownik)):
                if uzytkownik[i] != "+":
                    liczba += str(uzytkownik[i])
            wynik = wynik/int(liczba)
        else:
            wynik = 1
            i = 0
            while uzytkownik[i] != "/":
                liczba += str(uzytkownik[i])
                i += 1
            pierwsza = int(liczba)
            i += 1
            liczba = ""
            while i < len(uzytkownik):
                liczba += str(uzytkownik[i])
                i += 1
            wynik = round(pierwsza/int(liczba))
    print(wynik)
