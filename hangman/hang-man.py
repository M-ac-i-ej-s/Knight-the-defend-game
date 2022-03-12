import random
print("guess a name")
print("")

# Data base (choose words for your game)
slowo = random.choice(["Jane", "Jack", "Daniel", "Jorge", "Martha"])

lista_liter = []
for i in range(len(slowo)):
    lista_liter.append(slowo[i])


lista_pustek = []
for i in range(len(slowo)):
    lista_pustek.append("_")
lives = 6
lista_uzytych_liter = []

while "_" in lista_pustek:
    print("----------------------------------")
    print("you have", lives, "lives left")
    print(" ")
    print("you used these letters: ", * lista_uzytych_liter, sep=" ")
    print(" ")
    print(*lista_pustek, sep=" ")
    print(" ")
    litera = str(input("choose a letter: "))
    print(" ")
    if litera in lista_liter:
        index = lista_liter.index(litera)
        lista_pustek[index] = litera
        lista_liter[index] = "_"
        lista_uzytych_liter.append(litera)
        if not "_" in lista_pustek:
            print(*lista_pustek, sep=" ")
            print(" ")
            print("You Won!!")
    else:
        lista_uzytych_liter.append(litera)
        print("Not that one!!!!")
        lives -= 1
        if lives == 0:
            print("you have", lives, "lives left")
            print("you lost!!")
            break
        print(" ")
        continue
