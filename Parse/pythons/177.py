import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def row_has_only_one_color(row: np.ndarray) -> bool:
    """
    Check if a given row has only one color.
    
    Args:
    row: A numpy array representing a row in the input grid.
    
    Returns:
    A boolean value indicating whether the row has only one color or not.
    """
    return len(set(row)) == 1

def traverse_grid(input_grid: np.ndarray) -> List[int]:
    """
    Traverse the grid from left to right and top to bottom, noting the order of different colors.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of integers representing the order of different colors in the grid.
    """
    color_list = []
    for row in input_grid:
        for color in row:
            if color not in color_list:
                color_list.append(color)
    return color_list

def main(input_grid: np.ndarray) -> np.ndarray:
    color_list = traverse_grid(input_grid)
    output_grid = np.array([color_list])
    if row_has_only_one_color(input_grid[0]):
        return output_grid.T
    else:
        return output_grid