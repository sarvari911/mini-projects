#three single quotes in a print sattement is used to print a string as it is       
print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print("Welcome to the Treasure Island.")
print("Your mission ia to find the treasure.")
choice1 = input("You're at a crossroad, where do you want to go? Type 'left or 'right' ").lower()
# or input('You/'re at a crossroad, where do you want to go? Type "left" or "right".')
# basically using a / before a ' in a '' quotations in a print satement skpis the ' as the end of statement and prints it as it is



    # Correcting the indentation and ensuring proper new line formatting
    # What went wrong before:
    # 1. Indentation was inconsistent, causing syntax errors.
    # 2. Missing newline characters made the input prompts hard to read.
    # 3. Typos in strings (e.g., "ia" instead of "is", "unharmed" was misspelled).
    # 4. Logical errors in print statements (e.g., "beastrs" instead of "beasts").
    # 5. Lack of clarity in input prompts.
if choice1 == "left":
        choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\n'
                        'Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()
        if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed. There is a house with 3 doors:\n"
                            "one red, one yellow, and one blue. Which color do you choose? ").lower()
            if choice3 == "red":
                print("It's a room full of fire. Game over.")
            elif choice3 == "yellow":
                print("You found the treasure! You win!")
            elif choice3 == "blue":
                print("You enter a room full of beasts. Game over.")
            else:
                print("You've chosen a door that doesn't exist. Game over.")
        else:
            print("You got attacked by an angry trout. Game over.")
else:
        print("You fell into a hole. Game over.")
