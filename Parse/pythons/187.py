import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def split_pattern(input_grid: np.ndarray) -> np.ndarray:
    """
    The input is composed of two same pattern. Try to split the input vertically or horizontally, 
    to see if the two parts are the same. If same, return one pattern.
    """
    (height, width) = input_grid.shape
    if np.array_equal(input_grid[:height // 2, :], input_grid[height // 2:, :]):
        return input_grid[:height // 2, :]
    elif np.array_equal(input_grid[:, :width // 2], input_grid[:, width // 2:]):
        return input_grid[:, :width // 2]
    else:
        return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    pattern = split_pattern(input_grid)
    return pattern