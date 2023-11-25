import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

#Listen for keypresses
screen.onkeypress(player.move, 'Up')

screen.onkeypress(player.quit_game, 'space')


screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    print(player.dummy_variable)
    if player.dummy_variable == False:
        game_is_on = False