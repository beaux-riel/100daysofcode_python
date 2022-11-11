# Day 18 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Turtle and the Graphical User Interface (GUI) - Exercises

# Import ya' business
import turtle as t
import random

# Create a turtle object named Beaux (naturally).
beaux = t.Turtle()
# Change screen's color mode to allow for random RGB strings
t.colormode(255)
beaux.shape("turtle")

# Color list for turtle to draw with
# colors = ["blue", "purple", "lime", "sky blue", "pale green", "gold", "indigo", "red"]

# Random color picker
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_string = (r, g, b)
    return rgb_string

# Directions for old mate to turn (went a little crazy)
directions = [0, 45, 90, 135, 180, 225, 270, 315]
# beaux.pensize(10)
beaux.speed(0)

# Fill that screen yo'
for _ in range(2000):
    beaux.forward(30)
    beaux.setheading(random.choice(directions))
    beaux.color(random_color())
    beaux.pensize(random.randint(0,15))

# Give me a screen to work with that only closes "on click"
screen = t.Screen()
screen.exitonclick()