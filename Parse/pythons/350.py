import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_submatrix(input_grid: np.ndarray, r1: int, r2: int, c1: int, c2: int) -> np.ndarray:
    """
    Returns the submatrix of input_grid composed of rows from r1 to r2 and columns from c1 to c2.

    Args:
    input_grid: A numpy array representing the input grid.
    r1: An integer representing the starting row index.
    r2: An integer representing the ending row index.
    c1: An integer representing the starting column index.
    c2: An integer representing the ending column index.

    Returns:
    A numpy array representing the submatrix of input_grid.
    """
    return input_grid[r1:r2 + 1, c1:c2 + 1]

def replace_green_pixels_mirror(input_grid: np.ndarray, width: int) -> np.ndarray:
    """
    For each green pixel, denote it in line r, column c. Replace it with the color of the pixel in line r, column w-c.

    Args:
    input_grid: A numpy array representing the input grid.
    width: An integer representing the width of the input_grid.

    Returns:
    A numpy array representing the modified input grid.
    """
    green_pixels = np.where(input_grid == green)
    r_values = green_pixels[0]
    c_values = green_pixels[1]
    for (r, c) in zip(r_values, c_values):
        input_grid[r][c] = input_grid[r][width - c - 1]
    return input_grid

def replace_green_pixels(input_grid: np.ndarray, width: int) -> np.ndarray:
    """
    For each green pixel, denote it in line r, column c. Replace it with the color of the pixel in line w-r, column c.

    Args:
    input_grid: A numpy array representing the input grid.
    width: An integer representing the width of the input_grid.

    Returns:
    A numpy array representing the modified input grid.
    """
    green_pixels = np.where(input_grid == green)
    r_values = green_pixels[0]
    c_values = green_pixels[1]
    for (r, c) in zip(r_values, c_values):
        input_grid[r][c] = input_grid[width - r - 1][c]
    return input_grid

def get_width(input_grid: np.ndarray) -> int:
    """
    Returns the width of the input_grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    An integer representing the width of the input_grid.
    """
    return input_grid.shape[1]

def find_smallest_green_matrix(input_grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    Finds the smallest matrix with all green pixels in the input_grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple of four integers representing the smallest matrix with all green pixels in the input_grid.
    """
    (r1, r2, c1, c2) = (np.where(input_grid == green)[0].min(), np.where(input_grid == green)[0].max(), np.where(input_grid == green)[1].min(), np.where(input_grid == green)[1].max())
    return (r1, r2, c1, c2)

def main(input_grid: np.ndarray) -> np.ndarray:
    (r1, r2, c1, c2) = find_smallest_green_matrix(input_grid)
    w = get_width(input_grid)
    if r1 < w / 2 < r2:
        out = replace_green_pixels(input_grid, w)
    else:
        out = replace_green_pixels_mirror(input_grid, w)
    out = get_submatrix(out, r1, r2, c1, c2)
    return out