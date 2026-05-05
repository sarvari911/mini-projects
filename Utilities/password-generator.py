import random
import string

print("WELCOME TO THE PASSWORD GENERATOR")
print("This program will generate a password for you")

password_length = int(input("Enter the length of the password: "))
include_special_characters = input("Do you want to include special characters? (yes/no): ").lower()
include_numbers = input("Do you want to include numbers? (yes/no): ").lower()
include_uppercase = input("Do you want to include uppercase letters? (yes/no): ").lower()
include_lowercase = input("Do you want to include lowercase letters? (yes/no): ").lower()
# Check if at least one character type is selected
if not (include_special_characters == "yes" or include_numbers == "yes" or include_uppercase == "yes" or include_lowercase == "yes"):
    print("Please select at least one character type.")
else:
    # Initialize the character set based on user input
    character_set = ""
    if include_special_characters == "yes":
        character_set += string.punctuation
    if include_numbers == "yes":
        character_set += string.digits
    if include_uppercase == "yes":
        character_set += string.ascii_uppercase
    if include_lowercase == "yes":
        character_set += string.ascii_lowercase

    # Generate the password
   # password = ''.join(random.choice(character_set) for password in range(password_length))
    #print("Your generated password is:", password)

