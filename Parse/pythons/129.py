import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def highest_frequency_number(grid: np.ndarray) -> int:
    """
    Given a 3x3 grid of integers, returns the integer that appears most frequently in the grid.
    
    Args:
    grid: A 3x3 numpy array of integers
    
    Returns:
    The integer that appears most frequently in the grid.
    """
    flat_grid = grid.flatten()
    (unique, counts) = np.unique(flat_grid, return_counts=True)
    return unique[np.argmax(counts)]

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            output_grid[i][j] = highest_frequency_number(input_grid[3 * i:3 * i + 3, 3 * j:3 * j + 3])
    return output_grid