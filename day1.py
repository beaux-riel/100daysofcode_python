# Day 1 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Working with Variables in Python to Manage Data

# Variables
greeting = "G'day"
user = "Beaux"

# Simple
print("Hello World!")
print("Hello " + user + "!")

# Utilising print formating (f)
print(f'{greeting} {user}!')

# Counting characters (from an input)
print(len(input("What is your name? ")))

# Assignment 1
# Variables
welcome = "Welcome to the Band Name Generator"
first_question = "What's the name of the city you grew up in? "
second_question = "What's your pet's name? "
suggestion = "Your band name could be:"

# Program
print(f'{welcome}')
city = input(f"{first_question}")
pet = input(f"{second_question}")
print(f"{suggestion} {city} {pet}!")

# Alternative program - Same result, less code.
# Prints welcome message from {welcome} variable
print(f'{welcome}')
# Prints band name suggestion AFTER taking two inputs (first_question, second_question)
print(f"{suggestion} " + input(f'{first_question}') + " " + input(f'{second_question}'))

