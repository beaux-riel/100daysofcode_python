from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=2, stretch_len=1)
        new_car.penup()
        new_car.color(random.choic(COLORS))
        random_y = random.choice(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)