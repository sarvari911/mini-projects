from art_ceaser_cipher import logo
print(logo)

import string

def caesar_cipher(text, shift_amount, direction):
    result = ""

    if direction == "decode":
        shift_amount *= -1

    for char in text:
        if char in string.ascii_lowercase:
            new_index = (string.ascii_lowercase.index(char) + shift_amount) % 26
            result += string.ascii_lowercase[new_index]
        else:
            result += char

    return result


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ["encode", "decode"]:
        print("Invalid input. Try again.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    output = caesar_cipher(text, shift, direction)
    print(f"Result: {output}")

    again = input("Type 'yes' to go again, otherwise 'no': ").lower()
    if again != "yes":
        print("Goodbye!")
        break
      
