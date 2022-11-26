#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def compose(fun1, fun2):
    return lambda x: fun1(fun2(x))


def multiply_five(n):
    return n * 5


def add_ten(x):
    return x + 10
