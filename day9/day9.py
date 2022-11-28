# Day 9 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Dictionaries, Nesting and the Secret Auction

# replit only works with replit IDE
# from replit import clear

# Import ASCII Art
from day9_art import logo
print(logo)

# Creating bid dictionary for key:value pairs
bids = {}

# Kill switch
bidding_finished = False

# Function to identify the highest bidder
def find_highest_bidder(bidding_record):
    #Current highest bid and winner
    highest_bid = 0
    winner = ""

    # Logic for replacing highest bidder each time
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid: 
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Function for taking inputs from bidders
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

    # Logic for program loop or to announce the highest bidder
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)

# I'll deal with this next line after day 15.
#   elif should_continue == "yes":
    # clear()