# Day 1 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Learn to work with "print"

# Variables
greeting = "G'day"
user = "Beaux"

# Simple
print("Hello World!")
print("Hello " + user + "!")

# Utilising print formating (f)
print(f'{greeting} {user}!')

# Counting characters (from an input)
name = input("What is your name? ")
print(len(name))

# Assignment 1
# Variables
welcome = "Welcome to the Band Name Generator"
firstQuestion = "What's the name of the city you grew up in? "
secondQuestion = "What's your pet's name? "
suggestion = "Your band name could be:"

# Program
print(f'{welcome}')
city = input(f"{firstQuestion}")
pet = input(f"{secondQuestion}")
print(f"{suggestion} {city} {pet}!")

# Alternative program - Same result, less code.
# Prints welcome message from {welcome} variable
print(f'{welcome}')
# Prints band name suggestion AFTER taking two inputs (firstQuestion, secondQuestion)
print(f"{suggestion} " + input(f'{firstQuestion}') + " " + input(f'{secondQuestion}'))

