# Day 18 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Turtle and the Graphical User Interface (GUI) - Main 

from turtle import Turtle, Screen
import random

beaux = Turtle()
beaux.shape("turtle")
beaux.color("DeepPink3")

colors = ["blue", "purple", "lime", "sky blue", "pale green", "gold", "indigo", "red"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        beaux.forward(100)
        beaux.right(angle)

for shape_side_n in range(3, 11):
    beaux.color(random.choice(colors))
    draw_shape(shape_side_n)

# def draw_line():
#     for _ in range(15):
#         beaux.forward(10)
#         beaux.penup()
#         beaux.forward(10)
#         beaux.pendown()

# draw_line()

screen = Screen()
screen.exitonclick()