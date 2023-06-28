import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def cut_three_by_three(inner_grid: np.ndarray) -> np.ndarray:
    return inner_grid[:3, :3]

def cut_six_by_six(input_grid: np.ndarray, row: int, col: int) -> np.ndarray:
    return input_grid[row:row + 6, col:col + 6]

def find_smallest_col(input_grid: np.ndarray) -> int:
    for i in range(input_grid.shape[1]):
        if not np.all(input_grid[:, i] == black):
            return i
    return input_grid.shape[1]

def find_smallest_row(input_grid: np.ndarray) -> int:
    for i in range(input_grid.shape[0]):
        if not np.all(input_grid[i] == black):
            return i
    return input_grid.shape[0]

def main(input_grid: np.ndarray) -> np.ndarray:
    smallest_row = find_smallest_row(input_grid)
    smallest_col = find_smallest_col(input_grid)
    inner_grid = cut_six_by_six(input_grid, smallest_row, smallest_col)
    output = cut_three_by_three(inner_grid)
    return output