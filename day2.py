# Day 2 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Understanding Data Types and How to Manipulate Strings

# Assignment 2
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Program
# Greeting
print("Welcome to the tip calculator.")

# Variable 1
bill_total = float(input("What was the total bill? $"))

# Variable 2
desired_tip = float(input("What percentage tip would you like to give? ")) 

# Variable 3
guest_count = int(input("How many people to split the bill? "))

# Final tip - conversion
final_tip = (1 + desired_tip / 100)

# Final bill calculation
final_bill = ((bill_total * final_tip) / guest_count)

# Print statement
print(f'Each person should pay: ${final_bill:.2f}')
