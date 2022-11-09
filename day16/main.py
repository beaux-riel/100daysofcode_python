# Day 16 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Object Oriented Programming (OOP)

# Coffee machine (day 15) code but with an OOP spin

# Import ya' packages
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Created objects from classes 
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

# Kill switch
is_on = True

# Reports 
coffee_maker.report()
money_machine.report()

# While loop
while is_on:
    # Get menu, take input
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    # If kill switch...
    if choice == "off":
        is_on = False
    # If report...
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # Else order a coffee
    else:
        # Drink choice
        drink = menu.find_drink(choice)
        # If sufficient resources and payment has been made...
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make my coffee!
            coffee_maker.make_coffee(drink)
