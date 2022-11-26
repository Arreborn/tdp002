db = [
    ("j", "g"),
    ("a", "u"),
    ("k", "l"),
    ("o", "i"),
    ("b", "s"),
    ("@", "."),
    ("p", "s"),
    ("o", "e"),
]


def quick_sort(db, fun, index=0):
    pivot = db.pop(index)

    higher = []
    lower = []

    for item in db:
        if fun(item) > fun(pivot):
            higher.append(item)
        elif fun(item) < fun(pivot):
            lower.append(item)
        else:
            if item > pivot:
                higher.append(item)
            if item < pivot:
                lower.append(item)

    lower2 = []
    higher2 = []

    if len(higher) != 0:
        higher2 = quick_sort(higher, fun, len(higher) // 2)
    if len(lower) != 0:
        lower2 = quick_sort(lower, fun, len(lower) // 2)

    return_list = []

    while len(lower2) != 0:
        return_list.append(lower2.pop(0))
    return_list.append(pivot)
    while len(higher2) != 0:
        return_list.append(higher2.pop(0))

    return return_list


print(quick_sort(db, lambda k: k[0], 4))
