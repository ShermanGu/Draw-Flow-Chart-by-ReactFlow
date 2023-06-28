import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_bottom_left_green(input_grid):
    """
    Given a 2D grid of colors represented as integers, this function colors the bottom left position with green.

    Args:
    input_grid: A 2D numpy array of integers representing the colors of the grid.

    Returns:
    A 2D numpy array of integers representing the updated grid with the bottom left position colored green.
    """
    input_grid[-1][0] = green
    return input_grid

def color_last_line_yellow(input_grid):
    """
    Given a 2D grid of colors represented as integers, this function colors the last line with yellow.

    Args:
    input_grid: A 2D numpy array of integers representing the colors of the grid.

    Returns:
    A 2D numpy array of integers representing the updated grid with the last line colored yellow.
    """
    n = input_grid.shape[0]
    input_grid[n - 1] = yellow
    return input_grid

def color_inverse_diagonal_red(input_grid):
    """
    Given a 2D grid of colors represented as integers, this function colors the inverse diagonal with red.

    Args:
    input_grid: A 2D numpy array of integers representing the colors of the grid.

    Returns:
    A 2D numpy array of integers representing the updated grid with the inverse diagonal colored red.
    """
    n = input_grid.shape[0]
    for i in range(n):
        input_grid[i][n - i - 1] = red
    return input_grid

def main(input_grid):
    output = color_inverse_diagonal_red(input_grid)
    output = color_last_line_yellow(output)
    output = color_bottom_left_green(output)
    return output