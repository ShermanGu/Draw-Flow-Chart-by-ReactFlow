import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_gray_pixels(input_grid: np.ndarray) -> np.ndarray:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == grey:
                input_grid[i][j] = input_grid[i][0]
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    return paint_gray_pixels(input_grid)