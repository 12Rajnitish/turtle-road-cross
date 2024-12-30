# Importing necessary modules
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)  # Set the screen dimensions
screen.tracer(0)  # Turn off automatic screen updates to manually control the updates

# Creating objects for player, car manager, and scoreboard
my_turtle = Player()
car_manager = CarManager()
score = Scoreboard()

# Listening for keypress events to control the player movement
screen.listen()
screen.onkeypress(fun=my_turtle.move_fd, key='Up')  # Move forward when the 'Up' key is pressed
screen.onkeypress(fun=my_turtle.move_bk, key='Down')  # Move backward when the 'Down' key is pressed

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Slow down the game loop for smooth gameplay
    screen.update()  # Update the screen to reflect changes

    # Create new cars and move existing ones
    car_manager.create_car()
    car_manager.move_car()

    # Check for collision with cars
    for car in car_manager.all_cars:
        if car.distance(my_turtle) < 20:
            game_is_on = False
            score.game_over()

    # Check if the player has reached the finish line
    if my_turtle.is_at_finishline():
        my_turtle.goto_start()
        car_manager.level_up()
        score.increase_level()
        car_manager.increase_cars()

screen.exitonclick()  # Close the screen on click
