import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_90_counterclockwise(input_grid: np.ndarray) -> np.ndarray:
    return np.rot90(input_grid, k=1)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = rotate_90_counterclockwise(input_grid)
    return output_grid