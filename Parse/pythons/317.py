import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_pixels(input_grid: np.ndarray, mindex: int, ngrid: np.ndarray) -> np.ndarray:
    """
    Traverse all pixels in the inputgrid whose line number is less than mindex, if the value of the pixel is black and t
    """
    for i in range(mindex):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == black and input_grid[min(i + mindex + 1, input_grid.shape[0] - 1)][j] == black:
                ngrid[i][j] = black
            else:
                ngrid[i][j] = green
    return ngrid

def find_yellow_line_index(input_grid: np.ndarray) -> int:
    """
    This function takes in a numpy array of shape (n,m) and returns the index of the first row that contains a yellow pixel.
    """
    for i in range(input_grid.shape[0]):
        if yellow in input_grid[i]:
            return i
    return -1

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*m grid with multiple color pixels.
    """
    mindex = find_yellow_line_index(input_grid)
    ngrid = np.zeros((input_grid.shape[0] // 2, input_grid.shape[1]))
    ans_grid = color_pixels(input_grid, mindex, ngrid)
    return ans_grid