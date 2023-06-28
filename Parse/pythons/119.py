import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_non_black_cells(input_grid):
    """
    Traverse every position of input. For every position which is not black, if all of the four connected positions of it are not black, change the position to teal.
    """
    (rows, cols) = input_grid.shape
    output_grid = np.copy(input_grid)
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] != black:
                if i > 0 and j > 0 and (i < rows - 1) and (j < cols - 1):
                    if input_grid[i - 1][j] != black and input_grid[i + 1][j] != black and (input_grid[i][j - 1] != black) and (input_grid[i][j + 1] != black):
                        output_grid[i][j] = teal
    return output_grid

def main(input_grid):
    output = color_non_black_cells(input_grid)
    return output