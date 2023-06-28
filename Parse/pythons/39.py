import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_colors_in_rows(input_grid: np.ndarray, a: int, b: int) -> np.ndarray:
    input_grid[0:5, :][input_grid[0:5, :] != black] = a
    input_grid[-5:, :][input_grid[-5:, :] != black] = b
    return input_grid

def get_first_and_last_pixels_in_first_column(input_grid: np.ndarray) -> Tuple[int, int]:
    return (input_grid[0][0], input_grid[-1][0])

def replace_colors_in_columns(input_grid: np.ndarray, a: int, b: int) -> np.ndarray:
    input_grid[:, :5][input_grid[:, :5] != black] = a
    input_grid[:, -5:][input_grid[:, -5:] != black] = b
    return input_grid

def get_first_and_last_pixels_in_first_row(input_grid: np.ndarray) -> Tuple[int, int]:
    return (input_grid[0][0], input_grid[0][-1])

def is_first_column_not_black(input_grid: np.ndarray) -> bool:
    return not np.all(input_grid[:, 0] == black)

def main(input_grid: np.ndarray) -> np.ndarray:
    flag = is_first_column_not_black(input_grid)
    if flag:
        (a, b) = get_first_and_last_pixels_in_first_row(input_grid)
        out = replace_colors_in_columns(input_grid, a, b)
    else:
        (a, b) = get_first_and_last_pixels_in_first_column(input_grid)
        out = replace_colors_in_rows(input_grid, a, b)
    return out