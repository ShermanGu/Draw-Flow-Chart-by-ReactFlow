import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def put_pixels_right_to_left_at_row(color: int, row: int, number: int, output_grid: np.ndarray) -> np.ndarray:
    """
    Puts the given number of pixels of the given color from right to left at the given row in the output grid.

    Args:
    color: An integer representing the color of the pixels to be put.
    row: An integer representing the row at which the pixels are to be put.
    number: An integer representing the number of pixels to be put.
    output_grid: A numpy array representing the output grid.

    Returns:
    A numpy array representing the updated output grid.
    """
    for i in range(number):
        output_grid[row][output_grid.shape[1] - 1 - i] = color
    return output_grid

def count_non_black_pixels(input_grid: np.ndarray) -> List[int]:
    """
    Counts the number of non-black pixels of each color in the input grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A list of integers representing the count of non-black pixels of each color.
    """
    color_counts = [0] * 10
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                color_counts[input_grid[i][j]] += 1
    sorted_color = sorted(range(len(color_counts)), key=lambda k: color_counts[k], reverse=True)
    return sorted_color

def main(input_grid: np.ndarray) -> np.ndarray:
    sorted_color = count_non_black_pixels(input_grid)
    output_grid = np.zeros_like(input_grid)
    for i in range(len(sorted_color)):
        color = sorted_color[i]
        row = output_grid.shape[0] - 1 - i
        number = output_grid.shape[1] - i
        output_grid = put_pixels_right_to_left_at_row(color, row, number, output_grid)
    return output_grid