import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_green_pixel_to_teal(grid: np.ndarray, i: int, j: int) -> np.ndarray:
    """
    Color the green pixel to teal.
    
    Args:
    - grid (np.ndarray): the input grid
    - i (int): the row index of the pixel
    - j (int): the column index of the pixel
    
    Returns:
    - np.ndarray: the updated grid with the green pixel colored to teal
    """
    grid[i][j] = teal
    return grid

def is_green_with_adjacent_green_pixel(pixel: int, i: int, j: int, grid: np.ndarray) -> bool:
    """
    Check if a pixel is green and has another green pixel on top or down or left on right.
    
    Args:
    - pixel (int): the value of the pixel to check
    - i (int): the row index of the pixel
    - j (int): the column index of the pixel
    - grid (np.ndarray): the input grid
    
    Returns:
    - bool: True if the pixel is green and has another green pixel on top or down or left on right, False otherwise
    """
    if pixel == green:
        if i > 0 and grid[i - 1][j] == green:
            return True
        if i < grid.shape[0] - 1 and grid[i + 1][j] == green:
            return True
        if j > 0 and grid[i][j - 1] == green:
            return True
        if j < grid.shape[1] - 1 and grid[i][j + 1] == green:
            return True
    return False

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you can see some green pixels in the grid,                                                                                                            
    The output is the same size as the input.                                                                                                                           
    To make the output, if a green pixel has another green pixel on top or down or left on right, color the pixel to teal.                                              
    """
    output_grid = input_grid.copy()
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if is_green_with_adjacent_green_pixel(output_grid[i][j], i, j, input_grid):
                output_grid = color_green_pixel_to_teal(output_grid, i, j)
    return output_grid