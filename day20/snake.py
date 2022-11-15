# Day 20 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Build the Snake Game Part 1: Animation and Coordinates - Snake class
 
# What are ya' importing?
from turtle import Turtle

# Create constants so it's easy to refer to and update game mechanics
# 3 snake segments/body
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
# Direction bindings
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Create the class
class Snake:

    # __init__, innit?
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create/shape/design snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Chain the segments together and make them follow the head.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Movement/directions bindings with logic to prevent doubling back on one's self
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
