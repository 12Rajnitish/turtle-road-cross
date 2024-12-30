# Importing necessary module from turtle for scoreboard
from turtle import Turtle

# Constants for scoreboard font style
FONT = ("Courier", 18, "normal")  # Font for displaying the level and game over text

# Scoreboard class to manage the game's score and display
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.clear()  # Clear any existing writing on the screen
        self.up()  # Lift the pen to avoid drawing lines
        self.level = 1  # Initial level
        self.ht()  # Hide the turtle cursor
        self.goto(-280, 260)  # Position the scoreboard at the top left of the screen
        self.update_scoreboard()  # Update the scoreboard with the initial level

    # Method to update the scoreboard display
    def update_scoreboard(self):
        self.clear()  # Clear previous text
        self.write(f"Level :{self.level}", align='left', font=FONT)  # Display current level

    # Method to increase the level
    def increase_level(self):
        self.level += 1  # Increment the level by 1
        self.update_scoreboard()  # Update the scoreboard after the level increase

    # Method to display "Game Over" message
    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("Game Over!", align='center', font=FONT)  # Display the game over message
