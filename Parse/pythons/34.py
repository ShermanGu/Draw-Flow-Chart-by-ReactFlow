import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_grid_90_clockwise(grid: np.ndarray) -> np.ndarray:
    return np.rot90(grid, k=-1)

def fill_leftmost_teal_block(grid: np.ndarray, row: int, color: int) -> np.ndarray:
    for i in range(len(grid[row])):
        if grid[row][i] == teal:
            grid[row][i] = color
            break
    return grid

def find_non_black_cells(arr: np.ndarray) -> List[Tuple[int, int]]:
    return [(arr[i], i) for i in range(len(arr)) if arr[i] != black]

def get_first_column(grid: np.ndarray) -> np.ndarray:
    return grid[:, 0]

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.copy(input_grid)
    for i in range(4):
        first_col = get_first_column(output_grid)
        list = find_non_black_cells(first_col)
        for (color, row) in list:
            output_grid = fill_leftmost_teal_block(output_grid, row, color)
        output_grid = rotate_grid_90_clockwise(output_grid)
    return output_grid