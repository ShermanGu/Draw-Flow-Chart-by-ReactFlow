import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_orange_to_grey(input_grid: np.ndarray) -> np.ndarray:
    input_grid[input_grid == orange] = grey
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output = change_orange_to_grey(input_grid)
    return output