import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_black_to_red(upper: int, lower: int, left: int, right: int, input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function turns all black pixels in the given range into red.

    Args:
    upper: An integer representing the upper boundary of the range.
    lower: An integer representing the lower boundary of the range.
    left: An integer representing the left boundary of the range.
    right: An integer representing the right boundary of the range.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the output grid with all black pixels in the given range turned into red.
    """
    output_grid = np.copy(input_grid)
    for i in range(upper, lower + 1):
        for j in range(left, right + 1):
            if input_grid[i][j] == black:
                output_grid[i][j] = red
    return output_grid

def find_boundaries(input_grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    Given an input grid, this function returns the upper, lower, left and right boundaries of the non-black pixels.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple containing the upper, lower, left and right boundaries of the non-black pixels.
    """
    (rows, cols) = input_grid.shape
    upper = rows
    lower = 0
    left = cols
    right = 0
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] != black:
                upper = min(upper, i)
                lower = max(lower, i)
                left = min(left, j)
                right = max(right, j)
    return (upper, lower, left, right)

def main(input_grid: np.ndarray) -> np.ndarray:
    (upper, lower, left, right) = find_boundaries(input_grid)
    output_grid = turn_black_to_red(upper, lower, left, right, input_grid)
    return output_grid