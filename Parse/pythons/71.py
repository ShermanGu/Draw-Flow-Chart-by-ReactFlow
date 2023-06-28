import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def process_pixels(input_grid: np.ndarray, mindex: int, ngrid: np.ndarray) -> np.ndarray:
    """
    Traverse all pixels whose row number is less than mindex in inputgrid, set the pixel coordinates as (x, y),
    if the value of the pixel is the same as the value of (x + mindex + 1, y), then change the value of ngrid (x, y) to zero;
    change to green if different.
    Return the ngrid
    """
    for i in range(mindex):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == input_grid[i + mindex + 1][j]:
                ngrid[i][j] = 0
            else:
                ngrid[i][j] = green
    return ngrid

def find_yellow_line_index(input_grid: np.ndarray) -> int:
    """
    This function takes in a n*n grid with multiple color pixels and returns the index of the first yellow line found.
    """
    for i in range(input_grid.shape[0]):
        if np.array_equal(input_grid[i], np.array([yellow] * input_grid.shape[1])):
            return i
    return -1

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    mindex = find_yellow_line_index(input_grid)
    ngrid = np.zeros((input_grid.shape[0] // 2, input_grid.shape[1]))
    ans_grid = process_pixels(input_grid, mindex, ngrid)
    return ans_grid