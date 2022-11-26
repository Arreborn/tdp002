#!/usr/bin/env python3
#-*- coding: utf-8 -*-
def moduleCheck():
    """Checks if module.py is running as a module or program"""
    if __name__ == '__main__':
        print("Running as a program")
    else:
        print("Running as a module")

# Adds 5 to the supplied int
def add5(x):
    """Adds 5 to the supplied number"""
    return x + 5

# __name__ fetches the current project file
# __main__ checks if the file is running as a module
# If this file is run as a module, __main__ will designate the file it is imported to
if __name__ == '__main__':
    moduleCheck()

