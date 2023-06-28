import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_grey_area_with_non_grey_area(input_grid):
    (rows, cols) = input_grid.shape
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, -1, -1):
            if input_grid[i][j] != black and input_grid[i][j] != grey:
                non_grey_position = (i, j)
                break
        else:
            continue
        break
    return non_grey_position

def find_first_non_black_or_grey_position(input_grid):
    (rows, cols) = input_grid.shape
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] != black and input_grid[i][j] != grey:
                return (i, j)
    return None

def has_grey_color(input_grid):
    (rows, cols) = input_grid.shape
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == grey:
                return True
    return False

def find_grey_position(input_grid):
    (rows, cols) = input_grid.shape
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == grey:
                return (i, j)
    return None

def find_positions(input):
    p1 = find_first_non_black_or_grey_position(input)
    p2 = replace_grey_area_with_non_grey_area(input)
    return [p1, p2]

def main(input_grid):
    input = input_grid
    positions = find_positions(input)
    while True:
        grey_position = find_grey_position(input)
        x = positions[1][0] - positions[0][0] + 1
        y = positions[1][1] - positions[0][1] + 1
        input[grey_position[0]:grey_position[0] + x, grey_position[1]:grey_position[1] + y] = input[positions[0][0]:positions[1][0] + 1, positions[0][1]:positions[1][1] + 1]
        if not has_grey_color(input):
            break
    return input