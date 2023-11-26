from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#move increment is the amount move should increase on a new level


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(180)
        self.penup()
        self.goto(random.randint(300, 1000), random.randint(-220, 260))
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(0.5, 1)

    def move_car(self, level):
        self.forward(STARTING_MOVE_DISTANCE+MOVE_INCREMENT*level)

    def reset_car(self):
        self.goto(random.randint(350, 450), random.randint(-200, 280))