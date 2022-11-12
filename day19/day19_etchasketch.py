# Day 19 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Instances, State and Higher Order Functions - Etch-a-sketch Exercise

# Imports ya' stuffs
from turtle import Turtle, Screen

# Beaux-turtle and screen object creation
beaux = Turtle()
screen = Screen()

# Setup my functions
def move_forwards():
    beaux.forward(10)

def move_backwards():
    beaux.backward(10)

def turn_left():
    new_heading = beaux.heading() + 10
    beaux.setheading(new_heading)

def turn_right():
    new_heading = beaux.heading() - 10
    beaux.setheading(new_heading)

def clear():
    beaux.clear()
    beaux.penup()
    beaux.home()
    beaux.pendown()

# Create listeners
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()