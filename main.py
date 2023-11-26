import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player object
player = Player()

# Create the scoreboard object
scoreboard = Scoreboard()

# Create the cars objects
# This will have to move somewhere else when we start doing new levels
cars = []
for i in range(0, 20):
    cars.append(CarManager())

# Assign key-binds and listen for them
screen.onkeypress(player.move, 'Up')
screen.listen()

# Main game loop
# Will have to set up something to call this anew with each new level
game_is_on = True
while game_is_on:
    # Set FPS essentially
    time.sleep(0.1)
    # Display the score, probably don't need this here, could do at level reset
    scoreboard.display_score()
    # Move each car forwards the correct amount for the current level
    for car in cars:
        car.move_car(level=0)
        # And send them back once they go off-screen, to be reused. Saves memory
        if car.xcor() < -350:
            car.reset_car()
        # And detect collisions with the player
        if car.distance(player.position()) < 20:
            scoreboard.game_over()
            game_is_on = False
    # Check if the player has finished the level
    if player.ycor() > 280:
        scoreboard.new_level()
        #To be honest I think most of this will have to be done in main.py
    # Update the new frame to be displayed
    screen.update()

screen.exitonclick()