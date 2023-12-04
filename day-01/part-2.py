# Trebuchet?!

import re
from typing import List


def find_the_answer(inputs: List[str]) -> int:
    sum: int = 0
    NUMS_MAP = {"one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9"}

    for string in inputs:
        matches = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', string, re.IGNORECASE)
        first = matches[0]
        last = matches[-1]
        if first in NUMS_MAP: first = NUMS_MAP[first]
        if last in NUMS_MAP: last = NUMS_MAP[last]
        sum += int(first + last)

    return sum

if(__name__=='__main__'):
    inputs = []
    with open("input.txt", "r") as f:
        for line in f:
            inputs.append(line.strip())

    print(find_the_answer(inputs))