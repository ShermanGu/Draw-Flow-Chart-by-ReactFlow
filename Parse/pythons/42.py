import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_black_to_red(output: np.ndarray, i: int, j: int) -> None:
    output[i][j] = red

def is_grey_corner(input_grid: np.ndarray, i: int, j: int) -> bool:
    return input_grid[0][j] == grey and input_grid[i][input_grid.shape[1] - 1] == grey

def copy_array(input_grid: np.ndarray) -> np.ndarray:
    return np.copy(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output = copy_array(input_grid)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if is_grey_corner(input_grid, i, j):
                change_black_to_red(output, i, j)
    return output