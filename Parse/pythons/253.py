import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_grey_with_black(input_grid: np.ndarray) -> np.ndarray:
    input_grid[input_grid == grey] = black
    return input_grid

def replace_grey_with_red_in_column(input_grid: np.ndarray, column: int) -> np.ndarray:
    input_grid[:, column][input_grid[:, column] == grey] = red
    return input_grid

def replace_grey_with_blue_in_column(input_grid: np.ndarray, column: int) -> np.ndarray:
    input_grid[:, column][input_grid[:, column] == grey] = blue
    return input_grid

def get_column_with_lowest_nonzero_gray_pixels(input_grid: np.ndarray) -> int:
    gray_pixels_per_column = np.sum(input_grid == grey, axis=0)
    nonzero_gray_pixels_per_column = np.where(gray_pixels_per_column > 0, gray_pixels_per_column, np.inf)
    return np.argmin(nonzero_gray_pixels_per_column)

def get_column_with_highest_gray_pixels(input_grid: np.ndarray) -> int:
    gray_pixels_per_column = np.sum(input_grid == grey, axis=0)
    return np.argmax(gray_pixels_per_column)

def main(input_grid: np.ndarray) -> np.ndarray:
    a = get_column_with_highest_gray_pixels(input_grid)
    b = get_column_with_lowest_nonzero_gray_pixels(input_grid)
    out = replace_grey_with_blue_in_column(input_grid, a)
    out = replace_grey_with_red_in_column(out, b)
    out = replace_grey_with_black(out)
    return out