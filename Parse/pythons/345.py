import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_surrounded_element(input_grid: np.ndarray) -> int:
    """
    Given a 2D numpy array, this function finds the non-zero element that is surrounded by other non-zero elements.
    
    Args:
    input_grid: A 2D numpy array of integers
    
    Returns:
    An integer representing the non-zero element that is surrounded by other non-zero elements. If no such element is found, returns -1.
    """
    (rows, cols) = input_grid.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if input_grid[i][j] != 0:
                if input_grid[i - 1][j] != 0 and input_grid[i + 1][j] != 0 and (input_grid[i][j - 1] != 0) and (input_grid[i][j + 1] != 0):
                    return input_grid[i][j]
    return -1

def main(input_grid: np.ndarray) -> np.ndarray:
    surround_element = find_surrounded_element(input_grid)
    return np.array([[surround_element]])