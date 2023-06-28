import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def modify_grid(input_grid: np.ndarray) -> np.ndarray:
    """
    Traversing all 2*2 sub-grids in the inputgrid, if there are three teal
    pixels and one black pixel in a 2*2 sub-grid, paint the black pixel blue.
    Return the modified grid.
    """
    for i in range(input_grid.shape[0] - 1):
        for j in range(input_grid.shape[1] - 1):
            sub_grid = input_grid[i:i + 2, j:j + 2]
            if np.sum(sub_grid == teal) == 3 and np.sum(sub_grid == black) == 1:
                input_grid[i + np.where(sub_grid == black)[0][0], j + np.where(sub_grid == black)[1][0]] = blue
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    ans_grid = modify_grid(input_grid)
    return ans_grid