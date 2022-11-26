#!/usr/bin/env python3
# -*- coding: utf-8 -*-

db = [
    {"name": "Jakob", "position": "assistant"},
    {"name": "Åke", "position": "assistant"},
    {"name": "Ola", "position": "examiner"},
    {"name": "Henrik", "position": "assistant"},
]


def dbsearch(db, value, result):
    return_value = filter(lambda k: (k[value] == result), db)
    return_list = []
    for i in return_value:
        return_value = i
        new_order = {}
        new_order["position"] = return_value["position"]
        new_order["name"] = return_value["name"]
        return_list.append(new_order)
    return print(return_list)
