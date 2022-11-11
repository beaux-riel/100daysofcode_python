# Day 18 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Turtle and the Graphical User Interface (GUI) - Spirograph

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

beaux.pensize(10)
beaux.speed(0)

# Fill that screen yo'
def spirograph_1(gap):
    for _ in range(int(360 / gap)):
        beaux.color(random_color())
        beaux.circle(100)
        current_heading = beaux.heading()
        beaux.setheading(beaux.heading() + gap)

# def spirograph_2():
#     for _ in range(360):
#         beaux.color(random_color())
#         beaux.circle(100)
#         current_heading = beaux.heading()
#         beaux.setheading(current_heading + 10)

spirograph_1(20)

# Give me a screen to work with that only closes "on click"
screen = t.Screen()
screen.exitonclick()