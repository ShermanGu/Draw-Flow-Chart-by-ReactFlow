import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def concatenate_up_down(input_grid: np.ndarray, revert: np.ndarray) -> np.ndarray:
    return np.concatenate((input_grid, revert))

def flip_upside_down(input_grid: np.ndarray) -> np.ndarray:
    return np.flipud(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    revert = flip_upside_down(input_grid)
    output = concatenate_up_down(input_grid, revert)
    return output