# Day 18 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Turtle and the Graphical User Interface (GUI) - Main

# Saving below code to show how I worked through this exercise.
# Also save to Github repository as "day19/color_extractor.py"

# import colorgram

# rgb_colors = []

# # Extract 11 colors from an image.
# # Note: Need containing folder included in path for this to work properly.
# colors = colorgram.extract('day19/finish.jpg', 11)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random

t.colormode(255)

finish_color_list = [(254, 215, 20), (30, 22, 17), (136, 99, 57), (215, 228, 242), (68, 100, 123), (242, 246, 244), (14, 24, 36), (246, 241, 245), (152, 156, 186), (2, 169, 229)]
logo_color_list = [(254, 222, 69), (231, 73, 130), (39, 165, 92), (159, 218, 254), (82, 239, 182), (0, 169, 230), (91, 59, 186), (254, 137, 173), (198, 175, 243)]

beaux = t.Turtle()
beaux.speed(0)
beaux.hideturtle()
beaux.penup()

# Find lower left corner of screen
beaux.setheading(225)
beaux.forward(550)
beaux.setheading(0)
number_of_dots = 256

for dot_count in range(1, number_of_dots + 1):
    beaux.dot(20, random.choice(logo_color_list))
    beaux.penup()
    beaux.forward(50)

    if dot_count % 16 == 0:
        beaux.setheading(90)
        beaux.forward(50)
        beaux.setheading(180)
        beaux.forward(800)
        beaux.setheading(0)

screen = t.Screen()
screen.exitonclick()