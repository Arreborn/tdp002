import card
import solitaire
import os
import string

def select_seed():
        while True:
            seed = -1
            try:
                seed = int(input("Please enter a seed (only whole numbers). Enter 0 for a random seed: "))

            except ValueError:
                print("Error! Seed contains invalid characters.")

            if seed != -1 and seed != 0:
                break

            if seed == 0:
                seed = card.random_seed()
                print("You have a randomly generated seed. Make sure to save this seed for future decryption.")
                print("Your seed is: " + str(seed))
                input("Press any key to continue.")
                break
        return seed

def main():
    os.system('clear')
    print("Welcome to the encryption generator!")
    seed = select_seed()
    saved_messages = []

    os.system('clear')

    while True:

        print("                       Menu")
        print("------------------------------------------------------")
        print("1: Select new seed (current seed: " + str(seed) + ")")
        print("2: Encrypt a message")
        print("3: Decrypt a message")
        print("4: Show all saved encrypted messages")
        print("0: Exit")
        print("------------------------------------------------------")

        deck1 = card.create_solitaire_deck(seed)
        deck2 = card.create_solitaire_deck(seed)

        command = input("Please select an option: ")
        print("------------------------------------------------------")

        match command:
            case "1":
                seed = select_seed()

            case "2":
                original_message = input("Enter a message to encrypt (Only letters A - Z will be saved): ").upper()
                message = ""
                for letter in original_message:
                        if letter in string.ascii_uppercase:
                                message += letter

                encrypted_message = solitaire.solitaire_encrypt(deck1, message)
                print("------------------------------------------------------")
                print("The encrypted message is: " + encrypted_message)
                save_selector = input("Save message? [y / n]: " ).upper()
                if save_selector == "Y":
                    saved_messages.append(encrypted_message)

            case "3":
                if len(saved_messages) == 0:
                    print("You have no saved messages to decrypt.")
                    input("Press any key to continue.")
                else:
                    for i in range(len(saved_messages)):
                        print(str(i + 1) + ": " + saved_messages[i])
                    print("------------------------------------------------------")
                    command = int(input("Select a message to decrypt: "))
                    command -= 1

                    try:
                        decrypted_message = solitaire.solitaire_decrypt(deck2, saved_messages[command])
                        print("The decrypted message is: " + decrypted_message)
                        input("Press any key to continue.")
                    except ValueError:
                        print("Error! Incorrect value entered as selection. Please only enter a number.")
                        input("Press any key to continue.")
                    except IndexError:
                        print("Error! The selected number isn't present in the list.")
                        input("Press any key to continue.")

            case "4":
                for i in range(len(saved_messages)):
                    print(str(i + 1) + ": " + saved_messages[i])
                print("------------------------------------------------------")
                command = input("Decrypt all? [y / n]: ").upper()

                if command == "Y":
                    decrypt_list = []
                    for message in saved_messages:
                        deck2.clear()
                        deck2 = card.create_solitaire_deck(seed)
                        decrypt_list.append(solitaire.solitaire_decrypt(deck2, message))

                    for i in range(len(decrypt_list)):
                        print(str(i + 1) + ": " + decrypt_list[i])
                    input("Press any key to continue.")
                    print("------------------------------------------------------")
            case "0":
                command = input("All saved messages will be deleted upon exiting the program. Type 'exit' to quit. \nPress enter to go back to the program. ")
                if command == "EXIT" or command == "exit":
                    break
            case other:
                print("Unknown command.")
                input("Press any key to continue.")


        os.system('clear')

        deck1.clear()
        deck1 = card.create_solitaire_deck(seed)
        deck2.clear()
        deck2 = card.create_solitaire_deck(seed)

if __name__ == '__main__':
    main()
    os.system('clear')

