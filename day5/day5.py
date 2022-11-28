# Day 5 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Python Loops 

#Password Generator Project
import random
import time

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")

new_password_required = True

while(new_password_required):
	# Ask user if password a new password is required
	is_password_required = input(f'Do you require a new password? Type Y for yes or N to exit. ')
	
	# If password is required the program will begin prompting user, otherwise app will terminate.
	if (is_password_required.lower() == 'y'):
		new_password_required = True
	else:
		# Added some timers so the app felt a little more interactive.
		print(f'\nShutdown sequence initiated.')
		time.sleep(1)
		print(f'\nDeleting all secret files.')
		time.sleep(2)
		print(f'\nApp terminated.')
		exit()

	# Number of letters/symbols/numbers user requires for password
	nr_letters = int(input("\nHow many letters would you like in your password?\n")) 
	nr_symbols = int(input(f"\nHow many symbols would you like?\n"))
	nr_numbers = int(input(f"\nHow many numbers would you like?\n"))
	
	#Eazy Level - Order not randomised:
	#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
	
	#Hard Level - Order of characters randomised:
	#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
	
	# Empty variable to store password string
	password = ''
	
	# For loop to select letters/characters based on user input
	for char in range (1, nr_letters +1):
		random_char = random.choice(letters)
		password += random_char
	
	# For loop to select numbers based on user input
	for num in range (1, nr_symbols +1):
		random_num = random.choice(numbers)
		password += random_num
	
	# For loop to select symbols based on user input
	for sym in range (1, nr_numbers +1):
		random_sym = random.choice(symbols)
		password += random_sym
	
	# Variable to take {password} string and randomise contents for a more secure password
	random_password = ''.join(random.sample(password, len(password)))
	
	# Display password then ask user if they require another new password
	print(f'\n{random_password}\n')
	is_password_required
		
