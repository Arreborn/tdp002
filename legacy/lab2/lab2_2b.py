#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def create_shopping_list():
    list = ["Kurslitteratur", "Anteckningsblock", "Penna"]
    return list

# -------------------------------------------------------------------------------

def shopping_list(l):
    for i in range(len(l)):
        print(str(i + 1) + ": " + l[i])

# -------------------------------------------------------------------------------

def shopping_add(l):
    l.append(input("Vad ska läggas till i listan? "))

# -------------------------------------------------------------------------------

def shopping_remove(l):

    try:
        selector = int(input("Vilket objekt i listan vill du ta bort? (Välj mellan 1 - " + str(len(l)) + "): "))

        if selector > 0:
            l.pop(selector - 1)
        else:
            print("Felaktigt val! Detta objekt finns inte.")

    except IndexError:
        print("Felaktigt val! Detta objekt finns inte.")

    except ValueError:
        print("Felaktigt val! Du har inte angett en siffra.")

# -------------------------------------------------------------------------------

def shopping_change(l):
    print("Du kommer nu att byta ut ett objekt på listan mot ett annat.")

    try:
        selector = int(input("Vilket objekt i listan vill du byta ut? (Välj mellan 1 - " + str(len(l)) + "): "))

        if selector > 0:
            l[selector - 1] = input("Du har angett att byta ut följande objekt: {0}. Vad vill du byta ut detta mot? ".format(l[selector - 1]))
        else:
            print("Felaktigt val! Detta objekt finns inte.")

    except IndexError:
        print("Felaktigt val! Detta objekt finns inte.")

    except ValueError:
        print("Felaktigt val! Du har inte angett en siffra.")

# Runtime -----------------------------------------------------------------------

def main():
    isRunning = True
    slist = create_shopping_list()
    selectNo = ""

    print("\nVälkommen till shoppinglistan! ", end="")

    while isRunning:
        print("\nFöljande alternativ finns tillgängliga:\n")
        print("1: Skriv ut existerande lista\n2: Lägg till föremål i listan\n3: Ta bort ett föremål ut listan\n4: Ändra ett föremål i listan\n0: Avsluta")
        print("------------------")

        try:
            selectNo = int(input("\nVälj ett alternativ: "))

        except ValueError:
            print("Felaktigt val! Du har inte angett en siffra.")

        print("")
        if selectNo == 1:
            shopping_list(slist)
        elif selectNo == 2:
            shopping_add(slist)
        elif selectNo == 3:
            shopping_remove(slist)
        elif selectNo == 4:
            shopping_change(slist)
        elif selectNo == 0:
            isRunning = False
        else:
            print("Felaktigt val! Du måste välja mellan 1 - 4, eller 0 för att avsluta.")

if __name__ == '__main__':
    main()

