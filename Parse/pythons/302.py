import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_rows_and_columns(input_grid: np.ndarray, ngrid: np.ndarray) -> np.ndarray:
    """
    Traverse each row in the inputgrid, if the row is all black, paint the corresponding row in the ngrid red.
    Traverse each column in inputgrid, if the column is all black, paint the corresponding column in ngrid red.
    """
    for i in range(input_grid.shape[0]):
        if np.all(input_grid[i] == black):
            ngrid[i] = red
    for j in range(input_grid.shape[1]):
        if np.all(input_grid[:, j] == black):
            ngrid[:, j] = red
    return ngrid

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    ngrid = input_grid.copy()
    ans_grid = paint_rows_and_columns(input_grid, ngrid)
    return ans_grid