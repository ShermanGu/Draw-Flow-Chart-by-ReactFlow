import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def update_rightmost_column(input_grid: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    non_black_rows = np.where(input_grid[:, -1] != black)[0]
    output_grid[non_black_rows, -1] = input_grid[non_black_rows, -1]
    return output_grid

def deep_copy(input_grid: np.ndarray) -> np.ndarray:
    return np.copy(input_grid)

def find_non_black_rows(input_grid: np.ndarray) -> List[int]:
    rows_index = np.where(np.any(input_grid != black, axis=1))[0]
    return rows_index.tolist()

def main(input_grid: np.ndarray) -> np.ndarray:
    rows_index = find_non_black_rows(input_grid)
    mod_rows_index = rows_index[:-1]
    output_grid = deep_copy(input_grid)
    output_grid[mod_rows_index, 1:] = input_grid[mod_rows_index, :-1]
    output_grid = update_rightmost_column(input_grid, output_grid)
    return output_grid