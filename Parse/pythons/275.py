import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_pink_to_red(output_grid: np.ndarray) -> np.ndarray:
    output_grid[output_grid == pink] = red
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid.copy()
    output_grid = change_pink_to_red(output_grid)
    return output_grid