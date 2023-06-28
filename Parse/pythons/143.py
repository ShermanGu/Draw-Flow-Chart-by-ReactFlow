import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_green_with_black(input_grid: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    """
    This function replaces any green pixel in the output grid with black if there is a red pixel in the corresponding position in the bottom 4x4 grid of the input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    output_grid: A numpy array representing the modified input grid.
    
    Returns:
    A numpy array representing the final modified input grid.
    """
    bottom_grid = input_grid[-4:, :]
    for i in range(4):
        for j in range(4):
            if output_grid[i, j] == green and bottom_grid[i, j] == red:
                output_grid[i, j] = black
    return output_grid

def fill_colors(input_grid: np.ndarray) -> np.ndarray:
    """
    This function fills in the black pixels with green and changes all the orange pixels to black.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the modified input grid.
    """
    output_grid = input_grid.copy()
    output_grid[output_grid == black] = green
    output_grid[output_grid == orange] = black
    return output_grid

def copy_top_4_rows(input_grid: np.ndarray) -> np.ndarray:
    """
    This function copies the top 4 rows of the input grid and returns it as a new numpy array.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the top 4 rows of the input grid.
    """
    return input_grid[:4, :]

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see...orange, yellow, and red pixels in different shapes.                                                                                  
    The output grid size...is smaller. Make it 4x4.                                                                                                                     
    To make the output, you have to...only use the 4x4 grid that is at the top of the input grid where only the orange pixels are. Fill in the black pixels with green. 
    """
    output_grid = copy_top_4_rows(input_grid)
    output_grid = fill_colors(output_grid)
    output_grid = replace_green_with_black(input_grid, output_grid)
    return output_grid