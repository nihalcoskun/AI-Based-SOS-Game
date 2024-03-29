from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


@dataclass
class Location:
    x: int
    y: int



@dataclass
class Move:
    location: Location
    sign: Sign



class Sign(str, Enum):
    LETTER_S = "S"
    LETTER_O = "O"
    EMPTY = "_"

    @classmethod
    def get_input_valid_signs(cls) -> list[Sign]:
        return [cls.LETTER_S, cls.LETTER_O]

    @classmethod
    def from_user_input(cls, s: str) -> Sign:
        if Sign(s) not in cls.get_input_valid_signs():
            raise ValueError("Invalid input")

        return cls(s)