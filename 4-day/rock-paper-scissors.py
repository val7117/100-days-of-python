# This is a rock, paper, scissors game!

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]

# Ask for a choice and check the input

person_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if person_number > 2:
    print("You typed an invalid number, you lose!")
    exit(1)

# Randomization and selection

person_choice = options[person_number]
computer_number = random.randint(0,2)
computer_choice = options[computer_number]

# Printing choices

print(person_choice)
print("Computer chose:")
print(computer_choice)

# Rock, paper, scissors logic

if person_number == 0 and computer_number == 2:
    print("You win")
elif person_number == 2 and computer_number == 1:
    print("You win")
elif person_number == 1 and computer_number == 0:
    print("You win")
elif computer_number == 0 and person_number == 2:
    print("You lose")
elif computer_number == 2 and person_number == 1:
    print("You lose")
elif computer_number == 1 and person_number == 0:
    print("You lose")
else:
    print("Draw")