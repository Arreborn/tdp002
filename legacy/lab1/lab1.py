#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OG lab 1a / b

# loops through all numbers between 1 - 512, and adds all numbers together

# output = 1

# for i in range(1, 513):
#     output += i

# print("Addition: " + str(output))

# loops through all numbers between 1 - 512, and multiplies all numbers together

# output = 1

# for i in range(1, 513):
#     output = output * i

# print("Multiplikation: " + str(output))

# --------------------

# Remake with lambda - lab 5a


# def iterate(x, fun):
#     result = 1
#     for i in range(1, (x + 1)):
#         result = fun(result, i)
#     return result


# print("Addition: " + str(iterate(512, lambda x, y: x + y)))

# print("Multiplikation: " + str(iterate(512, lambda x, y: x * y)))

# --------------------

db = [
    {"name": "Jakob", "position": "assistant"},
    {"name": "Åke", "position": "assistant"},
    {"name": "Ola", "position": "examiner"},
    {"name": "Henrik", "position": "assistant"},
]


def dbsearch(db, value, result):
    return list(filter(lambda k: (k[value] == result), db))


print(dbsearch(db, "position", "examiner"))

# --------------------

haystack = "Can you find the needle in this haystack?".split()


def contains(key, haystack):
    temp = list(filter(lambda x: (x == key), haystack))
    if temp == []:
        return False
    else:
        return True


print(contains("find", haystack))

print(contains("in", haystack))

print(contains("needle", haystack))

print(contains("haystack", haystack))

print(contains("apple", haystack))
