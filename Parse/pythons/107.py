import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def enlarge_image(input_grid: np.ndarray) -> np.ndarray:
    """
    Enlarges the input grid proportionally to twice its original size (both width and height are doubled).

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the enlarged input grid.
    """
    return np.kron(input_grid, np.ones((2, 2), dtype=input_grid.dtype))

def fill_adjacent_pixels_with_color(input_grid: np.ndarray) -> np.ndarray:
    """
    Traverse the input grid, and if a non-black colored pixel is encountered, fill the adjacent pixels with the same color.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the modified input grid.
    """
    for i in range(1, input_grid.shape[0]):
        for j in range(1, input_grid.shape[1]):
            if input_grid[i][j] != black:
                color = input_grid[i][j]
                input_grid[i - 1][j] = color
                input_grid[i][j - 1] = color
                input_grid[i - 1][j - 1] = color
    return input_grid

def count_colors(input_grid: np.ndarray) -> int:
    """
    Counts the total number of different colors (excluding black) in the input grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    An integer representing the total number of different colors (excluding black) in the input grid.
    """
    unique_colors = set()
    for row in input_grid:
        for pixel in row:
            if pixel != black:
                unique_colors.add(pixel)
    return len(unique_colors)

def main(input_grid: np.ndarray) -> np.ndarray:
    n = count_colors(input_grid)
    input_grid = fill_adjacent_pixels_with_color(input_grid)
    input_grid = enlarge_image(input_grid)
    return input_grid