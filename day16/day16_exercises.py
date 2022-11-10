# Day 16 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Object Oriented Programming (OOP) - Day 16 exercises 

# from turtle import Turtle, Screen

# beaux = Turtle()
# print(beaux)
# beaux.shape("turtle")
# beaux.color("DeepPink3")
# beaux.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable() 
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"]) 
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Age", [1, 2, 3])
table.align = "l"

print(table)