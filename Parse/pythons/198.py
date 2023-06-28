import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def copy_short_yellow_line(input_grid: np.ndarray, shape: Tuple[int, int], i: int) -> np.ndarray:
    """
    Copies a short yellow line with the given shape at the specified column index in the input grid.

    Args:
    input_grid: A numpy array representing the input grid.
    shape: A tuple representing the shape of the yellow line (start row, end row).
    i: An integer representing the column index where the yellow line should be copied.

    Returns:
    A numpy array representing the updated grid after copying the yellow line.
    """
    (start_row, end_row) = shape
    for row in range(start_row, end_row + 1):
        input_grid[row][i] = yellow
    return input_grid

def find_yellow_line(input_grid: np.ndarray) -> Tuple[int, Tuple[int, int]]:
    """
    Finds the index and shape of the vertical line in yellow in the input grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple containing the index of the yellow line and a tuple representing its shape (start row, end row).
    """
    yellow_pixels = np.where(input_grid == yellow)
    if len(yellow_pixels[1]) == 0:
        return None
    j = yellow_pixels[1][0]
    start_row = min(yellow_pixels[0])
    end_row = max(yellow_pixels[0])
    return (j, (start_row, end_row))

def copy_yellow_pattern_along_horizontal(input_grid: np.ndarray) -> np.ndarray:
    (index, shape) = find_yellow_line(input_grid)
    for i in range(input_grid.shape[1]):
        if i % 2 == index % 2:
            input_grid = copy_short_yellow_line(input_grid, shape, i)
    return input_grid

def color_pixels_above_yellow(p: Tuple[int, int], input_grid: np.ndarray) -> np.ndarray:
    """
    Colors the given pixel and the pixels above it in the same column in yellow.

    Args:
    p: A tuple containing the row and column indices of the pixel to be colored.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the updated grid after coloring the pixels in yellow.
    """
    (i, j) = p
    input_grid[i][j] = yellow
    for k in range(i):
        input_grid[k][j] = yellow
    return input_grid

def move_down(p: Tuple[int, int], input_grid: np.ndarray) -> np.ndarray:
    """
    Moves the given pixel down by one row in the input grid.

    Args:
    p: A tuple containing the row and column indices of the pixel to be moved.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the updated grid after moving the pixel down by one row.
    """
    (i, j) = p
    if i == input_grid.shape[0] - 1:
        return input_grid
    (input_grid[i][j], input_grid[i + 1][j]) = (input_grid[i + 1][j], input_grid[i][j])
    return input_grid

def find_not_black_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Finds the first non-black pixel in the input grid and returns its coordinates.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple containing the row and column indices of the first non-black pixel.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                return (i, j)
    return None

def main(input_grid: np.ndarray) -> np.ndarray:
    p = find_not_black_pixel(input_grid)
    move = move_down(p, input_grid)
    color = color_pixels_above_yellow(p, input_grid)
    out = copy_yellow_pattern_along_horizontal(input_grid)
    return out