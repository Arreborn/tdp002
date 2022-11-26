#!/usr/bin/env python3
#-*- coding: utf-8 -*-

name = input("Vad heter du: ")
print("Hej " + name + "!")

year = str(2022 - int(input("Mata in din ålder: ")))

print("Du föddes år " + year + ".")

county = input("Vilket län föddes du i? ")

output = ""

temp = len(name) // 2

for i in range (0, temp):
    output += name[i]

temp = len(county) // 2

for i in range ((len(county) - temp), (len(county))):
    output += county[i]

print("Första halvan av ditt namn och andra halvan av ditt län är: " + output + ".")
