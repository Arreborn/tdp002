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


def insertion(db, fun=None):

    if fun == None:
        for i in range(1, len(db)):
            key = db[i]
            j = i - 1

            while j >= 0 and db[j] > key:
                db[j + 1] = db[j]
                j -= 1

            db[j + 1] = key

    else:
        for i in range(1, len(db)):
            key = db[i]
            j = i - 1

            while j >= 0 and fun(db[j]) > fun(key):
                db[j + 1] = db[j]
                j -= 1

            db[j + 1] = key

    return db


print(insertion(db))
print(insertion(db, lambda k: k[1]))
print(insertion(db, lambda k: k[0]))
