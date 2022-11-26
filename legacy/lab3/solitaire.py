import string
import card

def letters():
    alphabet = []
    for letter in string.ascii_uppercase:
        alphabet.append(letter)
    return alphabet

# KEYGEN-------------------------------------------

def solitaire_keystream(deck, message):
    alphabet = letters()
    encryption_key = ""
    while len(message) != len(encryption_key):

        joker = card.find_joker(deck)

        if joker[0] == 27:
            card.move_card(deck, 1, joker[0])
            joker[0] = 1
        else:
            card.move_card(deck, (joker[0] + 1), joker[0])
            joker[0] += 1

        if joker[1] == 27:
            card.move_card(deck, 2, joker[1])
            joker[1] = 2
        elif joker[1] == 26:
            card.move_card(deck, 1, joker[1])
            joker[1] = 1
        else:
            card.move_card(deck, (joker[1] + 2), joker[1])
            joker[1] += 2

        deck_a = []
        deck_b = []
        deck_c = []

        while True:
            if card.get_value(card.check_card_pos(deck, 0)) == 27:
                card.switch_deck(deck_b, deck)
                break
            else:
                card.switch_deck(deck_a, deck)

        while True:
            if card.get_value(card.check_card_pos(deck, 0)) == 27:
                card.switch_deck(deck_b, deck)
                break
            else:
                card.switch_deck(deck_b, deck)


        while len(deck) != 0:
            card.switch_deck(deck_c, deck)

        while len(deck_c) != 0:
            card.switch_deck(deck, deck_c)
        while len(deck_b) != 0:
            card.switch_deck(deck, deck_b)
        while len(deck_a) != 0:
            card.switch_deck(deck, deck_a)

        move_cards = card.get_value(card.check_card_pos(deck, 27))

        for i in range(move_cards):
            card.move_card(deck, 26, 0)

        value_top_card = card.get_value(card.check_card_pos(deck, 0))

        key_value = card.get_value(card.check_card_pos(deck, value_top_card))

        if key_value != 27:
            key_value -= 1
            # Värdet kan nu vara 0 - 25
            encryption_key += alphabet[key_value]

    return encryption_key

# ENCRYPT-------------------------------------------

def solitaire_encrypt(deck, message):
    alphabet = letters()
    key = solitaire_keystream(deck, message)
    encrypted_message = ""

    temp1 = []
    temp2 = []

    for letter in message:
        temp1.append(alphabet.index(letter) + 1)

    for letter in key:
        temp2.append(alphabet.index(letter) + 1)

    for i in range(len(temp1)):
        temp = temp1[i] + temp2[i]
        if temp > 26:
            temp -= 26
        temp -= 1
        encrypted_message += alphabet[temp]

    return encrypted_message

# DECRYPT-------------------------------------------

def solitaire_decrypt(deck, message):
    alphabet = letters()
    key = solitaire_keystream(deck, message)
    decrypted_message = ""

    temp1 = []
    temp2 = []

    for letter in message:
        temp1.append(alphabet.index(letter) + 1)

    for letter in key:
        temp2.append(alphabet.index(letter) + 1)

    for i in range(len(temp1)):
        temp = temp1[i] - temp2[i]
        if temp < 1:
            temp += 26
        temp -= 1
        decrypted_message += alphabet[temp]

    return decrypted_message


