# Day 21 of 100 Days of Code - Python
# https://www.udemy.com/course/100-days-of-code/
# Exercise - Build the Snake Game Part 2: Inheritance and List Slicing - Scoreboard
# Exercise - Build the Snake Game Part 2: Inheritance & List Slicing

# The in bits...
from turtle import Turtle

# Setting my constants
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Creating my scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    # Writes score to screen
    def update_scoreboard(self):
        self.clear()
        self.write(F"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # # Game over message - Center of screen
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER DUDE!", align=ALIGNMENT, font=FONT)
    
    # Increase score by one then update scoreboard
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

