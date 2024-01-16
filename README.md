Overview

This project presents an advanced Python-based strategic game that prominently features Artificial Intelligence (AI) elements in gameplay. At its core, the game is a tactical battle of wits between two players on a customizable game board. What makes this project stand out is its integration of various AI algorithms, notably the MiniMax Alpha Beta algorithm.

The game offers three distinct player types: a user-controlled player for those who prefer a hands-on approach, a randomly acting player for an element of unpredictability, and an AI player that uses sophisticated algorithms to make strategic decisions. This AI player is not just a static opponent; it's designed to adapt its strategy based on the game's progress, making each session unique and challenging.

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
