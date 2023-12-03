# Cube Conundrum

import re
from typing import List
import numpy as np


def get_possible_games(inputs: List[str]) -> int:
    possible_games: int = 0
    for string in inputs:
        if is_valid_game(string):
            possible_games += int(re.search(r'[0-9]+', string).group(0))

    return possible_games


def is_valid_game(game: str) -> bool:
    POSSIBLE_GAME_CONFIGURATIONS = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    sets = game.split("; ")
    sets[0] = sets[0].split(": ")
    sets.insert(1, sets[0][1])
    sets.pop(0)

    combinations = [{re.search(r'[a-z]+', color).group(0): int(re.search(r'[0-9]+', color).group(0)) for color in
                       set.split(", ") for set in sets} for set in sets]

    for combination in combinations:
        for key, value in combination.items():
            if value > POSSIBLE_GAME_CONFIGURATIONS[key]:
                print(combination)
                return False

    return True


if __name__ == '__main__':
    inputs = []
    with open("inputs.txt", "r") as f:
        for line in f:
            inputs.append(line.strip())

    print(get_possible_games(inputs))