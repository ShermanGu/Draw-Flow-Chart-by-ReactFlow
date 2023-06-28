import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def double_size(input_grid: np.ndarray) -> np.ndarray:
    out = np.repeat(np.repeat(input_grid, 2, axis=1), 2, axis=0)
    return out

def main(input_grid: np.ndarray) -> np.ndarray:
    out = double_size(input_grid)
    return out