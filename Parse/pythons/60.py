import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_square_region_with_pattern(input_grid: np.ndarray, pattern_grid: np.ndarray, i: int, j: int) -> np.ndarray:
    d = pattern_grid.shape[0]
    input_grid[i + 1:i + d + 1, j + 1:j + d + 1] = pattern_grid
    return input_grid

def set_row_col_to_blue(input_grid: np.ndarray, i: int, j: int) -> np.ndarray:
    input_grid[i, :] = blue
    input_grid[:, j] = blue
    return input_grid

def no_black_pixel(pattern_grid: np.ndarray) -> bool:
    return not np.any(pattern_grid == black)

def get_square_region(input_grid: np.ndarray, d: int, i: int, j: int) -> np.ndarray:
    return input_grid[i + 1:i + d + 1, j + 1:j + d + 1]

def get_output_grid(input_grid: np.ndarray, pattern_grid: np.ndarray, d: int) -> np.ndarray:
    for i in range(0, input_grid.shape[0], d + 1):
        for j in range(0, input_grid.shape[1], d + 1):
            input_grid = set_row_col_to_blue(input_grid, i, j)
            input_grid = replace_square_region_with_pattern(input_grid, pattern_grid, i, j)
    return input_grid

def get_pattern_grid(input_grid: np.ndarray, d: int) -> np.ndarray:
    for i in range(0, input_grid.shape[0], d + 1):
        for j in range(0, input_grid.shape[1], d + 1):
            pattern_grid = get_square_region(input_grid, d, i, j)
            if no_black_pixel(pattern_grid):
                return pattern_grid

def get_distance_between_blue_pixels(input_grid: np.ndarray) -> int:
    d = 0
    blue_found = False
    for i in range(input_grid.shape[1]):
        if input_grid[1][i] == blue:
            if blue_found:
                break
            blue_found = True
        elif blue_found:
            d += 1
    return d

def get_height_width(input_grid: np.ndarray) -> Tuple[int, int]:
    (h, w) = input_grid.shape
    return (h, w)

def main(input_grid: np.ndarray) -> np.ndarray:
    (h, w) = get_height_width(input_grid)
    d = get_distance_between_blue_pixels(input_grid)
    pattern_grid = get_pattern_grid(input_grid, d)
    output_grid = get_output_grid(input_grid, pattern_grid, d)
    return output_grid