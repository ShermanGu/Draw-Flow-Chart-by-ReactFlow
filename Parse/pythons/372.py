import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def swap_top_bottom_pixels_in_odd_columns(input_grid: np.ndarray) -> np.ndarray:
    """
    Swap the colors of the top and bottom pixels in every odd column (column number starting from 0).
    
    Args:
    input_grid: 2D numpy array representing the input grid
    
    Returns:
    2D numpy array representing the output grid with colors of top and bottom pixels swapped in odd columns
    """
    output_grid = np.copy(input_grid)
    (rows, cols) = input_grid.shape
    for c in range(1, cols, 2):
        for r in range(rows - 1):
            (output_grid[r][c], output_grid[r + 1][c]) = (output_grid[r + 1][c], output_grid[r][c])
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = swap_top_bottom_pixels_in_odd_columns(input_grid)
    return output_grid