import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_black_pixels_red(input_grid: np.ndarray) -> np.ndarray:
    """
    This function takes in a numpy array representing an image grid and colors the black pixels red, whose left and right
    neighbors are both blue. It returns the modified image grid as a numpy array.
    
    Args:
    input_grid: A numpy array representing an image grid
    
    Returns:
    A numpy array representing the modified image grid
    """
    output_grid = np.copy(input_grid)
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i][j] == black:
                if j > 0 and j < output_grid.shape[1] - 1 and (output_grid[i][j - 1] == blue) and (output_grid[i][j + 1] == blue):
                    output_grid[i][j] = red
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = color_black_pixels_red(input_grid)
    return output_grid