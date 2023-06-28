import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_grid_180(input_grid: np.ndarray) -> np.ndarray:
    """
    Given a 2D numpy array representing a grid of colors, this function rotates the grid 180 degrees.

    Args:
    input_grid: A 2D numpy array representing a grid of colors.

    Returns:
    A 2D numpy array representing the rotated grid.
    """
    return np.rot90(np.rot90(input_grid))

def find_blue_square(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given a 2D numpy array representing a grid of colors, this function finds the top-left coordinates of a 5x5 blue square.

    Args:
    input_grid: A 2D numpy array representing a grid of colors.

    Returns:
    A tuple of two integers representing the top-left coordinates of a 5x5 blue square.
    """
    (i, j) = np.where(input_grid == blue)
    return (i[0], j[0])

def main(input_grid: np.ndarray) -> np.ndarray:
    (i, j) = find_blue_square(input_grid)
    grid = rotate_grid_180(input_grid)
    return grid[i:i + 5, j:j + 5]