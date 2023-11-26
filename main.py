import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []

#Listen for keypresses
screen.onkeypress(player.move, 'Up')

screen.onkeypress(player.quit_game, 'space')


screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scoreboard.display_score()
    create_car = random.randint(0, 100)
    for i in range(20):
        cars.append(CarManager())
    for car in cars:
        car.move_car()
        if car.xcor() < -350:
            car.reset_car()
    print(len(cars))

    screen.update()
    if player.playing == False:
        game_is_on = False