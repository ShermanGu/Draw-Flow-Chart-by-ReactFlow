import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_270(grid: np.ndarray) -> np.ndarray:
    """
    Rotate the input grid by 270 degrees.
    :param grid: 2D numpy array representing the input grid
    :return: 2D numpy array representing the rotated grid
    """
    return np.rot90(grid, k=3)

def extend_column_to_grid(column: np.ndarray, n: int) -> np.ndarray:
    """
    Extend a column to a grid with n columns.
    :param column: 1D numpy array representing the column to be extended
    :param n: integer representing the number of columns in the output grid
    :return: 2D numpy array representing the output grid
    """
    return np.tile(column, (n, 1)).T

def rotate_if_needed(input_grid: np.ndarray, colors: List[int]) -> Tuple[bool, np.ndarray]:
    """
    If the most frequent color in each row occurs less than 50% of the time, rotate the input grid by 90 degrees.
    :param input_grid: 2D numpy array representing the input grid
    :param colors: List of most frequent colors in each row
    :return: Tuple of boolean indicating whether the grid was rotated and the rotated grid
    """
    threshold = input_grid.shape[1] // 2
    has_rotate = False
    for (i, row) in enumerate(input_grid):
        if np.count_nonzero(row == colors[i]) < threshold:
            input_grid = np.rot90(input_grid)
            has_rotate = True
            break
    return (has_rotate, input_grid)

def find_most_frequent_color_in_row(grid: np.ndarray) -> List[int]:
    """
    Find the color with the most occurrences in each row of the input grid.
    :param grid: 2D numpy array representing the input grid
    :return: List of integers representing the most frequent color in each row
    """
    return [np.bincount(row).argmax() for row in grid]

def main(input_grid: np.ndarray) -> np.ndarray:
    colors = find_most_frequent_color_in_row(input_grid)
    (has_rotate, input_grid) = rotate_if_needed(input_grid, colors)
    colors = find_most_frequent_color_in_row(input_grid)
    output_grid = extend_column_to_grid(np.array(colors), n=input_grid.shape[1])
    if has_rotate:
        output_grid = rotate_270(output_grid)
    return output_grid