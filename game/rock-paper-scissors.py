import random
print("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _________
---'      ____)____
             ______)
              _______)
            _______)
---.___________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (_____)
---.__(____)
""")





user_choice = input("Your choice: ")

computer_choice = random.randint(0, 2)
print("Computer chose:", computer_choice)
