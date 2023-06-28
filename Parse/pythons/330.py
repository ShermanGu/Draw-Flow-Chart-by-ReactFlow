import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_colors(grid: np.ndarray, i: int, j: int) -> None:
    if i > 0:
        grid[i - 1][j] = red
    if j > 0:
        grid[i][j - 1] = orange
    if j < grid.shape[1] - 1:
        grid[i][j + 1] = pink
    if i < grid.shape[0] - 1:
        grid[i + 1][j] = teal

def main(input_grid: np.ndarray) -> np.ndarray:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                paint_colors(input_grid, i, j)
    return input_grid