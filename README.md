# Tic-Tac-Toe Game

A simple, text-based Tic-Tac-Toe game built with Python and `numpy`, where two players can take turns to mark spaces on a 3x3 board. The first player to align three of their symbols horizontally, vertically, or diagonally wins the game.

## Game Rules

1. **Player Symbols**: Player 1 is assigned "X" and Player 2 is assigned "O".
2. **Turns**: Players alternate turns, starting with Player 1.
3. **Winning Conditions**: A player wins by placing three of their symbols in a row, column, or diagonal.
4. **Draw**: If all 9 spaces are filled without a winner, the game ends in a draw.

## Features

- **Real-time board display**: The board updates after each turn.
- **Input validation**: Prompts players to re-enter values if the input is invalid or if the space is already taken.
- **Win Checking**: Detects and announces a win or draw.

## Code Structure

- **Board Setup**: A 3x3 grid initialized with `'-'` characters to represent empty spaces.
- **Symbol Placement**: Prompts each player to choose a row and column to place their symbol.
- **Win Checking Functions**:
  - `check_rows()`: Checks if a player has aligned symbols in a row.
  - `check_cols()`: Checks for aligned symbols in a column.
  - `check_diagonals()`: Checks for aligned symbols in a diagonal.
- **Game Control**: The `play()` function manages player turns and checks for win/draw conditions.


## Requirements

- Python 3.x
- numpy library

## Running The Game

Clone the repository : git clone https://github.com/ayush-5158/TicTacToe-Game.git

Install numpy if not already installed : pip install numpy

Run the script : python tictactoe.py

