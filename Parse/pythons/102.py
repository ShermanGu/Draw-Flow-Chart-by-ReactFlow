import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def check_symmetry(input_grid: np.ndarray) -> int:
    if np.array_equal(input_grid, np.fliplr(input_grid)):
        return blue
    else:
        return yellow

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.array([[check_symmetry(input_grid)]])
    return output_grid