import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def copy_non_black_pixels(output_grid: np.ndarray, grid: np.ndarray) -> np.ndarray:
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != black:
                output_grid[i, j] = grid[i, j]
    return output_grid

def divide_grid_by_red_columns(grid: np.ndarray) -> List[np.ndarray]:
    divided_grids = []
    start_col = 0
    for j in range(grid.shape[1]):
        if np.all(grid[:, j] == red):
            divided_grids.append(grid[:, start_col:j])
            start_col = j + 1
    divided_grids.append(grid[:, start_col:])
    return divided_grids[:-1][::-1]

def main(input_grid: np.ndarray) -> np.ndarray:
    input_grid = np.concatenate((input_grid, np.array([[2], [2], [2], [2]])), axis=1)
    divided_grids = divide_grid_by_red_columns(input_grid)
    output_grid = np.zeros((4, 4))
    for grid in divided_grids:
        output_grid = copy_non_black_pixels(output_grid, grid)
    return output_grid