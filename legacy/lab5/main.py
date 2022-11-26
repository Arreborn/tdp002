#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from re import match
import lab5a
import lab5b
import lab5c
import lab5d
import lab5e
import lab5f
import lab5g
import lab5h
from os import system

if __name__ == "__main__":
    while True:
        system("clear")
        print("Welcome to lab 5 - the main program (patent pending)")
        print("1. Lab 5a")
        print("2. Lab 5b")
        print("3. Lab 5c")
        print("4. Lab 5d")
        print("5. Lab 5e")
        print("6. Lab 5f")
        print("7. Lab 5g")
        print("8. Lab 5h")
        command = input("Please select a module to run (1-8 or a-h, 0 to exit): ")

        system("clear")

        if command == "1" or command == "a":
            print("Original lab 1:\n")
            lab5a.og()
            print("-----------")
            print("Revised lab 1:\n")
            print("Addition: " + str(lab5a.iterate(512, lambda x, y: x + y)))
            print("Multiplikation: " + str(lab5a.iterate(512, lambda x, y: x * y)))
            input("\nPress enter to return to the main menu.")
        elif command == "2" or command == "b":
            print("Searching for 'position' and 'examiner':\n")
            lab5b.dbsearch(lab5b.db, "position", "examiner")
            input("\nPress enter to return to the main menu.")
        elif command == "3" or command == "c":
            lab5c.run_me()
        elif command == "4" or command == "d":
            lab5d.run_me()
        elif command == "5" or command == "e":
            lab5e.run_me()
        elif command == "6" or command == "f":
            usr_input = int(input("Enter a number to run the function with: "))
            add_usr_input = lab5f.partial(lab5f.add, usr_input)
            usr_input = int(input("Enter another number to use with the functions: "))
            print(add_usr_input(usr_input))
            input("\nPress enter to return to the main menu.")
        elif command == "7" or command == "g":
            usr_input = int(input("Enter a number: "))
            compose = lab5g.compose(lab5g.add_ten, lab5g.multiply_five)
            print(compose(usr_input))
            another_composition = lab5g.compose(lab5g.multiply_five, lab5g.add_ten)
            print(another_composition(usr_input))
            input("\nPress enter to return to the main menu.")
        elif command == "8" or command == "h":
            usr_input = int(input("Enter a number: "))
            lab5h.process(range(usr_input))
            input("\nPress enter to return to the main menu.")
        elif command == "0":
            break
        else:
            command = input(
                "\nIncorrect input! Please select a valid module (1-8 or a-h): "
            )
