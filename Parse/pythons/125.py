import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_bottom_pixel(p: List[Tuple[int, int]], input_grid: np.ndarray) -> np.ndarray:
    """
    This function takes in a numpy array representing an image and a list of tuples representing the coordinates
    of all black pixels that have at least 3 non-black neighbors. It colors the bottom pixel in the same column with 
    black pixel in yellow.
    
    Args:
    - p: a list of tuples representing the coordinates of all black pixels that have at least 3 non-black neighbors.
    - input_grid: a numpy array representing an image
    
    Returns:
    - A numpy array representing the image with the bottom pixel in the same column with black pixel in yellow.
    """
    for (i, j) in p:
        input_grid[-1][j] = yellow
    return input_grid

def find_black_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    This function takes in a numpy array representing an image and returns a list of tuples representing the coordinates
    of all black pixels that have at least 3 non-black neighbors.
    
    Args:
    - input_grid: a numpy array representing an image
    
    Returns:
    - A list of tuples representing the coordinates of all black pixels that have at least 3 non-black neighbors.
    """
    black_pixels = []
    for i in range(1, input_grid.shape[0] - 1):
        for j in range(1, input_grid.shape[1] - 1):
            if input_grid[i][j] == black:
                neighbors = [input_grid[i - 1][j], input_grid[i + 1][j], input_grid[i][j - 1], input_grid[i][j + 1]]
                if neighbors.count(black) == 1:
                    black_pixels.append((i, j))
    return black_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    p = find_black_pixels(input_grid)
    out = color_bottom_pixel(p, input_grid)
    return out