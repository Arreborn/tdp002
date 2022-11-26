#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def run_me():

    haystack = "Can you find the needle in this haystack?".split()
    print(haystack)

    def contains(key, haystack):
        temp = list(filter(lambda x: (x == key), haystack))
        if temp == []:
            return False
        else:
            return True

    while True:

        search_key = input("Enter the word you want to search for in the haystack: ")

        print(contains(search_key, haystack))

        if input("Run again? (Y / N): ").upper() != "Y":
            break


# print(contains("find", haystack)) # True

# print(contains("in", haystack)) # True

# print(contains("needle", haystack)) # True

# print(contains("haystack", haystack)) # False

# print(contains("apple", haystack)) # False
