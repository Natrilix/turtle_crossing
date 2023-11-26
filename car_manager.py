from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#move increment is the amount move should increase on a new level


class CarManager(Turtle):
    move_distance = STARTING_MOVE_DISTANCE
    def __init__(self):
        super().__init__()
        self.setheading(180)
        self.penup()
        self.goto(random.randint(300, 500), random.randint(-200, 280))
        self.color(random.choice(COLORS))

    def move_car(self):
        self.forward(self.move_distance)
        pass

    def reset_car(self):
        car.goto(random.randint(350, 450), random.randint(-200, 280))