Turtle Crossing Game

This is a Python-based turtle crossing game built using the 'turtle' graphics library. The game involves controlling a turtle to cross a road filled with moving cars, while avoiding collisions and reaching the finish line.

Features:
- Player Movement: Use the arrow keys to control the turtle’s movement.
- Car Movement: Cars move from right to left and increase speed as the player progresses.
- Leveling System: Each time the player reaches the finish line, the game level increases, and the speed of cars increases.
- Game Over: The game ends if the player collides with a car.

Requirements:
- Python 3.x
- 'turtle' graphics library (should be pre-installed with Python)

Installation:
1. Clone the repository or download the project files.
2. Ensure you have Python 3.x installed on your system.
3. Open the terminal or command prompt and navigate to the project directory.
4. Run the game using the following command:
   python main.py

Game Instructions:
- Press the Up Arrow to move the turtle forward.
- Press the Down Arrow to move the turtle backward.
- Avoid colliding with the cars moving from right to left.
- Reach the finish line to increase your level and the speed of the cars.

Project Structure:
- main.py: The main game loop and screen setup.
- player.py: Contains the Player class for controlling the turtle.
- car_manager.py: Manages car creation, movement, and speed.
- scoreboard.py: Displays the current level and game over message.

License:
This project is open-source and available under the MIT License.
