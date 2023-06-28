import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_last_element_with_grey(output_grid: np.ndarray, i: int, col: int) -> np.ndarray:
    if (i - col) % 4 == 3:
        output_grid[-1, i] = grey
    return output_grid

def replace_odd_column_with_grey(output_grid: np.ndarray, i: int, col: int) -> np.ndarray:
    if (i - col) % 4 == 1:
        output_grid[0, i] = grey
    return output_grid

def replace_even_column_with_element(output_grid: np.ndarray, i: int, col: int, ele: int) -> np.ndarray:
    if (i - col) % 2 == 0:
        output_grid[:, i] = ele
    return output_grid

def find_non_zero_element(input_grid: np.ndarray) -> Tuple[int, int]:
    non_zero_indices = np.nonzero(input_grid)
    return (non_zero_indices[1][0], input_grid[non_zero_indices][0])

def create_black_grid(input_grid: np.ndarray) -> np.ndarray:
    return np.zeros_like(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = create_black_grid(input_grid)
    (col, ele) = find_non_zero_element(input_grid)
    for i in range(input_grid.shape[1]):
        if i >= col:
            output_grid = replace_even_column_with_element(output_grid, i, col, ele)
            output_grid = replace_odd_column_with_grey(output_grid, i, col)
            output_grid = replace_last_element_with_grey(output_grid, i, col)
    return output_grid