import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_bottom_left_color_with_black(input_grid: np.ndarray) -> np.ndarray:
    (rows, cols) = input_grid.shape
    input_grid[rows - 1, 0] = black
    return input_grid

def replace_colors(input_grid: np.ndarray) -> np.ndarray:
    (rows, cols) = input_grid.shape
    bottom_left_color = input_grid[rows - 1, 0]
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] != black:
                input_grid[i, j] = bottom_left_color
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    out = replace_colors(input_grid)
    out = replace_bottom_left_color_with_black(out)
    return out