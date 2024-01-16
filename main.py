import math

from game import Game
from game_board import GameBoard
from players import AbstractPlayer, PlayerType

PLAYER_TYPE_MESSAGE = """1. User Player
2. Random Player
3. MiniMax Alpha Beta Player
"""


def _create_game_board():
    return GameBoard(size=5)


def _select_player_type():
    while True:
        try:
            return PlayerType(int(input(PLAYER_TYPE_MESSAGE)))
        except ValueError as e:
            print(e)


def _input_depth(game_board: GameBoard):
    while True:
        try:
            depth_str = input("Input depth for MiniMax Alpha Beta player (Optional): ")
            if depth_str:
                depth = int(depth_str)
            else:
                depth = int(math.log(game_board.get_size(), 2))

            return depth
        except ValueError as e:
            print(e)
            continue


def _select_player(game_board: GameBoard):
    player_type = _select_player_type()
    player_kwargs = {}
    if player_type == PlayerType.USER_PLAYER:
        player_name = input("Enter the name for the User Player: ")
        player_kwargs['name'] = player_name
    elif player_type == PlayerType.MINIMAX_PLAYER_Alpha_Beta:
        player_kwargs["depth"] = _input_depth(game_board)

    return AbstractPlayer.create(player_type=player_type, **player_kwargs)

def main():
    game_board = _create_game_board()
    print("Choose the First Player Type:")
    player_1 = _select_player(game_board)
    print("Choose the Second Player Type:")
    player_2 = _select_player(game_board)
    Game(player_1=player_1, player_2=player_2, game_board=game_board).run()


if __name__ == "__main__":
    main()
