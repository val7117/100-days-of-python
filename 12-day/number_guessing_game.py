# This is a simple number guessing name
from art import logo
import random

print(logo)
print("I'm thinking of a number between 1 and 100.")

# Choosing a level of difficulty
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty_level == 'easy':      
    number_of_lives = 10
elif difficulty_level == 'hard':
    number_of_lives = 5
else:
    print("Sorry, wrong option.")
    exit(1)
print(f"You have {number_of_lives} attempts.")

# Choosign a random int between 1 and 100
guessed_number = random.randint(1, 100)

# Printing function
def info_print(num_of_lives=int):
    print("Guess again.")
    print(f"You have {num_of_lives} attempts remaining to guess a number.")

# Play logic
playing = True
while playing:
  if number_of_lives != 0:
    guess = int(input("Make a guess: "))
    if guess == guessed_number:
      print(f"You got it! The answer was {guess}.")
      playing = False
    elif guess < guessed_number:
        number_of_lives -= 1
        print("Too low.")
        info_print(number_of_lives)
    elif guess > guessed_number:
        number_of_lives -= 1
        print("To high.")
        info_print(number_of_lives)
  else:
    print("You've run out of guesses, you lose.")
    playing = False