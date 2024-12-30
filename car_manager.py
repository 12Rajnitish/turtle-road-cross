# Importing necessary modules
from turtle import Turtle
import random as rd

# Constants for car properties
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of car colors
STARTING_MOVE_DISTANCE = 5  # Starting speed of the cars
MOVE_INCREMENT = 5  # Increment in car speed as the game progresses

# CarManager class responsible for managing car creation and movement
class CarManager:

    def __init__(self):
        self.all_cars = []  # List to hold all the cars
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars
        self.random_list = [1, 2, 3, 4, 5, 6]  # List to control the random chance for car creation

    # Method to create a new car with random properties
    def create_car(self):
        random_chance = rd.choice(self.random_list)
        if random_chance == 1:
            new_car = Turtle(shape='square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.up()
            new_car.color(rd.choice(COLORS))
            random_y = rd.randint(-220, 220)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    # Method to move all cars
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Method to increase car speed after each level
    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    # Method to increase the number of cars created
    def increase_cars(self):
        if len(self.random_list) > 1:
            self.random_list = self.random_list[:-1]
