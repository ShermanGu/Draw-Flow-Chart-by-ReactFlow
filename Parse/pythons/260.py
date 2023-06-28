import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_teal_pixels_red(input_grid: np.ndarray) -> np.ndarray:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == teal:
                input_grid[i][j] = red
    return input_grid

def move_non_black_pixels_to_next_row(input_grid: np.ndarray) -> np.ndarray:
    for i in range(input_grid.shape[0] - 2, -1, -1):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black and input_grid[i + 1][j] == black:
                input_grid[i + 1][j] = input_grid[i][j]
                input_grid[i][j] = black
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    input_grid = move_non_black_pixels_to_next_row(input_grid)
    input_grid = make_teal_pixels_red(input_grid)
    return input_grid