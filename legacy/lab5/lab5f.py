#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def add(n, m):
    return n + m


def partial(fun, val):
    return lambda m: fun(val, m)


add_five = partial(add, 5)
