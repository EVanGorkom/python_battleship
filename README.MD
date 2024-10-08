# Battleship

## Overview

This is a Python implementation of the classic game **Battleship**, where a player competes against a computer to sink each other's fleet of ships. The game is played in the terminal, and the player is prompted to place ships and take turns firing at the opponent.

## Game Rules

- Both players (you and the computer) have a grid representing their fleet's positions.
- Each player takes turns firing at the opponent's grid, trying to hit and sink their ships.
- The game ends when all ships of either player are sunk.

## Features

- **Place Ships:** You can place your ships on the board with a valid coordinate input.
- **Computer Opponent:** The computer randomly places its ships and fires at your board.
- **Game Over Check:** The game checks if all ships of a player have been sunk to determine the winner.
- **Visual Rendering:** The board is rendered in the terminal with marks for hits, misses, and ships.

## How to Play

1. Clone this repository:
    ```bash
    git clone https://github.com/EVanGorkom/python_battleship
    cd battleship-python
    ```

2. Install required dependencies (if any).

3. Run the game:
    ```bash
    python3 game.py
    ```

4. Follow the prompts in the terminal:
    - **Place ships:** Enter coordinates for where you'd like to place each of your ships.
    - **Take turns:** Enter coordinates to fire at the enemy's board.
    - The game will end when either player's fleet is fully destroyed.

## Example Gameplay

```
Welcome to BATTLESHIP soldier!
Press 'p' to Play. 
Press 'q' to Quit.

Your opponent has placed their ships. Now it's your turn soldier.
==============Player Board==============
  A B C D
1 * * * *
2 * * * *
3 * * * *
4 * * * *

Where shall we put our Cruiser soldier?
Enter the 3 coordinates you'd like separated with a space.
EX: a2 b2 or A3 A4
```

## Project Structure

- `game.py`: Main game logic.
- `board.py`: Handles the game board and ship placements.
- `cell.py`: Represents each cell in the game board.
- `ship.py`: Defines ships and handles hit detection.
- `lib/`: Folder containing additional modules (Board, Ship, etc.)

## Future Improvements

- Add more ship types (e.g., Battleship, Destroyer).
- Enhance computer AI for ship placement and firing strategies.
- Add saving and loading of game state.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Legal Disclaimer

I do not own Battleship. All ideas, images, and game logic is simply recreated for entertainment and educational purposes.

---

You can modify the "git clone" URL with your actual repository URL if this project is hosted somewhere like GitHub.