#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


def stars(i):
    return "*" * i


def mirror(i):
    return i


def generate_list(fun, x):
    return_list = []

    for i in range(1, (x + 1)):
        return_list.append(fun(i))

    return return_list


def run_me():

    while True:

        number = input("Enter a number: ")
        while re.match("^[0-9]+$", number) is None:
            number = input("Incorrect input! Enter a number: ")

        selection = input("Enter 1 to print numbers, 2 to print stars: ")
        while re.match("^[1,2]$", selection) is None:
            selection = input("Incorrect input! Only select 1 or 2: ")

        selection = int(selection)

        if selection == 1:
            print(generate_list(mirror, int(number)))
        elif selection == 2:
            print(generate_list(stars, int(number)))

        if input("Run again? (Y / N): ").upper() != "Y":
            break
