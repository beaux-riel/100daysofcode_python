#Day 1 of 100 Days of Code - Python
#Exercise - Learn to work with "print"

#Variables
greeting = "G'day"
user = "Beaux"

#Simple
print("Hello World!")
print("Hello " + user + "!")

#Utilising print formating (f)
print(f'{greeting} {user}!')


#Assignment 1
#Variables
welcome = "Welcome to the Band Name Generator"
first_question = "What's the name of the city you grew up in? "
second_question = "What's your pet's name? "
suggestion = "Your band name could be:"

#Program
print(f'{welcome}')
city = input(f"{first_question}")
pet = input(f"{second_question}")
print(f"{suggestion} {city} {pet}!")

