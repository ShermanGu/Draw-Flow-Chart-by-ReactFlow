import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_output(output: np.ndarray, color_grid: np.ndarray) -> np.ndarray:
    """
    Colors the output grid according to the color grid.

    Args:
    output: A 4x4 numpy array representing the output grid.
    color_grid: A 4x4 numpy array representing the color grid.

    Returns:
    A 4x4 numpy array with colored cells.
    """
    for i in range(4):
        for j in range(4):
            if color_grid[i][j] != black:
                output[i][j] = color_grid[i][j]
    return output

def separate_grids(input):
    grids = []
    for i in range(2):
        for j in range(2):
            grid = input[i * 5:(i + 1) * 5 - 1, j * 5:(j + 1) * 5 - 1]
            grids.append(grid)
    return grids

def main(input_grid):
    grids = separate_grids(input_grid)
    output = np.zeros((4, 4), dtype=np.int32)
    for i in range(4):
        output = color_output(output, grids[3 - i])
    return output