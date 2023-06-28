import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_left_pixels_in_line_i_with_a(input_grid: np.ndarray, i: int, m: int, a: int) -> np.ndarray:
    out = input_grid.copy()
    out[i, :m] = a
    return out

def replace_pixels_in_line_i_with_a(input_grid: np.ndarray, i: int, n: int, a: int) -> np.ndarray:
    m = i + n
    out = replace_left_pixels_in_line_i_with_a(input_grid, i, m, a)
    return out

def get_height(input_grid: np.ndarray) -> int:
    return input_grid.shape[0]

def count_pixels_of_color_a_in_first_row(input_grid: np.ndarray, a: int) -> int:
    return np.count_nonzero(input_grid[0] == a)

def get_first_pixel_color(input_grid: np.ndarray) -> int:
    return input_grid[0][0]

def copy_first_row_to_all_rows(input_grid: np.ndarray) -> np.ndarray:
    return np.array([input_grid[0]] * input_grid.shape[0])

def expand_height(input_grid: np.ndarray, h: int) -> np.ndarray:
    return np.pad(input_grid, ((0, h - input_grid.shape[0]), (0, 0)))

def get_half_width(input_grid: np.ndarray) -> int:
    return input_grid.shape[1] // 2

def main(input_grid: np.ndarray) -> np.ndarray:
    h = get_half_width(input_grid)
    out = expand_height(input_grid, h)
    out = copy_first_row_to_all_rows(out)
    a = get_first_pixel_color(out)
    n = count_pixels_of_color_a_in_first_row(out, a)
    h = get_height(out)
    for i in range(1, h):
        out = replace_pixels_in_line_i_with_a(out, i, n, a)
    return out