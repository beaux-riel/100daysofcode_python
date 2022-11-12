# Day 19 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Instances, State and Higher Order Functions - Turtle Race

# Importing blah blah
from turtle import Turtle, Screen
import random

# Kill switch
is_race_on = False

# Setting screen instances
screen = Screen()
screen.setup(width=500, height=400)

# User input
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

# Colors and starting positions for turtle instances
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]

# Empty list to fill with turtle instances upon creation
all_turtles = []

# Creation and positioning for 7 turtles
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# On button
if user_bet:
    is_race_on = True

# While loop logic
while is_race_on:

    # First turtle to cross 230 wins - flicks the kill switch - prints win/loss statement.
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        # Turle pacing logic
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Exit on click
screen.exitonclick()