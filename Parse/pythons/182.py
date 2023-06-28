import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_lower_right_quarter(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    """
    Turns non-black pixels in lower right quarter of output_grid into the color of the lower right pixel of input grid.

    Args:
    output_grid: A numpy array representing the output grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the updated output grid.
    """
    lower_right_color = input_grid[-1, -1]
    (rows, cols) = output_grid.shape
    for i in range(rows // 2, rows):
        for j in range(cols // 2, cols):
            if output_grid[i, j] != black:
                output_grid[i, j] = lower_right_color
    return output_grid

def turn_lower_left_quarter(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    """
    Turns non-black pixels in lower left quarter of output_grid into the color of the lower left pixel of input grid.

    Args:
    output_grid: A numpy array representing the output grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the updated output grid.
    """
    lower_left_color = input_grid[-1, 0]
    (rows, cols) = output_grid.shape
    for i in range(rows // 2, rows):
        for j in range(cols // 2):
            if output_grid[i, j] != black:
                output_grid[i, j] = lower_left_color
    return output_grid

def turn_upper_right_quarter(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    """
    Turns non-black pixels in upper right quarter of output_grid into the color of the upper right pixel of input grid.

    Args:
    output_grid: A numpy array representing the output grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the updated output grid.
    """
    upper_right_color = input_grid[0, -1]
    (rows, cols) = output_grid.shape
    for i in range(rows // 2):
        for j in range(cols // 2, cols):
            if output_grid[i, j] != black:
                output_grid[i, j] = upper_right_color
    return output_grid

def turn_upper_left_quarter(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    """
    Turns non-black pixels in upper left quarter of output_grid into the color of the upper left pixel of input grid.

    Args:
    output_grid: A numpy array representing the output grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the updated output grid.
    """
    upper_left_color = input_grid[0, 0]
    (rows, cols) = output_grid.shape
    for i in range(rows // 2):
        for j in range(cols // 2):
            if output_grid[i, j] != black:
                output_grid[i, j] = upper_left_color
    return output_grid

def divide_input(input_grid: np.ndarray) -> np.ndarray:
    """
    Divides the input grid by all blue rows and pixels, and returns the center grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the center grid.
    """
    blue_rows = np.where(np.all(input_grid == blue, axis=1))[0]
    blue_cols = np.where(np.all(input_grid == blue, axis=0))[0]
    center_grid = input_grid[blue_rows[0] + 1:blue_rows[-1], blue_cols[0] + 1:blue_cols[-1]]
    return center_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = divide_input(input_grid)
    output_grid = turn_upper_left_quarter(output_grid, input_grid)
    output_grid = turn_upper_right_quarter(output_grid, input_grid)
    output_grid = turn_lower_left_quarter(output_grid, input_grid)
    output_grid = turn_lower_right_quarter(output_grid, input_grid)
    return output_grid