# Day 7 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Hangman 

import random

# Provided with course materials
from hangman_art import stages, logo
from hangman_words import word_list

# ASCII Art Header
print(logo)

# Game "switch"
game_is_finished = False
lives = len(stages) - 1

# Chosen word from hangman_words
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Blank display for guesses
display = []
for _ in range(word_length):
    display += "_"

# Guess
while not game_is_finished:
    guess = input("Guess a letter: ").lower()

	# Repeated guess
    if guess in display:
        print(f"You've already guessed {guess}")

	# Logic for placing letters in empty spots
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

	# Kill switch if all lives lost
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")
    
	# Win
    if not "_" in display:
        game_is_finished = True
        print("You win.")

	# Print ASCII Art after each failed guess
    print(stages[lives])