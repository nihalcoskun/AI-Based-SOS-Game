from __future__ import annotations

from utils import Location
from utils import Move
from utils import Sign


class GameBoard:
    def __init__(self, size: int = 5):
        self._size = size
        self._board: list[list[Sign]] = self._create_empty_game_board()

    def _sign_to_char(self, sign: Sign) -> str:
        if sign == Sign.LETTER_S:
            return 'S'
        elif sign == Sign.LETTER_O:
            return 'O'
        else:
            return ' '


    def _create_empty_game_board(self) -> list[list[Sign]]:
        board = [[Sign.EMPTY for _ in range(self._size)] for _ in range(self._size)]
        board[0][0] = board[0][-1] = board[-1][0] = board[-1][-1] = Sign.LETTER_S
        return board

    def get_size(self) -> int:
        return self._size

    def get_location_sign(self, location: Location) -> Sign:
        return self._board[location.x][location.y]

    
    def print_game_board(self) -> None:
        sos_sequences = self.identify_sos_sequences()
        print('   ' + '  '.join(str(i) for i in range(self.get_size())))
        for i, row in enumerate(self._board):
            print(i, end=' ')
            for j, space in enumerate(row):
                if (i, j) in [loc for seq in sos_sequences for loc in seq]:
                    print("*", end="")
                print(self._sign_to_char(space), end="")
                if (i, j) in [loc for seq in sos_sequences for loc in seq]:
                    print("*", end="")
                print(" |", end="")
            print("\n")
        print((self.get_size() * 4 + 1) * "—" + "\n")

    def play_move(self, move: Move) -> None:
        self._board[move.location.x][move.location.y] = move.sign

    def get_locations_with_sign(self, sign: Sign):
        return [
            Location(i, j)
            for i, row in enumerate(self._board)
            for j, element in enumerate(row)
            if element == sign
        ]

    def get_empty_locations(self) -> list[Location]:
        return self.get_locations_with_sign(sign=Sign.EMPTY)

    def has_empty_locations(self) -> bool:
        return bool(self.get_empty_locations())

    def get_sos_count(self) -> int:
        sos_count = 0
        for i, row in enumerate(self._board):
            for j, value in enumerate(row):
                if value == Sign.LETTER_O:
                    if j != 0 and j != self.get_size() - 1:
                        if (
                            self._board[i][j + 1] == Sign.LETTER_S
                            and self._board[i][j - 1] == Sign.LETTER_S
                        ):
                            sos_count += 1  # horiz

                    if i != 0 and i != self.get_size() - 1:
                        if (
                            self._board[i + 1][j] == Sign.LETTER_S
                            and self._board[i - 1][j] == Sign.LETTER_S
                        ):
                            sos_count += 1  # vertical

                    if (
                        i != 0
                        and i != self.get_size() - 1
                        and j != 0
                        and j != self.get_size() - 1
                    ):
                        if (
                            self._board[i + 1][j + 1] == Sign.LETTER_S
                            and self._board[i - 1][j - 1] == Sign.LETTER_S
                        ):
                            sos_count += 1  # neg diag

                        if (
                            self._board[i - 1][j + 1] == Sign.LETTER_S
                            and self._board[i + 1][j - 1] == Sign.LETTER_S
                        ):
                            sos_count += 1  # pos diag
        return sos_count

    def is_in_range(self, location: Location) -> bool:
        return 0 <= location.x < self._size and 0 <= location.y < self._size

    def is_almost_sos(self, location: Location) -> bool:
        for i in range(-1, 2):
            for j in range(-1, 2):
                o_pos = Location(location.x + i, location.y + j)
                s_pos = Location(location.x + 2 * i, location.y + 2 * j)
                if self.is_in_range(s_pos):
                    is_soe = (
                        self.get_location_sign(o_pos) == Sign.LETTER_O
                        and self.get_location_sign(s_pos) == Sign.EMPTY
                    )
                    is_ses = (
                        self.get_location_sign(o_pos) == Sign.EMPTY
                        and self.get_location_sign(s_pos) == Sign.LETTER_S
                    )
                    if is_soe or is_ses:
                        return True

        return False

    def identify_sos_sequences(self):
    # Returns a list of tuples, each representing the coordinates of an SOS sequence
        sos_locations = []
        for i in range(self._size):
          for j in range(self._size):
             if self._board[i][j] == Sign.LETTER_S:
                # Check horizontally
                if j <= self._size - 3 and self._board[i][j + 1] == Sign.LETTER_O and self._board[i][j + 2] == Sign.LETTER_S:
                    sos_locations.append(((i, j), (i, j + 1), (i, j + 2)))
                # Check vertically
                if i <= self._size - 3 and self._board[i + 1][j] == Sign.LETTER_O and self._board[i + 2][j] == Sign.LETTER_S:
                    sos_locations.append(((i, j), (i + 1, j), (i + 2, j)))
                # Check diagonally (down-right)
                if i <= self._size - 3 and j <= self._size - 3 and self._board[i + 1][j + 1] == Sign.LETTER_O and self._board[i + 2][j + 2] == Sign.LETTER_S:
                    sos_locations.append(((i, j), (i + 1, j + 1), (i + 2, j + 2)))
                # Check diagonally (up-right)
                if i >= 2 and j <= self._size - 3 and self._board[i - 1][j + 1] == Sign.LETTER_O and self._board[i - 2][j + 2] == Sign.LETTER_S:
                    sos_locations.append(((i, j), (i - 1, j + 1), (i - 2, j + 2)))
        return sos_locations
    
    def move_is_ok(self, move: Move) -> bool:
        if (
            move.location.x >= self._size
            or move.location.y >= self._size
            or move.location.x < 0
            or move.location.y < 0
        ):
            return False

        return self._board[move.location.x][move.location.y] == Sign.EMPTY