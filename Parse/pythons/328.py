import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_middle_column_black(input_grid: np.ndarray) -> np.ndarray:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if j != input_grid.shape[1] // 2:
                input_grid[i][j] = black
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output = color_middle_column_black(input_grid)
    return output