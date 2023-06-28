import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_empty_grid() -> np.ndarray:
    return np.zeros((3, 3), dtype=int)

def find_top_row(input_grid: np.ndarray, color: int) -> int:
    for row in range(input_grid.shape[0]):
        if color in input_grid[row]:
            return row
    return -1

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see some grey pixels and teal pixels.
    The output grid is 3x3
    find the row of the topest grey pixel, and the row of the topeset teal pixel, and compute the abs dist between the two.
    color the output grid with teal according to the abs dist,
    the way is first color first row from left to right, if the pixels are not enough, then color next row from right to left, then left to right, then right to left, etc. 
    """
    row_topest_grey = find_top_row(input_grid, grey)
    row_topest_teal = find_top_row(input_grid, teal)
    dist = abs(row_topest_grey - row_topest_teal)
    output_grid = make_empty_grid()
    row = 0
    col = 0
    dict = 1
    while dist > 0:
        output_grid[row][col] = teal
        col += dict
        dist -= 1
        if col == 2 or col == 0:
            row += 1
            dict = -dict
    return output_grid