import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_subgrid(input_grid: np.ndarray, lux: int, luy: int, lbx: int, lby: int, tcnt: int) -> np.ndarray:
    """
    In the input grid, takes (lux+1, luy+1) as the upper left corner, takes the subgrid whose shape is (lby - luy -1, tcnt-2), and returns the grid.
    """
    return input_grid[lux + 1:lbx, luy + 1:lby]

def find_bottom_right(input_grid: np.ndarray, tcolor: int, lux: int, luy: int) -> Tuple[int, int]:
    """
    This function takes in a n*n grid with multiple color pixels, the color that appears consecutively the most, and the coordinates of the top-left pixel of the largest consecutive block of the most frequent color. It returns the coordinates of the bottom-right pixel of the largest consecutive block of the most frequent color.
    """
    for i in range(lux, input_grid.shape[0]):
        for j in range(luy, input_grid.shape[1]):
            if input_grid[i][j] == tcolor and (i + 1 == input_grid.shape[0] or input_grid[i + 1][j] != tcolor) and (j + 1 == input_grid.shape[1] or input_grid[i][j + 1] != tcolor):
                return (i, j)
    return (-1, -1)

def find_top_left(input_grid: np.ndarray, tcolor: int) -> Tuple[int, int]:
    """
    This function takes in a n*n grid with multiple color pixels and the color that appears consecutively the most. It returns the coordinates of the top-left pixel of the largest consecutive block of the most frequent color.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == tcolor and i + 1 < input_grid.shape[0] and (j + 1 < input_grid.shape[1]) and (input_grid[i + 1][j] == tcolor) and (input_grid[i][j + 1] == tcolor):
                return (i, j)
    return (-1, -1)

def find_consecutive_color(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes in a n*n grid with multiple color pixels and returns the color that appears consecutively the most and the number of times it appears consecutively.
    """
    max_consecutive_count = 0
    max_consecutive_color = None
    for row in input_grid:
        consecutive_count = 1
        for i in range(1, len(row)):
            if row[i] == row[i - 1]:
                consecutive_count += 1
            else:
                if consecutive_count > max_consecutive_count:
                    max_consecutive_count = consecutive_count
                    max_consecutive_color = row[i - 1]
                consecutive_count = 1
        if consecutive_count > max_consecutive_count:
            max_consecutive_count = consecutive_count
            max_consecutive_color = row[-1]
    return (max_consecutive_color, max_consecutive_count)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    (tcolor, tcnt) = find_consecutive_color(input_grid)
    (lux, luy) = find_top_left(input_grid, tcolor)
    (lbx, lby) = find_bottom_right(input_grid, tcolor, lux, luy)
    ans_grid = get_subgrid(input_grid, lux, luy, lbx, lby, tcnt)
    return ans_grid