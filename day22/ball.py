# Day 22 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Build Pong: The Famous Arcade Game - Ball class
 
from turtle import Turtle

class Ball(Turtle):

    def __init__ (self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)