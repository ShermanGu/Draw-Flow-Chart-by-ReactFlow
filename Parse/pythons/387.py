import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_black_with_teal_in_index_column(index: List[int], grid: np.ndarray) -> np.ndarray:
    for i in index:
        for j in range(grid.shape[0]):
            if grid[j][i] == black:
                grid[j][i] = teal
    return grid

def find_non_black_columns(grid: np.ndarray) -> List[int]:
    non_black_columns = []
    for i in range(grid.shape[1]):
        if not np.all(grid[:, i] == black):
            non_black_columns.append(i)
    return non_black_columns

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.concatenate((input_grid, input_grid), axis=0)
    output_grid = np.concatenate((output_grid, output_grid), axis=1)
    index = find_non_black_columns(output_grid)
    output_grid = replace_black_with_teal_in_index_column(index, output_grid)
    return output_grid