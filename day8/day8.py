# Day 8 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Function Parameters and Caeser Cipher

# Note to self: I wasn't super focused on this set of lessons. Logic discussions worth another visit.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Condensed function (vs encode() decode() from previous exercises)
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    # shift_amount = shift_amount * -1
    shift_amount *= -1
  for char in start_text:
    # If character in alphabet encode/decode accordingly
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    # Else just add the symbol/number
    else:
        end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from day8_art import logo
print(logo)

# Program switch
should_continue = True

# Inputs/variables
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Prevent someone breaking the app by using an 'out of index' number
    shift = shift % 26

    # Call caeser function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Restart prompt
    restart = input('Type \"yes\" if you would like to go again. Otherwise type \"no\".\n').lower()
    if restart == 'no':
        should_continue = False
        print('Goodbye')