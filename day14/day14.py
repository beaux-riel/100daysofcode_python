# Day 14 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Higher Lower Game Project

from day14_art import *
from day14_game_data import data
import random
import os

def clear():
   os.system('clear')

def format_data(account):
	"""Format the account data into printable format"""
	account_name = account["name"]
	account_descr = account["description"]
	account_country = account["country"]
	return f"{account_name}, a {account_descr} from {account_country}"

def check_answer(guess, a_followers, b_followers):
	"""Take the user guess and follower counts and returns if they got it right."""
	if a_followers > b_followers:
		return guess == "a"
	else:
		return guess == "b"

# Score
score = 0
# Kill switch
game_should_continue = True
# Intereting piece of logic. {account_b} is randomly chosen here, then when the game loads that choice is
#  automagically moved to {account_a} and {account_b} is chosen again, but from within the game loop.
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
	# Generate a random account from the game data
	# Making account at position B become the next account at position A.
	account_a = account_b
	account_b = random.choice(data)

	if account_a == account_b:
		account_b == random.choice(data)
	
	# Positioning of clear here creates a very cool screen clear when game starts and after each turn.
	clear()
	# Display art
	print(logo)
	# Compare statements (+ ASCII art)
	print(f"Compare A: {format_data(account_a)}.")
	print(vs)
	print(f"Against B: {format_data(account_b)}.")

	# Ask user for a guess
	guess = input("Who has more followers? Type 'A' or 'B': ").lower()

	# Check if user is correct
	# Get follower account of each account
	a_follower_count = account_a["follower_count"]
	b_follower_count = account_b["follower_count"]
	is_correct = check_answer(guess, a_follower_count, b_follower_count)

	# Give user feedback on their guess
	# Score keeping.
	if is_correct:
		score += 1
		print(f"You're right! Current score: {score}.")
	else:
		game_should_continue = False
		print(f"Sorry, that's wrong. Final score: {score}.")
