import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def count_non_black_pixels(input_grid: np.ndarray) -> int:
    return np.count_nonzero(input_grid != black)

def main(input_grid: np.ndarray) -> np.ndarray:
    num_non_black = count_non_black_pixels(input_grid)
    output_grid = np.zeros_like(input_grid)
    if num_non_black <= 3:
        output_grid[0, :num_non_black] = red
    else:
        output_grid[0, :] = red
        output_grid[1, 1] = red
    return output_grid