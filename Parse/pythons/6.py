import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_color_coordinate(input_grid: np.ndarray, color: int) -> Tuple[int, int]:
    """
    This function takes in a numpy array of shape (7, 7) and a color integer and returns the coordinate of the first occurrence of the color in the input.

    Args:
    input_grid: A numpy array of shape (7, 7) containing integers from 0 to 9.
    color: An integer representing the color to search for.

    Returns:
    A tuple of two integers representing the coordinate of the first occurrence of the color in the input.
    """
    for i in range(7):
        for j in range(7):
            if input_grid[i][j] == color:
                return (i, j)
    return (-1, -1)

def get_non_black_colors(input_grid: np.ndarray) -> Tuple[int, int, int]:
    """
    This function takes in a numpy array of shape (7, 7) and returns a tuple of three non-black colors present in the input.

    Args:
    input_grid: A numpy array of shape (7, 7) containing integers from 0 to 9.

    Returns:
    A tuple of three integers representing the non-black colors present in the input.
    """
    non_black_colors = set(np.unique(input_grid)) - {black}
    return tuple(non_black_colors)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.zeros((7, 7), dtype=int)
    (color1, color2, color3) = get_non_black_colors(input_grid)
    for color in (color1, color2, color3):
        (x, y) = get_color_coordinate(input_grid, color)
        if (x + y) % 3 == 0:
            c1 = color
        elif (x + y) % 3 == 1:
            c2 = color
        else:
            c3 = color
    for i in range(7):
        for j in range(7):
            if (i + j) % 3 == 0:
                output_grid[i][j] = c1
            elif (i + j) % 3 == 1:
                output_grid[i][j] = c2
            else:
                output_grid[i][j] = c3
    return output_grid