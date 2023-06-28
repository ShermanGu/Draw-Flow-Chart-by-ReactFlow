import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_border_teal(input_grid: np.ndarray) -> np.ndarray:
    """
    Paints the pixels of all borders of the input grid as teal and returns the modified grid.
    """
    input_grid[0, :] = teal
    input_grid[-1, :] = teal
    input_grid[:, 0] = teal
    input_grid[:, -1] = teal
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    ans_grid = paint_border_teal(input_grid)
    return ans_grid