import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_pixels_around_b_with_red(b: int, grid: np.ndarray) -> np.ndarray:
    """
    Given a 2D numpy array and an integer representing a color, replace the 8 pixels around the given color with red.

    Args:
    - b: integer representing the color to target
    - grid: 2D numpy array of integers representing colors

    Returns:
    - out: 2D numpy array with the 8 pixels around the target color replaced with red
    """
    (height, width) = grid.shape
    out = np.copy(grid)
    for i in range(height):
        for j in range(width):
            if grid[i][j] == b:
                if i - 1 >= 0 and j - 1 >= 0:
                    out[i - 1][j - 1] = red
                if i - 1 >= 0:
                    out[i - 1][j] = red
                if i - 1 >= 0 and j + 1 < width:
                    out[i - 1][j + 1] = red
                if j - 1 >= 0:
                    out[i][j - 1] = red
                if j + 1 < width:
                    out[i][j + 1] = red
                if i + 1 < height and j - 1 >= 0:
                    out[i + 1][j - 1] = red
                if i + 1 < height:
                    out[i + 1][j] = red
                if i + 1 < height and j + 1 < width:
                    out[i + 1][j + 1] = red
    return out

def replace_pixels_except_b_with_black(b: int, grid: np.ndarray) -> np.ndarray:
    """
    Given a 2D numpy array and an integer representing a color, replace all pixels except for the given color with black.

    Args:
    - b: integer representing the color to keep
    - grid: 2D numpy array of integers representing colors

    Returns:
    - out: 2D numpy array with all pixels except for the given color replaced with black
    """
    out = np.where(grid == b, b, black)
    return out

def get_unique_color(grid: np.ndarray) -> int:
    """
    Given a 2D numpy array, find the color that appears only once in the array.

    Args:
    - grid: 2D numpy array of integers representing colors

    Returns:
    - unique_color: integer representing the color that appears only once in the array
    """
    (colors, counts) = np.unique(grid, return_counts=True)
    unique_color = colors[np.where(counts == 1)][0]
    return unique_color

def main(input_grid: np.ndarray) -> np.ndarray:
    b = get_unique_color(input_grid)
    out = replace_pixels_except_b_with_black(b, input_grid)
    out = replace_pixels_around_b_with_red(b, out)
    return out