import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_upper_right_corner_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function returns a 3x3 numpy array containing the nine pixels in the upper right corner.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A 3x3 numpy array containing the nine pixels in the upper right corner.
    """
    return input_grid[:3, -3:]

def main(input_grid: np.ndarray) -> np.ndarray:
    out = np.zeros((3, 3), dtype=int)
    out = find_upper_right_corner_pixels(input_grid)
    return out