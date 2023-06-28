import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def set_elements_around_colors(input_grid: np.ndarray) -> np.ndarray:
    """
    Sets black elements around red element in input grid to blue elments, sets black elements around green element in input grid to pink elements, and sets black elements around teal element in input grid to yellow elements.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the output grid after setting the elements around the specified colors.
    """
    output_grid = copy_grid(input_grid)
    for i in range(1, input_grid.shape[0] - 1):
        for j in range(1, input_grid.shape[1] - 1):
            if input_grid[i][j] == red:
                output_grid[i - 1:i + 2, j - 1:j + 2][output_grid[i - 1:i + 2, j - 1:j + 2] == black] = blue
            elif input_grid[i][j] == green:
                output_grid[i - 1:i + 2, j - 1:j + 2][output_grid[i - 1:i + 2, j - 1:j + 2] == black] = pink
            elif input_grid[i][j] == teal:
                output_grid[i - 1:i + 2, j - 1:j + 2][output_grid[i - 1:i + 2, j - 1:j + 2] == black] = yellow
    return output_grid

def copy_grid(input_grid: np.ndarray) -> np.ndarray:
    """
    Returns a copy of the input grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing a copy of the input grid.
    """
    return np.copy(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = copy_grid(input_grid)
    output_grid = set_elements_around_colors(output_grid)
    return output_grid