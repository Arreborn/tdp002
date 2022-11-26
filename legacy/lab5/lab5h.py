#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lab5f import partial
from lab5g import compose


def make_filter_map(filter_fun, map_fun):
    return lambda x: print(
        list(compose(partial(map, map_fun), partial(filter, filter_fun))(x))
    )


process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)

process(range(10))
