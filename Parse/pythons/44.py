import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_lines(input_grid: np.ndarray) -> np.ndarray:
    """
    For each line in the input grid, if the start of the line is non-zero and equal to the end of the line,
    fill the line with the start element.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the output grid with filled lines.
    """
    output_grid = np.copy(input_grid)
    for i in range(output_grid.shape[0]):
        if output_grid[i, 0] != 0 and output_grid[i, 0] == output_grid[i, -1]:
            output_grid[i, :] = output_grid[i, 0]
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = fill_lines(input_grid)
    return output_grid