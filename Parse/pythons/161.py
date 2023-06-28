import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_rectangles_with_blue(input_grid: np.ndarray, rectangles: List[Tuple[int, int]]) -> np.ndarray:
    """
    This function takes an input grid and a list of tuples representing the top-left corner of a 3x3 rectangle filled with black in the input grid. It returns a new grid where the 3x3 rectangles are filled with blue.
    
    Args:
    input_grid: A numpy array representing the input grid
    rectangles: A list of tuples, where each tuple represents the top-left corner of a 3x3 rectangle filled with black in the input grid.
    
    Returns:
    A numpy array representing the output grid where the 3x3 rectangles are filled with blue.
    """
    output_grid = input_grid.copy()
    for rectangle in rectangles:
        (i, j) = rectangle
        output_grid[i:i + 3, j:j + 3] = blue
    return output_grid

def find_black_rectangles(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    This function takes an input grid and returns a list of tuples, where each tuple represents the top-left corner of a 3x3 rectangle filled with black in the input grid.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A list of tuples, where each tuple represents the top-left corner of a 3x3 rectangle filled with black in the input grid.
    """
    black_rectangles = []
    for i in range(input_grid.shape[0] - 2):
        for j in range(input_grid.shape[1] - 2):
            if np.all(input_grid[i:i + 3, j:j + 3] == black):
                black_rectangles.append((i, j))
    return black_rectangles

def identity(input_grid: np.ndarray) -> np.ndarray:
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = identity(input_grid)
    rectangles = find_black_rectangles(input_grid)
    output_grid = fill_rectangles_with_blue(input_grid, rectangles)
    return output_grid