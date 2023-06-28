import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    find the black pixel that its left pixel, top pixel, left top pixel are all the same color except black, return a 1x1 pixel of that color.
    """
    color = 0
    for row in range(1, input_grid.shape[0] - 1):
        for col in range(1, input_grid.shape[1] - 1):
            left_color = input_grid[row][col - 1]
            top_color = input_grid[row - 1][col]
            left_top_color = input_grid[row - 1][col - 1]
            if left_color == top_color and left_color == left_top_color and (left_color != black):
                color = left_color
    return np.array([[color]])