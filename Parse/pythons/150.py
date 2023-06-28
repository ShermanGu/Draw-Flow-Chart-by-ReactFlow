import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_non_black_pixel_in_first_row(input_grid: np.ndarray) -> int:
    for i in range(input_grid.shape[1]):
        if input_grid[0][i] != black:
            return i
    return -1

def find_non_black_pixel_in_first_column(input_grid: np.ndarray) -> int:
    for i in range(input_grid.shape[0]):
        if input_grid[i][0] != black:
            return i
    return -1

def color_adjacent_pixels_yellow(input_grid: np.ndarray, x: int, y: int) -> np.ndarray:
    for i in range(max(0, x - 1), min(input_grid.shape[0], x + 2)):
        for j in range(max(0, y - 1), min(input_grid.shape[1], y + 2)):
            if i != x or j != y:
                input_grid[i][j] = yellow
    return input_grid

def find_intersection(input_grid: np.ndarray) -> Tuple[int, int]:
    x = find_non_black_pixel_in_first_column(input_grid)
    y = find_non_black_pixel_in_first_row(input_grid)
    return (x, y)

def main(input_grid: np.ndarray) -> np.ndarray:
    (x, y) = find_intersection(input_grid)
    output = color_adjacent_pixels_yellow(input_grid, x, y)
    return output