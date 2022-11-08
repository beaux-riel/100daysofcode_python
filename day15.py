# Day 15 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Local Development Environment Setup & the Coffee Machine

# Imports - Once again, attempted to make this feel a little more interactive/"real world".
import os
import time

# Supplied data
# Increased cost of each item because "why not"?
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 3.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 4.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 4.0,
    }
}

# Total from all coffee's sold
profit = 0
# Starting resources
# Updated resources so we could "make" more than one cup.
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

# Screen clear
def clear():
   os.system('clear')

# Resource check
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

# Processes coin payment by taking the quantity of each coin (this step is not reflective of the real world - worth revisiting)
# Updated coin payment to feel a little more "Canadian"
# Note: Worth revisiting and allowing the user to "skip" a coin or making certain coin input optional
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = float(input("How many toonies?: ")) * 2
    total += float(input("How many loonies?: ")) * 1
    total += float(input("How many quarters?: ")) * 0.25
    total += float(input("How many dimes?: ")) * 0.1
    total += float(input("How many nickles?: ")) * 0.05
    return total

# Compares money received to drink cost. Refunds if insufficient funds. 
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print('\nDispensing change')
        time.sleep(3)
        print(f"\nHere is ${change:.2f} in change.")
        time.sleep(3)
        global profit
        profit += drink_cost
        return True
    else:
        # Corrected to 2 decimal places
        print(f"\nSorry that item cost ${drink_cost:.2f}.\nRefunding: ${money_received:.2f}.")
        return False

# Make coffee - Duh. Removes individual resources from resources dictionary
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\nDispensing {drink_name}") 
    time.sleep(3)
    print(f"\nHere is your {drink_name} ☕️. Enjoy!")
    time.sleep(3)
    clear()

# Kill switch
is_on = True

# Repeated while loop
while is_on:
    # Initial input
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turns off the machine
    if choice == "off":
        is_on = False
    # Generates a report that outline total resources remaining
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
    # Else checks that resources are sufficient
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            # and that payment has been made
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
