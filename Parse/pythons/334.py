import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_black_pixels_with_yellow_in_column(input_grid: np.ndarray, x1: int, x2: int, y1: int) -> np.ndarray:
    for i in range(x1, x2 + 1):
        if input_grid[i][y1] == black:
            input_grid[i][y1] = yellow
    return input_grid

def replace_black_pixels_with_yellow(input_grid: np.ndarray, y1: int, y2: int, x2: int) -> np.ndarray:
    for j in range(y1, y2 + 1):
        if input_grid[x2][j] == black:
            input_grid[x2][j] = yellow
    return input_grid

def get_min_max(x: int, y: int) -> Tuple[int, int]:
    return (min(x, y), max(x, y))

def find_red_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                return (i, j)

def find_teal_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == teal:
                return (i, j)

def main(input_grid: np.ndarray) -> np.ndarray:
    (x1, y1) = find_teal_pixel(input_grid)
    (x2, y2) = find_red_pixel(input_grid)
    (a1, a2) = get_min_max(x1, x2)
    (b1, b2) = get_min_max(y1, y2)
    out = replace_black_pixels_with_yellow(input_grid, b1, b2, x2)
    out = replace_black_pixels_with_yellow_in_column(out, a1, a2, y1)
    return out