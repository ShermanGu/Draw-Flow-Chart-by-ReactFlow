import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def double_size_shape1(input_grid: np.ndarray) -> np.ndarray:
    out = np.concatenate((input_grid, input_grid), axis=1)
    return out

def main(input_grid: np.ndarray) -> np.ndarray:
    out = double_size_shape1(input_grid)
    return out