# Cube Conundrum

import re
from typing import List
import numpy as np


def get_total_power_product(inputs: List[str]) -> int:
    total_power_product: int = 0
    for string in inputs:
        total_power_product += get_power_product(string)

    return total_power_product


def get_power_product(game: str) -> bool:
    POSSIBLE_GAME_CONFIGURATION = {
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

    mred, mgreen, mblue = 1, 1, 1
    for item in combinations:
        for key, value in item.items():
            if (key == 'red') and value > mred:
                mred = value
            elif (key == 'green') and value > mgreen:
                mgreen = value
            elif (key == 'blue') and value > mblue:
                mblue = value

    return (mred*mgreen*mblue)


if __name__ == '__main__':
    inputs = []
    with open("input.txt", "r") as f:
        for line in f:
            inputs.append(line.strip())

    print(get_total_power_product(inputs))