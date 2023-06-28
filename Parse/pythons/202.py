import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def swap_colors_according_to_order(input_grid: np.ndarray, color_order: List[int]) -> np.ndarray:
    """
    This function takes in a numpy array representing a grid of colors and a list of integers representing the order of
    colors along the middle column of the grid. It returns a numpy array with the colors of the pixels swapped according
    to the given order.
    
    Args:
    - input_grid: a numpy array of shape (n, m) representing a grid of colors, where n is the number of rows and m is the
    number of columns
    - color_order: a list of integers representing the order of colors along the middle column of the grid
    
    Returns:
    - A numpy array with the colors of the pixels swapped according to the given order.
    """
    color_map = {color_order[i]: color_order[-i - 1] for i in range(len(color_order))}
    output_grid = np.vectorize(color_map.get)(input_grid)
    return output_grid

def record_middle_column_color_order(input_grid: np.ndarray) -> List[int]:
    """
    This function takes in a numpy array representing a grid of colors and returns a list of integers representing the
    order of colors along the middle column of the grid. If a color already exists, it is ignored.
    
    Args:
    - input_grid: a numpy array of shape (n, m) representing a grid of colors, where n is the number of rows and m is the
    number of columns
    
    Returns:
    - A list of integers representing the order of colors along the middle column of the grid.
    """
    middle_column = input_grid[:, input_grid.shape[1] // 2]
    color_order = []
    for color in middle_column:
        if color not in color_order:
            color_order.append(color)
    return color_order

def main(input_grid: np.ndarray) -> np.ndarray:
    r = record_middle_column_color_order(input_grid)
    out = swap_colors_according_to_order(input_grid, r)
    return out