import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_diagonal_pixels(input_grid: np.ndarray, c: int) -> np.ndarray:
    not_black_indices = np.where(input_grid != black)
    not_black_pixel = (not_black_indices[0][0], not_black_indices[1][0])
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if i + j == not_black_pixel[0] + not_black_pixel[1] or i - j == not_black_pixel[0] - not_black_pixel[1]:
                input_grid[i][j] = c
    return input_grid

def get_not_black_color(input_grid: np.ndarray) -> int:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                return input_grid[i][j]
    return black

def main(input_grid: np.ndarray) -> np.ndarray:
    c = get_not_black_color(input_grid)
    out = color_diagonal_pixels(input_grid, c)
    return out