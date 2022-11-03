# Day 10 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Functions with Outputs

# Basic calculator
from day10_art import logo

# Individual operations
# Division	
def divide(n1, n2):
	return n1 / n2
	
# Multiplication
def multiply(n1, n2):
	return n1 * n2

# Addition
def add(n1, n2):
	return n1 + n2

# Subtraction
def subtract(n1, n2):
	return n1 - n2

# Dictionary of operations for easy reference
operations = {
	"/" : divide,
	"*" : multiply,
	"+" : add,
	"-" : subtract,
	}

# Calculator function
def calculator():
    print(logo)

    # First number input - changed to float for obvious reasons
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)

    # Kill switch
    should_continue = True

    # Next number input logic
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        # {calculation_function} checks the operations dictionary, matches the symbol and then applies that logic to the answer (next line).
        calculation_function = operations[operation_symbol]
        # Eg. '*' matches with {multiply}, so the following line would read: answer = multiply(num1, num2)
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Kill switch interaction. 
        # 'Y' continues stringing operations together by changing num1 to the answer, 'N' will set {should_continue} to False, and then start the app again.
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            # Introduced recussion to allow user to perform additional calculations (rather than continously stringing operations together).
            calculator()

        # The following was code that was used for early iterations of the app. I left this in this assignment for reference sake.
        # operation_symbol = input("Pick another operation: ")
        # num3 = float(input("What's the next number?: "))
        # calculation_function = operations[operation_symbol]
        # # This line of code below introduced a bug. Again, I left this in this assignment for reference sake.
        # # second_answer = calculation_function(calculation_function(num1, num2), num3)
        # second_answer = calculation_function(first_answer, num3)

        # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

calculator()