# Zadanie na wtorek:
# gra w zgadywanie liczb

# tutaj daj zmienne dot. wygranej i liczby prób



# 1. brak wygranej
# 2. nieprzekroczona liczba prób

# while(drawn_number == guessed_number):
#     # pobranie danych od użytkownika
#     # musimy sprawdzić czy użytkownik zgadł
#     # a jeśli nie to napisać czy trafił za nisko, czy za wysoko
#     # pamiętaj o zwiększaniu liczby prób (+=)
#     pass
# komunikat o przegranej albo wygranej

# drawn_number(number)

import random
tries = 7
drawn_number = random.randint(1, 100)
print(drawn_number, "Print kontrolny")

print("Try to guess a number in range 1 to 100. You have 7 tries")
while tries > 0:
    
    guessed_number = int(input("Enter a number: "))

    if drawn_number == guessed_number:
        print("Winner!")
        break

    else:
        tries -= 1

        if drawn_number > guessed_number:
            print("Too low")
        else:
            print("Too high")

        print("You have", tries, "tries left\n")
    if tries == 0:
        print("Roses are red\n"
              "Violets are blue\n"
              "You are a loser\n"
              "Go back to school!")
