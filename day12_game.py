# Day 12 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Scope and Number Guessing Game

from random import randint
from day12_art import logo

# Set constants for turn limits
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Game loop
def game():
    print(logo)
    #Choose a random number between 1 ands 100
    print("Welcome to Beaux's Kick Ass Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Psst. The correct answer is: {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        #Let the user guess a number
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()

# Exercise notes: I coded something that worked, but it was messy.
# Watching the Udemy walkthrough helped me to breakdown the problem,
# versus allowing myself just to randomly work on 15 different aspects 
# of a build at any given time. Slow. Steady. Thoughtful. Deliberate.