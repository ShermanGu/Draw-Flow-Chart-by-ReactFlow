import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_combination_array(flip_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    return np.concatenate((flip_grid, input_grid), axis=0)

def flip_up_down(input_grid: np.ndarray) -> np.ndarray:
    return np.flipud(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    flip_grid = flip_up_down(input_grid)
    output = get_combination_array(flip_grid, input_grid)
    return output