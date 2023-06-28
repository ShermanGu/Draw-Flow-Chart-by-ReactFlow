import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_red_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    This function returns a new grid after changing the color of some red pixels to blue.
    If a red pixel has no red pixel up or down or left or right, then it is turned to blue.

    Args:
    input_grid (numpy.ndarray) : a two-dimensional numpy array containing the grid of pixels.

    Returns:
    numpy.ndarray : a new two-dimensional numpy array containing the updated grid.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                if i == 0 or input_grid[i - 1][j] != red:
                    if i == input_grid.shape[0] - 1 or input_grid[i + 1][j] != red:
                        if j == 0 or input_grid[i][j - 1] != red:
                            if j == input_grid.shape[1] - 1 or input_grid[i][j + 1] != red:
                                input_grid[i][j] = blue
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = change_red_pixels(input_grid)
    return output_grid