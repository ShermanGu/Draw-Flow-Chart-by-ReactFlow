import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def expand_blocks(input_grid: np.ndarray) -> np.ndarray:
    """
    Given a 2D numpy array representing a grid of colored blocks, this function expands each block in the grid to a
    square of four blocks.

    Args:
    - input_grid (np.ndarray): a 2D numpy array representing a grid of colored blocks, where each element is an integer
                               representing a color

    Returns:
    - np.ndarray: a 2D numpy array representing the expanded grid, where each element is an integer representing a color
    """
    output = np.repeat(np.repeat(input_grid, 2, axis=1), 2, axis=0)
    return output

def find_smallest_rectangle(input_grid: np.ndarray) -> np.ndarray:
    """
    Given a 2D numpy array representing a grid of colored blocks, this function finds the smallest rectangle that can
    contain all the yellow blocks in the grid.

    Args:
    - input_grid (np.ndarray): a 2D numpy array representing a grid of colored blocks, where each element is an integer
                               representing a color

    Returns:
    - np.ndarray: a 2D numpy array representing the smallest rectangle that can contain all the yellow blocks in the grid,
                  where each element is an integer representing a color
    """
    yellow_indices = np.where(input_grid == yellow)
    (min_row, max_row) = (np.min(yellow_indices[0]), np.max(yellow_indices[0]))
    (min_col, max_col) = (np.min(yellow_indices[1]), np.max(yellow_indices[1]))
    output = input_grid[min_row:max_row + 1, min_col:max_col + 1]
    return output

def main(input_grid: np.ndarray) -> np.ndarray:
    output = find_smallest_rectangle(input_grid)
    output = expand_blocks(output)
    return output