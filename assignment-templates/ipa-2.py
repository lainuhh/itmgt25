alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shift_letter(letter, shift):
    new_position = (alphabet.find(letter.capitalize()) + shift) % 26
    return alphabet[new_position]


def caesar_cipher(message, shift):
    encrypted_msg = ''
    for character in message:
        new_position = (alphabet.find(character.capitalize()) + shift) % 26
        encrypted_msg += alphabet[new_position]
    return encrypted_msg


def shift_by_letter(letter, letter_shift):
    if letter == " ":
        shifted_letter = " "
    else:
        shift_num = alphabet.find(letter_shift)
        new_position = (alphabet.find(letter) + shift_num) % 26
        shifted_letter = alphabet[new_position]
    return shifted_letter


def vigenere_cipher(message, key):
    encrypted_msg = ''
    for i in range(len(message)):
        if message[i] == " ":
            encrypted_msg += " "
        else:
            key_index = i % len(key)
            new_position = (alphabet.find(message[i].capitalize()) + alphabet.find(key[key_index])) % 26
            encrypted_msg += alphabet[new_position]
    return encrypted_msg


def scytale_cipher(message, shift):
    if len(message) % shift > 0:
        message += "_" * (shift - (len(message) % shift))
    encoded_message = ""
    for i in range(len(message)):
        # new pos = column_number + (num_of_columns * column_pos)
        new_pos = (i // shift) + (len(message) // shift) * (i % shift)
        encoded_message += message[new_pos]
    return encoded_message


def scytale_decipher(message, shift):
    decoded_message = ""
    for i in range(shift):
        decoded_message += message[i::shift]
    return decoded_message
