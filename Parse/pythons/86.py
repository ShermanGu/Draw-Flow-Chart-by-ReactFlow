import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_180(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.rot90(input_grid, 2)
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = rotate_180(input_grid)
    return output_grid