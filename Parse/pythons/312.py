import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_first_two_rows(grid: np.ndarray) -> np.ndarray:
    pattern = grid[:2, :]
    out = np.tile(pattern, (grid.shape[0] // pattern.shape[0], 1))
    return out

def fill_grid_with_pattern(output_grid: np.ndarray, pattern: np.ndarray) -> np.ndarray:
    out = np.tile(pattern, (output_grid.shape[0] // pattern.shape[0], output_grid.shape[1] // pattern.shape[1]))
    return out

def select_square(grid: np.ndarray, len: int) -> np.ndarray:
    return grid[:len, 1:len + 1]

def count_colors(grid: np.ndarray) -> int:
    return len(np.unique(grid))

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.zeros_like(input_grid)
    color_num = count_colors(input_grid)
    len = color_num - 1
    pattern = select_square(input_grid, len)
    grid1 = fill_grid_with_pattern(output_grid, pattern)
    output_grid = fill_first_two_rows(grid1)
    return output_grid