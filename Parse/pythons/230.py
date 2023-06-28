import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def concatenate_along_column(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    return np.concatenate((arr1, arr2), axis=1)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = concatenate_along_column(input_grid, input_grid)
    return output_grid