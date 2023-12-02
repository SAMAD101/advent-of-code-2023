# Trebuchet?!

import re
from typing import List


def find_the_answer(inputs: List[str]) -> int:
    sum: int = 0
    dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "zero": "0"}
    for string in inputs:
        matches = re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine|zero)', string)
        if(matches[0] in dict):
            matches[0] = dict[matches[0]]
        if(matches[-1] in dict):
            matches[-1] = dict[matches[-1]]
        sum += int(matches[0] + matches[-1])

    return sum

if(__name__=='__main__'):
    inputs = []
    with open("inputs.txt", "r") as f:
        for line in f:
            inputs.append(line.strip())

    print(find_the_answer(inputs))