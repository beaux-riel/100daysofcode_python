# Day 22 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Build Pong: The Famous Arcade Game - Main


from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Revival")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

# Exit game on screen click
screen.exitonclick()