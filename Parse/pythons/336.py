import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_color(input_grid: np.ndarray) -> np.ndarray:
    """
    This function takes an n*n grid with multiple color pixels as input.
    It traverses all pixels and changes the color of the pixel from gray to teal and from teal to gray.
    It returns the updated grid.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == grey:
                input_grid[i][j] = teal
            elif input_grid[i][j] == teal:
                input_grid[i][j] = grey
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    ans_grid = change_color(input_grid)
    return ans_grid