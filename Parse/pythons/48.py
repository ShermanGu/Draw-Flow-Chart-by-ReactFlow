import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_sub_grid_with_color(input_grid: np.ndarray, color: int) -> np.ndarray:
    """
    This function takes an input grid and a color and returns a sub grid that contains the corresponding color in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    color: An integer representing the color to be searched in the grid.
    
    Returns:
    A numpy array representing the sub grid that contains the corresponding color in the grid.
    """
    sub_grid = np.where(input_grid == color, color, -1)
    sub_grid = sub_grid[sub_grid != -1]
    sub_grid = sub_grid.reshape(int(len(sub_grid) ** 0.5), int(len(sub_grid) ** 0.5))
    return sub_grid

def find_least_common_color(input_grid: np.ndarray) -> int:
    """
    This function takes an input grid and returns the least common color in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    An integer representing the least common color in the grid.
    """
    (unique, counts) = np.unique(input_grid, return_counts=True)
    color_counts = dict(zip(unique, counts))
    least_common_color = min(color_counts, key=color_counts.get)
    return least_common_color

def main(input_grid: np.ndarray) -> np.ndarray:
    color = find_least_common_color(input_grid)
    sub_grid = find_sub_grid_with_color(input_grid, color)
    return sub_grid