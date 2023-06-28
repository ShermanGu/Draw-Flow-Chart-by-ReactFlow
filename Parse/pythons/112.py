import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def mirror_non_zero_rows(input_grid: np.ndarray, non_zero_rows: List[int]) -> np.ndarray:
    output = input_grid
    output[::-1][non_zero_rows] = input_grid[non_zero_rows]
    return output

def find_non_zero_rows(input_grid: np.ndarray) -> List[int]:
    non_zero_rows = []
    for i in range(input_grid.shape[0]):
        if np.any(input_grid[i]):
            non_zero_rows.append(i)
    return non_zero_rows

def main(input_grid: np.ndarray) -> np.ndarray:
    non_zero_rows = find_non_zero_rows(input_grid)
    output = mirror_non_zero_rows(input_grid, non_zero_rows)
    return output