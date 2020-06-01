# Caesar Cipher
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 7

def choose_action():
    action = input("Would you like to encrypt or decrypt?")
    if (action == "encrypt"):
        message = input("What would you like to encrypt? ")
        encrypt(message)
    elif (action == "decrypt"):
        message = input("What would you like to decrypt? ")
        decrypt(message)

# def caesar_cipher():
#     key = 5
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     for char in message:
#         # for alphabet[char], hidden_message[char +5]




def encrypt(message):
    encypted_message = ""
    for letter in message:
        if(letter == " "):
            new_letter = " "
        elif (letter != " "):
            index = alphabet.index(letter)
            if(index+key < 26):
                new_letter = alphabet[index+key]
            else:
                new_letter = alphabet[index-(26-key)]
        encypted_message = encypted_message + new_letter
    print(encypted_message)


def decrypt(message):
    encypted_message = ""
    for letter in message:
        if (letter == " "):
            new_letter = " "
        elif (letter != " "):
            index = alphabet.index(letter)
            if (index - key >= 0):
                new_letter = alphabet[index - key]
            else:
                new_letter = alphabet[index + (26 - key)]
        encypted_message = encypted_message + new_letter
    print(encypted_message)

choose_action()
