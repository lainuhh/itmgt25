
def shift_letter(letter, shift):
    if letter == " ":
        return " "
    new_position = ((ord(letter) + (shift + 65)) % 26) + 65
    return chr(new_position)


def caesar_cipher(message, shift):
    encrypted_msg = ''
    for character in message:
        if character == " ":
            encrypted_msg += " "
        else:
            new_position = ((ord(character) + (shift + 65)) % 26) + 65
            encrypted_msg += chr(new_position)
    return encrypted_msg


def shift_by_letter(letter, letter_shift):
    if letter == " ":
        shifted_letter = " "
    else:
        shift_num = ord(letter_shift)
        new_position = ((ord(letter) + shift_num) % 26) + 65
        shifted_letter = chr(new_position)
    return shifted_letter


def vigenere_cipher(message, key):
    encrypted_msg = ''
    extended_key = ''

    for i in range(len(message)):
        extended_key += key[(i % len(key))]

    for i in range(len(message)):
        print(f"Editing char: {message[i]} | {ord(message[i])}")
        if message[i] == " ":
            encrypted_msg += " "
        else:
            key_index = i % len(key)
            new_position = ((ord(message[i]) + ord(extended_key[key_index])) % 26) + 65
            encrypted_msg += chr(new_position)
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
