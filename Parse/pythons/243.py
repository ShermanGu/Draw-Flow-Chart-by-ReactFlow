import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def does_not_meet_other_color(row, len, color):
    return row[len] == color

def flip_grid_left_right(grid: np.ndarray) -> np.ndarray:
    return np.fliplr(grid)

def get_input_coordinate(i, j, len):
    return (i * (len + 1), j * (len + 1))

def find_square_side_length(row):
    (len, color) = (0, row[0])
    while does_not_meet_other_color(row, len, color):
        len += 1
    return len

def main(input_grid: np.ndarray) -> np.ndarray:
    square_side_length = find_square_side_length(input_grid[0])
    output_len = input_grid.shape[0] // square_side_length
    output_grid = np.zeros((output_len, output_len), dtype=int)
    for i in range(output_len):
        for j in range(output_len):
            (x, y) = get_input_coordinate(i, j, square_side_length)
            output_grid[i][j] = input_grid[x][y]
    return flip_grid_left_right(output_grid)