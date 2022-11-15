# Day 21 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Build the Snake Game Part 2: Inheritance and List Slicing - Food Module
# Exercise - Build the Snake Game Part 2: Inheritance & List Slicing

# Come on in, the code is fine!
from turtle import Turtle
import random

# Food class w/ turtle super class (in order to inherit turtle-y attributes)
class Food(Turtle):

    # Design/define our food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("violet")
        self.speed(0)
        self.refresh()

    # Give the food some way to spawn randomly on screen.
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)