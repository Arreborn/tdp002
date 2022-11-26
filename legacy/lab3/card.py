import random

def random_seed():
    seed = random.randint(1, 10000000000000)
    return seed

def create_deck():
    deck = []
    for i in range(1, 5):
        for j in range(1, 14):
            deck.append((i, j))
    deck.append((5, 27))
    deck.append((6, 27))
    return deck

def check_card_pos(deck, index):
    return deck[index]

def get_value(deck):
    if deck[0] == 1:
        return int(deck[1])
    elif deck[0] == 2:
        return int(deck[1] + 13)
    elif deck[0] == 5 or deck[0] == 6:
        return 27

def create_solitaire_deck(seed):
    deck = create_deck()
    send_deck = []
    for card in deck:
        if card[0] == 1 or card[0] == 2:
            send_deck.append(card)
        if card[0] == 5 or card[0] == 6:
            send_deck.append(card)
    shuffle_deck(send_deck, seed)
    return send_deck

def shuffle_deck(deck, seed):
    random.seed(seed)
    random.shuffle(deck)

def move_card(deck, pos_destination, pos_origin):
    deck.insert(pos_destination, deck.pop(pos_origin))

def switch_deck(deck_to, deck_from):
    deck_to.append(deck_from.pop(0))

def find_joker(deck):
    joker = []

    for i in range(len(deck)):
        if deck[i][0] == 5:
            joker.append(i)

    for i in range(len(deck)):
        if deck[i][0] == 6:
            joker.append(i)

    return joker
