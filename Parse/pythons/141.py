import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def vertical_mirror(input_grid: np.ndarray) -> np.ndarray:
    return np.concatenate((input_grid, np.flipud(input_grid)), axis=0)

def horizontal_mirror(input_grid: np.ndarray) -> np.ndarray:
    return np.concatenate((input_grid, np.fliplr(input_grid)), axis=1)

def main(input_grid: np.ndarray) -> np.ndarray:
    grid1 = horizontal_mirror(input_grid)
    output_grid = vertical_mirror(grid1)
    return output_grid