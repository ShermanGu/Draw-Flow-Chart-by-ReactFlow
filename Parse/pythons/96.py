import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_to_black(input_grid: np.ndarray, i: int, j: int) -> np.ndarray:
    """
    Colors the given point in input_grid to black.

    Args:
    input_grid: A numpy array representing the input grid.
    i: An integer representing the row index of the point.
    j: An integer representing the column index of the point.

    Returns:
    A numpy array with the given point colored black.
    """
    input_grid[i][j] = black
    return input_grid

def all_adjacent_black(input_grid: np.ndarray, i: int, j: int) -> bool:
    """
    Checks if all eight adjacent points of the given point in input_grid are black.

    Args:
    input_grid: A numpy array representing the input grid.
    i: An integer representing the row index of the point.
    j: An integer representing the column index of the point.

    Returns:
    A boolean value indicating if all eight adjacent points of the given point in input_grid are black.
    """
    (rows, cols) = input_grid.shape
    adjacent_points = [(i + di, j + dj) for di in [-1, 0, 1] for dj in [-1, 0, 1] if di != 0 or dj != 0]
    for (x, y) in adjacent_points:
        if x >= 0 and x < rows and (y >= 0) and (y < cols) and (input_grid[x][y] != black):
            return False
    return True

def main(input_grid: np.ndarray) -> np.ndarray:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if all_adjacent_black(input_grid, i, j):
                input_grid = color_to_black(input_grid, i, j)
    return input_grid