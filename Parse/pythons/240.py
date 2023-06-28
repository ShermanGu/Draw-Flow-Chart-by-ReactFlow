import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_cw(input_grid: np.ndarray) -> np.ndarray:
    return np.rot90(input_grid, k=-1)

def flip_ud(input_grid: np.ndarray) -> np.ndarray:
    return np.flipud(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    out_grid = flip_ud(input_grid)
    out_grid = rotate_cw(out_grid)
    return out_grid