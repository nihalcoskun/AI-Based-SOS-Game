Overview

This project is a Python-based implementation of a strategic game involving two players. The game utilizes a board where players make moves and try to outsmart each other. It's built with extensibility and modular design in mind, using classes and data structures for efficient gameplay.

Features

Game Board Customization: Customizable board size for varied levels of play.

Player Types: Supports different player types including user-controlled, random, and AI players (using the MiniMax Alpha Beta algorithm).

Scoring System: Implements a scoring system to track players' performance.

Interactive User Interface: Command-line interface for user inputs and game interaction.

Usage

After starting the game, follow the on-screen prompts to:

-Choose player types.

-Make moves on the board.

-View the game board and scores after each move.

How to Play

-Players take turns to place either an 'S' or an 'O' on the board.

-The objective is to form the sequence 'SOS' horizontally, vertically, or diagonally.

-Each time 'SOS' is formed, the player earns a point.

Code Structure

main.py: The entry point of the game. Handles user interactions and game setup.

game.py: Defines the Game class to manage game states and rules.

game_board.py: Contains the GameBoard class for board representation and manipulation.

players.py: Defines player classes including AbstractPlayer and specific player types.

utils.py: Utility classes and enums like Location, Move, and Sign.

Requirements

Python 3.x
