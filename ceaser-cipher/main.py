from art import logo
from alphabet import alphabet

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(simple_text, shift_number):
    """
    Takes simple text and shift number and prints encrypted text
    """
    cipher_text = ""
    for char in simple_text:
        char_index = alphabet.index(char)
        cipher_char_index = char_index + shift_number
        if cipher_char_index >= 26:
            cipher_char_index -= 26
        cipher_text += alphabet[cipher_char_index]
    print(f"The encoded text is {cipher_text}")


def decrypt(encrypt_text, shift_number):
    """
    Takes an encrypted text and shift number and prints normal text
    """
    plain_text = ""
    for char in encrypt_text:
        char_index = alphabet.index(char)
        plain_char_index = char_index - shift_number
        plain_text += alphabet[plain_char_index]
    print(f"The decoded text is {plain_text}")


def caeser(normal_text, shift_number, direction_type):
    if direction_type == "encode":
        encrypt(normal_text, shift_number)
    elif direction_type == "decode":
        decrypt(normal_text, shift_number)
    else:
        print("Invalid direction")


caeser(text, shift, direction)
