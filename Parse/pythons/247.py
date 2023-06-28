import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def copy_blue_pixel_left_up(input_grid: np.ndarray) -> np.ndarray:
    blue_pixel_position = np.where(input_grid == blue)
    (row, col) = (blue_pixel_position[0][0], blue_pixel_position[1][0])
    while col > 0:
        input_grid[row - 1, col - 1] = blue
        (row, col) = (row - 1, col - 1)
    return input_grid

def copy_blue_pixel_right_up(input_grid: np.ndarray) -> np.ndarray:
    blue_pixel_position = np.where(input_grid == blue)
    (row, col) = (blue_pixel_position[0][0], blue_pixel_position[1][0])
    while col < input_grid.shape[1] - 1 and row > 0:
        input_grid[row - 1, col + 1] = blue
        (row, col) = (row - 1, col + 1)
    return input_grid

def is_blue_pixel_reached_top(input_grid: np.ndarray) -> bool:
    """
    This function checks if the blue pixel has reached the top of the grid.

    Args:
    input_grid: A numpy array representing the grid.

    Returns:
    A boolean value indicating if the blue pixel has reached the top of the grid.
    """
    return blue in input_grid[0]

def main(input_grid: np.ndarray) -> np.ndarray:
    flag = is_blue_pixel_reached_top(input_grid)
    while not flag:
        copy_blue_pixel_right_up(input_grid)
        copy_blue_pixel_left_up(input_grid)
        flag = is_blue_pixel_reached_top(input_grid)
    return input_grid