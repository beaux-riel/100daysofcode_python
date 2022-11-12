# Day 20 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Build the Snake Game Part 1: Animation and Coordinates

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Beaux's Snazzy Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)



game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments:
    #     seg.forward(20)
    
    for seg_num in range(start=2, stop=0, step=-1):
    segments[seg_num]

# Left the below code in for reference's sake

# segment_1 = Turtle("square")
# segment_1.color("white")
# segment_1.goto(x=-20, y=0)

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(x=-20, y=0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(x=-40, y=0)

screen.exitonclick()