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
        first = None
        last = None
        while(True):
            match = re.search(r'\d|one|two|three|four|five|six|seven|eight|nine', string)
            if(match):
                if not first:
                    first = match.group(0)
                    string = string[match.end():]
                    continue
                last = match.group(0)
                string = string[match.end():]
            else:
                break
        if last is None: last = first
        if first in NUMS_MAP.keys(): first = NUMS_MAP[first]
        if last in NUMS_MAP.keys(): last = NUMS_MAP[last]
        sum += int(first + last)

    return sum

if(__name__=='__main__'):
    inputs = []
    with open("inputs.txt", "r") as f:
        for line in f:
            inputs.append(line.strip())

    print(find_the_answer(inputs))