# Day 3 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Control Flow and Logical Operators 

# Assignment 3 - 

# ASCII Art header
print('''
*******************************************************************************
888                     888              
888                     888              
888                     888              
88888b. 888  888.d8888b 888  888888  888 
888 "88b888  88888K     888 .88P888  888 
888  888888  888"Y8888b.888888K 888  888 
888  888Y88b 888     X88888 "88bY88b 888 
888  888 "Y88888 88888P'888  888 "Y88888 
                                     888 
                                Y8b d88P 
                                 "Y88P"  
*******************************************************************************
''')
# Generic Intro statments
print("Welcome to Husky Hunt!\n")
print("Oh no, Kali the Husky escaped from home! Your mission is to track her down.\n")

#Write your code below this line 👇

# Nested if statements
choice1 = input('You follow a trail of destruction throughout the neighbourhood and soon arrive at Kali\'s favourite spot; the duck pond. Which way will you go from here? Type "left" or "right" \n').lower()
# Statement 1
if choice1 == "left":
  choice2 = input('\nYou followed Kali\'s tracks all the way to Cultus Lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    # Statement 2
  if choice2 == "wait":
    choice3 = input("\nAfter an uneventful trip you arrive at the island. On this island are 3 tents. One red, one yellow and one blue. From each tent comes a low growling sound... Which colour tent do you look inside? \n").lower()
    # Statement 3
    if choice3 == "red":
      print("It's a BEAR! Game Over.")
    elif choice3 == "yellow":
      print("\nYou found Kali! You Win!")
    elif choice3 == "blue":
      print("You enter the tent to find a farting truck driver! Game Over.")
      # Statement 3 else
    else:
      print("You chose a tent that doesn't exist. Game Over.")
# Statement 2 else
  else:
    print("You get a cramp and drown. Game Over.")
# Statement 1 else
else:
  print("You get eaten by a rabid duck. Game Over.")
