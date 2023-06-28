import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def mirror_image(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function draws a mirror image of the upper half grid on the middle row axis in the lower half grid,
    and draws a mirror image of the left half grid on the middle column axis in the right half grid.
    It returns the modified grid.
    """
    middle_row = input_grid.shape[0] // 2
    middle_col = input_grid.shape[1] // 2
    upper_half = input_grid[:middle_row, :]
    lower_half = input_grid[middle_row:, :]
    lower_half[:middle_row, :] = np.flip(upper_half, axis=0)
    left_half = input_grid[:, :middle_col]
    right_half = input_grid[:, middle_col:]
    right_half[:, :middle_col] = np.flip(left_half, axis=1)
    return input_grid

def delete_middle_row_and_column(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function deletes the middle row and middle column of the grid.
    It returns the modified grid.
    """
    middle_row = input_grid.shape[0] // 2
    middle_col = input_grid.shape[1] // 2
    output_grid = np.delete(input_grid, middle_row, axis=0)
    output_grid = np.delete(output_grid, middle_col, axis=1)
    return output_grid

def replace_not_black_with_color(input_grid: np.ndarray, c: int) -> np.ndarray:
    """
    Given an input grid and a color c, this function replaces all the non-black cells in the grid with the color c.
    It returns the modified grid.
    """
    not_black = input_grid != black
    input_grid[not_black] = c
    return input_grid

def get_middle_row_color(input_grid: np.ndarray) -> int:
    return input_grid[input_grid.shape[0] // 2][0]

def main(input_grid: np.ndarray) -> np.ndarray:
    c = get_middle_row_color(input_grid)
    t = replace_not_black_with_color(input_grid, c)
    d = delete_middle_row_and_column(t)
    out = mirror_image(d)
    return out