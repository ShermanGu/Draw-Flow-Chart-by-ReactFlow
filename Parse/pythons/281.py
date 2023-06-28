import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_positions_to_black(input: List[List[int]], positions: List[Tuple[int, int]]) -> List[List[int]]:
    for (i, j) in positions:
        input[i][j] = black
    return input

def change_corners_to_grey(input: List[List[int]], positions: List[Tuple[int, int]]) -> List[List[int]]:
    for (i, j) in positions:
        if i > 0 and j > 0:
            input[i - 1][j - 1] = grey
        if i > 0 and j < len(input[i]) - 1:
            input[i - 1][j + 1] = grey
        if i < len(input) - 1 and j > 0:
            input[i + 1][j - 1] = grey
        if i < len(input) - 1 and j < len(input[i]) - 1:
            input[i + 1][j + 1] = grey
    return input

def change_positions_to_blue(input: List[List[int]], positions: List[Tuple[int, int]]) -> List[List[int]]:
    for (i, j) in positions:
        if i > 0:
            input[i - 1][j] = blue
        if i < len(input) - 1:
            input[i + 1][j] = blue
        if j > 0:
            input[i][j - 1] = blue
        if j < len(input[i]) - 1:
            input[i][j + 1] = blue
    return input

def find_grey_positions(input: List[List[int]]) -> List[Tuple[int, int]]:
    positions = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == grey:
                positions.append((i, j))
    return positions

def main(input):
    positions = find_grey_positions(input)
    output = change_positions_to_blue(input, positions)
    output = change_corners_to_grey(output, positions)
    output = change_positions_to_black(output, positions)
    return output