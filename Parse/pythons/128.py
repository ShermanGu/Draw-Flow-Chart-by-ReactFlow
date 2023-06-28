import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_grid_with_color(input_grid: np.ndarray, color: int) -> np.ndarray:
    """
    This function takes an input grid and a color and returns a new grid with all blocks filled with the given color.
    
    Args:
    input_grid: A numpy array representing the input grid.
    color: An integer representing the color to fill the grid with.
    
    Returns:
    A numpy array representing the output grid with all blocks filled with the given color.
    """
    output_grid = np.full_like(input_grid, color)
    return output_grid

def find_most_common_color(input_grid: np.ndarray) -> int:
    """
    This function takes an input grid and returns the most common color in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    An integer representing the most common color in the grid.
    """
    (colors, counts) = np.unique(input_grid, return_counts=True)
    return colors[np.argmax(counts)]

def main(input_grid: np.ndarray) -> np.ndarray:
    color = find_most_common_color(input_grid)
    output_grid = fill_grid_with_color(input_grid, color)
    return output_grid