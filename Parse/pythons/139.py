import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_180_clockwise(input_grid: np.ndarray) -> np.ndarray:
    return np.rot90(np.rot90(input_grid))

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = rotate_180_clockwise(input_grid)
    return output_grid