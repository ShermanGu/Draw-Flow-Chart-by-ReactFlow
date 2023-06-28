import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_grey_with_green(grid: np.ndarray, i: int) -> np.ndarray:
    """
    This function replaces the grey elements in the i-th column of the grid with green elements if the total number of columns minus i is odd.

    Args:
    grid: A numpy array representing the input grid.
    i: An integer representing the column index.

    Returns:
    A numpy array representing the updated grid.
    """
    if (grid.shape[1] - i) % 2 == 1:
        for j in range(grid.shape[0]):
            if grid[j][i] == grey:
                grid[j][i] = green
    return grid

def initialize_grid(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.copy(input_grid)
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = initialize_grid(input_grid)
    for i in range(input_grid.shape[1]):
        output_grid = replace_grey_with_green(output_grid, i)
    return output_grid