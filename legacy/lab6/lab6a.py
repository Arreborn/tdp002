imdb = [
    {"title": "The Rock", "actress": "Nicholas Cage", "score": 11},
    {"title": "Raise your voice", "actress": "Hilary Duff", "score": 10},
    {"title": "Black Hawk Down", "actress": "Eric Bana", "score": 12},
    {"title": "National Treasure", "actress": "Nicholas Cage", "score": 20},
    {"title": "The Men Who Stare At Goats", "actress": "Ewan McGregor", "score": 9000},
]


def linear_search(database, search, key):
    for item in database:
        if search == key(item):
            print(item)


linear_search(imdb, "Nicholas Cage", lambda k: k["actress"])
