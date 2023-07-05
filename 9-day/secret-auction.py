from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

bids_dict = {}
any_bidders_left = True

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ''
    for name in bids_dict:
        if bids_dict[name] > highest_bid:
            highest_bid = bids_dict[name]
            winner = name
    print(f"The winner is {winner} with a bid ${highest_bid}.")

while any_bidders_left:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids_dict[name] = bid
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if question == 'no':
        any_bidders_left = False
        find_highest_bidder(bids_dict)
    elif question == 'yes':
        os.system('clear')