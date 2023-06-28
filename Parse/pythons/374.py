import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_diagonal_lines_black(input_grid: np.ndarray) -> np.ndarray:
    output = np.copy(input_grid)
    n = input_grid.shape[0]
    for i in range(n):
        output[i, i] = black
        output[i, n - i - 1] = black
    return output

def main(input_grid: np.ndarray) -> np.ndarray:
    output = color_diagonal_lines_black(input_grid)
    return output