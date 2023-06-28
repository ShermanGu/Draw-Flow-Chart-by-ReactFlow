import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_grey_pixels_blue(input_grid: np.ndarray, grey_pixels: List[Tuple[int, int]]) -> np.ndarray:
    """
    Given an input grid and a list of tuples containing the indices of all the grey pixels in the grid,
    turns each grey pixel and its 8 neighbors in the 3x3 area into blue.
    
    Args:
    input_grid: A numpy array representing the input grid.
    grey_pixels: A list of tuples containing the indices of all the grey pixels in the grid.
    
    Returns:
    A numpy array representing the updated grid.
    """
    for (i, j) in grey_pixels:
        for x in range(max(0, i - 1), min(input_grid.shape[0], i + 2)):
            for y in range(max(0, j - 1), min(input_grid.shape[1], j + 2)):
                input_grid[x][y] = blue
    return input_grid

def find_grey_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples containing the indices of all the grey pixels in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples containing the indices of all the grey pixels in the grid.
    """
    grey_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == grey:
                grey_pixels.append((i, j))
    return grey_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    p = find_grey_pixels(input_grid)
    out = turn_grey_pixels_blue(input_grid, p)
    return out