import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_grey_point(input_grid: np.ndarray, col: int, color: int) -> np.ndarray:
    """
    Paints all grey points in the specified column of the input grid to the specified color.

    Args:
    - input_grid: A numpy array representing the input grid.
    - col: An integer representing the index of the column to be painted.
    - color: An integer representing the color to which the grey points in the specified column should be painted.

    Returns:
    - A numpy array representing the updated input grid with the grey points in the specified column painted to the specified color.
    """
    input_grid[input_grid[:, col] == grey, col] = color
    return input_grid

def sort_grey_num(grey_num: List[int]) -> List[int]:
    return np.argsort(grey_num)[::-1]

def count_grey_per_column(input_grid: np.ndarray) -> List[int]:
    return np.count_nonzero(input_grid == grey, axis=0)

def main(input_grid: np.ndarray) -> np.ndarray:
    grey_num = count_grey_per_column(input_grid)
    sorted_list = sort_grey_num(grey_num)
    color_list = [blue, red, green, yellow]
    for i in range(4):
        output = paint_grey_point(input_grid, sorted_list[i], color_list[i])
    return output