#!/usr/bin/env python3
# -*- coding: utf-8 -*-


frame("Välkommen till Python! Denna sträng är längre, längre, läääängre.")

print("\n -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- \n")


def triangle(n):
    temp = 1
    for i in range(n):
        for j in range(temp):
            print("*", end="")
        print("")
        temp += 2


triangle(10)

print("\n -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- \n")


def square(n):
    for j in range(n * 10):
        for i in range(n * 10):
            print("*", end="")
        print(" ", end="")
        for i in range(n * 10):
            print("*", end="")
        print("")


def flag(n):
    square(n)
    print("")
    square(n)


flag(1)

print("\n -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*- \n")
