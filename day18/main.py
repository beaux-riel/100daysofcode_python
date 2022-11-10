# Day 18 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Turtle and the Graphical User Interface (GUI) - Main 

# Import ya' business
from turtle import Turtle, Screen
import random

# Create a turtle object named Beaux (naturally).
beaux = Turtle()
beaux.shape("turtle")
beaux.color("DeepPink3")

# Color list for turtle to draw with
colors = ["blue", "purple", "lime", "sky blue", "pale green", "gold", "indigo", "red"]

# Draw shape function
def draw_shape(num_sides):
    angle = 360 / num_sides
    # turtle.speed(0) is the fastest. Goes slower as number increases.
    beaux.speed(0)
    # Now let's create. For number of sides we're going to draw for 20 paces then 
    # turn 360 degrees/number of sides and repeat for the number of sides.
    for _ in range(num_sides):
        beaux.forward(20)
        beaux.right(angle)
    # Felt spicy, mirrored the art. Same as above but runs in the opposite direction
    # immediately after the first shape is drawn.
    for _ in range(num_sides):
        beaux.forward(20)
        beaux.left(angle)
        
# How many times do you want to repeat this? 
# I'm starting at Triangle (3 sides) and am working up to a Pentacontagon (50 sides).
for shape_side_n in range(3, 51):
    beaux.color(random.choice(colors))
    draw_shape(shape_side_n)

# def draw_line():
#     for _ in range(15):
#         beaux.forward(10)
#         beaux.penup()
#         beaux.forward(10)
#         beaux.pendown()

# draw_line()

# Give me a screen to work with that only closes "on click"
screen = Screen()
screen.exitonclick()