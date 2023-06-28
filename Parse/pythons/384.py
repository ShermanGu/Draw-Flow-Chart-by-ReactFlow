import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def flip_rows(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.copy(input_grid)
    output_grid[:5, :] = input_grid[-5:, :][::-1, :]
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = flip_rows(input_grid)
    return output_grid