# Importing necessary module from turtle for player creation
from turtle import Turtle

# Constants for player movement and finish line position
STARTING_POSITION = (0, -280)  # Starting position of the player (turtle)
MOVE_DISTANCE = 10  # Distance the player moves each time
FINISH_LINE_Y = 270  # Y-coordinate of the finish line

# Player class that inherits from Turtle class
class Player(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.penup()  # Lift the pen to avoid drawing lines
        self.shape('turtle')  # Set the shape of the player as a turtle
        self.color('red', 'green')  # Set the player's color
        self.seth(90)  # Set the player's orientation (90 degrees, facing upward)
        self.goto_start()  # Position the player at the starting point

    # Move the player forward
    def move_fd(self):
        self.fd(MOVE_DISTANCE)

    # Move the player backward
    def move_bk(self):
        self.bk(MOVE_DISTANCE)

    # Check if the player has reached the finish line
    def is_at_finishline(self):
        return self.ycor() >= FINISH_LINE_Y

    # Reset the player's position to the start
    def goto_start(self):
        self.goto(STARTING_POSITION)
