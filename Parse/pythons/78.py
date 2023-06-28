import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_3x3_matrix_with_color_in_each_row_and_column(input_grid: np.ndarray, c: int) -> np.ndarray:
    """
    Given an input grid and a color c, returns a 3x3 matrix from the input, with at least one pixel color of c in each row and at least one pixel color of c in each column.

    Args:
    input_grid: A numpy array representing the input grid.
    c: An integer representing the color.

    Returns:
    A numpy array representing the 3x3 matrix with at least one pixel color of c in each row and at least one pixel color of c in each column.
    """
    for i in range(input_grid.shape[0] - 2):
        for j in range(input_grid.shape[1] - 2):
            if c in input_grid[i:i + 3, j:j + 3]:
                row_sum = np.sum(input_grid[i:i + 3, j:j + 3] == c, axis=1)
                col_sum = np.sum(input_grid[i:i + 3, j:j + 3] == c, axis=0)
                if np.all(row_sum) and np.all(col_sum):
                    return input_grid[i:i + 3, j:j + 3]
    return np.zeros((3, 3))

def get_highest_color(input_grid: np.ndarray) -> int:
    """
    Given an input grid, returns the color with the highest number of pixels except for black.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    An integer representing the color with the highest number of pixels except for black.
    """
    color_counts = np.bincount(input_grid.flatten())
    color_counts[black] = 0
    return np.argmax(color_counts)

def main(input_grid: np.ndarray) -> np.ndarray:
    c = get_highest_color(input_grid)
    out = find_3x3_matrix_with_color_in_each_row_and_column(input_grid, c)
    return out