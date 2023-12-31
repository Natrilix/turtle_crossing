from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    score = 1
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-275, 250)
        self.color('black')
        self.hideturtle()

    def display_score(self):
        self.write(arg=f'Level {self.score}', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg='GAME OVER', align='center', font=FONT)

    def new_level(self):
        pass