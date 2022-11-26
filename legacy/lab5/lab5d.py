#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from termcolor import colored
from re import match


def pwd():
    print(os.getcwd() + "/")


def ls():
    ls_cwd = os.listdir(os.getcwd())
    for i in ls_cwd:
        print(i, end="   ")
    print("")


def cd(path="/home/arreborn/"):
    os.chdir(path)


def cat(path):
    with open(path) as f:
        printable = f.read()
        print(printable)


def clear():
    os.system("clear")


def run_me():
    print("Use the command 'exit' to return to the main menu.")
    while True:
        command = input(colored("command > ", "blue"))

        if command == "ls":
            ls()
        elif match("^cd", command):
            if command == "cd":
                cd()
            else:
                command_spliced = command[3:]
                try:
                    cd(command_spliced)
                except:
                    print(colored("Error: ", "red") + "Not a valid directory")
        elif command == "pwd":
            pwd()
        elif command == "exit":
            break
        elif match("^cat", command):
            command_spliced = command[4:]
            try:
                cat(command_spliced)
            except:
                print(colored("Error: ", "red") + "Not a valid file")
        elif command == "clear":
            clear()
