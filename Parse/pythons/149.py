import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def flip_left_right(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.fliplr(input_grid)
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = flip_left_right(input_grid)
    return output_grid