############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#################################################################
from art import logo
import random
import os

# Clear screen
os.system('clear')

# List of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Printing function
def printing_func(cards):
    result = sum(cards)
    print(logo)
    print(f"    Your cards: {cards}, current score: {result}")
    print(f"    Dealer's first card: {dealer_first_card}")

playing = True

while playing:
    new_game_question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    os.system('clear')
    if new_game_question == 'n':
        playing = False
        continue

    # Lists of cards for player and dealer
    player_cards = []
    dealer_cards = []

    # Function that chooses a random card from a deck and automatically choose value for Ace (11 or 1)
    def choose_card(deck=list):
        """This function chooses a random card and append it into the deck."""
        card = random.choice(cards)
        if card == 11 and (21 - sum(deck)) < 11:
            card = 1
            deck.append(card)
        deck.append(card)

    # Two starting cards for player and dealer
    for i in range(0, 2):
        choose_card(player_cards)
        choose_card(dealer_cards)

    # Add cards to dealer while the dealer's result < 17
    while sum(dealer_cards) < 17:
        choose_card(dealer_cards)

    # First known dealer card and a score
    dealer_first_card = dealer_cards[0]
    
    # Print result
    printing_func(player_cards)

    # Asking to get another card
    keep_asking = True
    while sum(player_cards) <= 21 and keep_asking:
        get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_another_card == 'n':
            keep_asking = False
        else:
            choose_card(player_cards)
        os.system('clear')
        printing_func(player_cards)

    # Get final results of player & dealer
    player_result = sum(player_cards)
    dealer_result = sum(dealer_cards)

    # Print final results of player & dealer
    print(f"Your final hand: {player_cards}, final score: {player_result}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_result}")

    # Check who has won
    if player_result > 21:
        print("You went over. You lose 😤")
    elif dealer_result > 21:
        print("Opponent went over. You win 😁")
    elif player_result == dealer_result:
        print("Draw 🙃")
    elif dealer_result > player_result:
        print("You lose 😤!")
    else:
        print("You win 😃")