import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def generate_output_grid(major_color: int, vertical_line_num: int, horizontal_line_num: int) -> np.ndarray:
    """
    Given the major color, number of grids in the first row that are not of major color, and number of grids in the first column that are not of major color,
    this function generates an output grid of size (horizontal_line_num + 1) x (vertical_line_num + 1) where all grids are of major color.

    Args:
    major_color: An integer representing the major color in the grid.
    vertical_line_num: An integer representing the number of grids in the first row that are not of major color.
    horizontal_line_num: An integer representing the number of grids in the first column that are not of major color.

    Returns:
    A numpy array representing the output grid.
    """
    output = np.full((horizontal_line_num + 1, vertical_line_num + 1), major_color)
    return output

def find_horizontal_line_num(input_grid: np.ndarray, major_color: int) -> int:
    """
    Given an input grid and the major color, this function finds the number of grids in the first column that are not of major color.

    Args:
    input_grid: A numpy array representing the input grid.
    major_color: An integer representing the major color in the grid.

    Returns:
    An integer representing the number of grids in the first column that are not of major color.
    """
    first_column = input_grid[:, 0]
    return len(first_column) - np.count_nonzero(first_column == major_color)

def find_vertical_line_num(input_grid: np.ndarray, major_color: int) -> int:
    """
    Given an input grid and the major color, this function finds the number of grids in the first row that are not of major color.

    Args:
    input_grid: A numpy array representing the input grid.
    major_color: An integer representing the major color in the grid.

    Returns:
    An integer representing the number of grids in the first row that are not of major color.
    """
    first_row = input_grid[0]
    return len(first_row) - np.count_nonzero(first_row == major_color)

def find_major_color(input_grid: np.ndarray) -> int:
    """
    Given an input grid, this function finds the major color in the grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    An integer representing the major color in the grid.
    """
    color_counts = np.bincount(input_grid.flatten())
    major_color = np.argmax(color_counts)
    return major_color

def main(input_grid: np.ndarray) -> np.ndarray:
    major_color = find_major_color(input_grid)
    vertical_line_num = find_vertical_line_num(input_grid, major_color)
    horizontal_line_num = find_horizontal_line_num(input_grid, major_color)
    output = generate_output_grid(major_color, vertical_line_num, horizontal_line_num)
    return output