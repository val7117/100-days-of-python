# This is my own code for Blackjack or 21 game
# Python 3.11
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