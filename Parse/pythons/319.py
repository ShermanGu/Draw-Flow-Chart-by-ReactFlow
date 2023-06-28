import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_grid(input_grid: np.ndarray) -> np.ndarray:
    """
    Traverse each column, count how many red pixels are in each column. Divide this number by 2 and denote it as cnt. Change the cnt pixels at the bottom of the column to teal. Return the changed grid.
    """
    (height, width) = input_grid.shape
    for j in range(width):
        red_count = 0
        for i in range(height):
            if input_grid[i][j] == red:
                red_count += 1
        cnt = red_count // 2
        for i in range(height - 1, height - 1 - cnt, -1):
            input_grid[i][j] = teal
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    ngrid = change_grid(input_grid)
    return ngrid