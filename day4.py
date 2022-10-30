# Day 4 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Randomisation and Python Lists 

import random

#ASCII images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Scissors
'''

#Write your code below this line 👇

# Variables
# Images list
game_images = [rock, paper, scissors]

# Game answer bank
user_win = 'You win!\n'
computer_win = 'You lose. :(\n'
invalid_guess = 'You typed an invalid answer. You lose.\n'
draw = 'That\'s a draw!\n'

# Added while loop so this app is actually usable
while(True):
	# Take user input/guess
	user_selection = int(input('Which do you choose? Type 0 for rock, 1 for paper and 2 for scissors.\n'))
	
	# Check if user guess is valid
	if user_selection >= 3 or user_selection < 0:
		print(invalid_guess)
	else:
		print(game_images[user_selection])
	
		# Generate computer guess 
		computer_selection = random.randint(0,2)
		print(f'The computer chose:')
		print(game_images[computer_selection])
	
		# Game logic
		if user_selection == 0 and computer_selection == 2:
			print(user_win)
		elif computer_selection == 0 and user_selection == 2:
			print(computer_win)
		elif computer_selection > user_selection:
			print(computer_win)
		elif user_selection > computer_selection:
			print(user_win)
		elif computer_selection == user_selection:
			print(draw)

