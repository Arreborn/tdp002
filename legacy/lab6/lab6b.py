people = [
    {"name": "Adam", "age": 16},
    {"name": "Beatrice", "age": 59},
    {"name": "Cassidy", "age": 27},
    {"name": "David", "age": 32},
    {"name": "Elin", "age": 28},
    {"name": "Fred", "age": 12},
    {"name": "Gunnar", "age": 40},
    {"name": "Henry", "age": 61},
    {"name": "Ida", "age": 20},
    {"name": "Julia", "age": 41},
    {"name": "Kate", "age": 39},
    {"name": "Love", "age": 29},
    {"name": "Mike", "age": 33},
    {"name": "Nancy", "age": 24},
    {"name": "Oliver", "age": 10},
    {"name": "Pontus", "age": 30},
    {"name": "Quentin", "age": 23},
    {"name": "Ruben", "age": 37},
    {"name": "Sara", "age": 20},
    {"name": "Tom", "age": 49},
    {"name": "Ulf", "age": 72},
    {"name": "Viktor", "age": 26},
    {"name": "Walter", "age": 49},
    {"name": "Xavier", "age": 19},
    {"name": "Ylva", "age": 67},
    {"name": "Zarah", "age": 21},
]


def binary_search(database, search, key):
    low = 0
    high = len(database)

    while True:

        if high < low:
            print(search + " does not exist")

        middle = low + (high - low) // 2

        if key(database[middle])[0] < search[0]:
            low = middle + 1

        elif key(database[middle])[0] > search[0]:
            high = middle - 1

        else:
            print(database[middle])
            break


binary_search(people, "Zarah", lambda k: k["name"])
