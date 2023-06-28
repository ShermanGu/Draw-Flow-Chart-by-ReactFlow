import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_to_maroon(grid: np.ndarray, i: int, j: int) -> np.ndarray:
    """
    Colors the given point in the grid to maroon.

    Args:
    - grid (np.ndarray): The input grid.
    - i (int): The row index of the point.
    - j (int): The column index of the point.

    Returns:
    - np.ndarray: The updated grid with the given point colored to maroon.
    """
    grid[i][j] = maroon
    return grid

def has_red_neighbors_in_horizontal_directions(grid: np.ndarray, i: int, j: int) -> bool:
    """
    Checks if the given point has red neighbors in horizontal directions.

    Args:
    - grid (np.ndarray): The input grid.
    - i (int): The row index of the point.
    - j (int): The column index of the point.

    Returns:
    - bool: True if the given point has red neighbors in horizontal directions, False otherwise.
    """
    if grid[i][j] == black:
        row = grid[i]
        if red in row[:j] and red in row[j + 1:]:
            return True
    return False

def main(input_grid: np.ndarray) -> np.ndarray:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if has_red_neighbors_in_horizontal_directions(input_grid, i, j):
                input_grid = color_to_maroon(input_grid, i, j)
    return input_grid