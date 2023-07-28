# This is a higher lower game

from art import logo, vs
from game_data import data
import random
import os

# Clear sceent command
os.system('clear')

# Generate A random
a_random = random.choice(data)

# Printing function
def printing_func():
    """This function prints the compared choices"""
    print(f"Compare A: {a_name}, a {a_description}, from {a_country}")
    print(vs)
    print(f"Against B: {b_name}, a {b_description}, from {b_country}")

# Additional parameters of game
Playing = True
score = 0
first_try = 0

# Game logic
while Playing:
    print(logo)

    # Generate B random
    b_random = random.choice(data)

    # Exclude repeatition
    while a_random == b_random:
        b_random = random.choice(data)

    # Extract A choice components
    a_name = a_random["name"]
    a_follower_count = a_random["follower_count"]
    a_description = a_random["description"]
    a_country = a_random["country"]

    # Extract B choice components
    b_name = b_random["name"]
    b_follower_count = b_random["follower_count"]
    b_description = b_random["description"]
    b_country = b_random["country"]
    
    # Do not print result during first try
    if first_try != 0:
        print(f"You're right! Current score: {score}")
    printing_func()

    # Asking for a choice
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear sceent command
    os.system('clear')

    # Main checking logic
    if answer == "a" and a_follower_count >= b_follower_count:
        score += 1
        a_random = b_random
    elif answer == "b" and b_follower_count >= a_follower_count:
        score += 1
        a_random = b_random
    else:
        Playing = False
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
    
    # Increase count of tries
    first_try += 1