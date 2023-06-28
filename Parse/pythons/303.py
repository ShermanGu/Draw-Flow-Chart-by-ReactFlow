import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def generate_new_grid(input_grid: np.ndarray, mcolor: int) -> np.ndarray:
    """
    This function generates a new grid based on the input grid and the most common color.
    It traverses the input grid, and if the pixel (x, y) color is mcolor, then it uses (3*x, 3*y) as the upper left corn

    Args:
    input_grid: A numpy array representing the input grid
    mcolor: An integer representing the most common color in the input grid

    Returns:
    A numpy array representing the new grid
    """
    new_grid = np.zeros((input_grid.shape[0] * 3, input_grid.shape[1] * 3))
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == mcolor:
                new_grid[3 * i:3 * i + 3, 3 * j:3 * j + 3] = input_grid
    return new_grid

def get_most_common_color(input_grid: np.ndarray) -> int:
    """
    This function takes an input grid and returns the color with the most occurrences in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    An integer representing the color with the most occurrences in the input grid.
    """
    color_counts = np.bincount(input_grid.flatten())
    return np.argmax(color_counts)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    mcolor = get_most_common_color(input_grid)
    ans_grid = generate_new_grid(input_grid, mcolor)
    return ans_grid