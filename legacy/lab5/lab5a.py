#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# OG lab 1a / b


def og():

    # loops through all numbers between 1 - 512, and adds all numbers together
    output = 1

    for i in range(2, 513):
        output += i

    print("Addition: " + str(output))

    # loops through all numbers between 1 - 512, and multiplies all numbers together

    output = 1

    for i in range(2, 513):
        output = output * i

    print("Multiplikation: " + str(output))


# --------------------

# Remake with lambda - lab 5a


def iterate(x, fun):
    result = 1
    for i in range(2, (x + 1)):
        result = fun(result, i)
    return result
