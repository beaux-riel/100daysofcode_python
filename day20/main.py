# Day 20 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Build the Snake Game Part 1: Animation and Coordinates - Main

# What ya' importin'?
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Beaux's Snazzy Snake Game")
screen.tracer(0)

# Create snake instance
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Create listener and key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Power button/kill switch
game_is_on = True

# And action!
while game_is_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        
        scoreboard.increase_score()

# Exit game on screen click
screen.exitonclick()


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

    # for seg in segments:
    #     seg.forward(20)