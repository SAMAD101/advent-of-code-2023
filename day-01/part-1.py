# Trebuchet?!

import re


def find_the_answer(inputs: list) -> int:
    sum = 0
    for string in inputs:
        matches = re.findall(r'\d', string)
        sum += int(matches[0] + matches[-1])

    return sum

if(__name__=='__main__'):
    inputs = []
    with open("inputs.txt", "r") as f:
        for line in f:
            inputs.append(line.strip())

    print(find_the_answer(inputs))

