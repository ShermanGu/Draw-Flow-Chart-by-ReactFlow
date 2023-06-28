import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def copy_to_3x3_grid(input_grid: np.ndarray, output_grid: np.ndarray, i: int, j: int) -> np.ndarray:
    output_grid[3 * i:3 * i + 3, 3 * j:3 * j + 3] = input_grid
    return output_grid

def make_grid() -> np.ndarray:
    return np.zeros((9, 9), dtype=int)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = make_grid()
    for i in range(3):
        for j in range(3):
            if input_grid[i, j] == red:
                output_grid = copy_to_3x3_grid(input_grid, output_grid, i, j)
    return output_grid