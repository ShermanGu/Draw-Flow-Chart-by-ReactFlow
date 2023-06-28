import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def put_red_on_diagonal(red_corner: Tuple[int, int], input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid and the coordinates of the bottom-right red pixel, this function puts red pixels on the diagonal
    from the red corner to the bottom-right corner.

    Args:
    red_corner: A tuple containing the row and column indices of the bottom-right red pixel.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the updated grid with red pixels on the diagonal.
    """
    (i, j) = red_corner
    while i < input_grid.shape[0] and j < input_grid.shape[1]:
        input_grid[i][j] = red
        i += 1
        j += 1
    return input_grid

def put_blue_on_diagonal(blue_corner: Tuple[int, int], input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid and the coordinates of the top-left blue pixel, this function puts blue pixels on the diagonal
    from the blue corner to the top-left corner.

    Args:
    blue_corner: A tuple containing the row and column indices of the top-left blue pixel.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the updated grid with blue pixels on the diagonal.
    """
    (i, j) = blue_corner
    while i >= 0 and j >= 0:
        input_grid[i][j] = blue
        i -= 1
        j -= 1
    return input_grid

def find_bottom_right_red_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given an input grid, this function finds the bottom-right red pixel and returns its coordinates.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple containing the row and column indices of the bottom-right red pixel.
    """
    for i in range(input_grid.shape[0] - 1, -1, -1):
        for j in range(input_grid.shape[1] - 1, -1, -1):
            if input_grid[i][j] == red:
                return (i, j)

def find_top_left_blue_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given an input grid, this function finds the top-left blue pixel and returns its coordinates.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple containing the row and column indices of the top-left blue pixel.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                return (i, j)

def main(input_grid: np.ndarray) -> np.ndarray:
    blue_corner = find_top_left_blue_pixel(input_grid)
    red_corner = find_bottom_right_red_pixel(input_grid)
    input_grid = put_blue_on_diagonal(blue_corner, input_grid)
    input_grid = put_red_on_diagonal(red_corner, input_grid)
    return input_grid