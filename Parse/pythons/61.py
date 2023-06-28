import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_black_pixels_green(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, returns a numpy ndarray representing the grid with all black pixels filled with green color.
    
    Args:
    - input_grid: a numpy ndarray representing the input grid
    
    Returns:
    - a numpy ndarray representing the grid with all black pixels filled with green color
    """
    output_grid = input_grid.copy()
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i][j] == black:
                output_grid[i][j] = green
    return output_grid

def fill_blue_pixels(new_blue_pixels: List[Tuple[int, int]], output_grid: np.ndarray) -> np.ndarray:
    """
    Given a list of tuples representing the coordinates of blue pixels in a grid and a numpy ndarray representing the output grid,
    fills all the new blue pixels with blue color.
    
    Args:
    - new_blue_pixels: a list of tuples representing the coordinates of blue pixels in a grid after shifting
    - output_grid: a numpy ndarray representing the output grid
    
    Returns:
    - a numpy ndarray representing the output grid with all new blue pixels filled with blue color
    """
    for pixel in new_blue_pixels:
        output_grid[pixel[0]][pixel[1]] = blue
    return output_grid

def shift_blue_pixels(blue_pixels: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Given a list of tuples representing the coordinates of blue pixels in a grid, returns a new list of tuples
    where the row coordinates remain the same and the column coordinates are shifted by 11 minus the original column coordinate.
    
    Args:
    - blue_pixels: a list of tuples representing the coordinates of blue pixels in a grid
    
    Returns:
    - a new list of tuples where the row coordinates remain the same and the column coordinates are shifted by 11 minus the original column coordinate
    """
    new_blue_pixels = []
    for pixel in blue_pixels:
        new_col = 11 - pixel[1]
        new_blue_pixels.append((pixel[0], new_col))
    return new_blue_pixels

def find_blue_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples representing the coordinates of all blue pixels in the grid.
    
    Args:
    - input_grid: a numpy ndarray representing the input grid
    
    Returns:
    - a list of tuples representing the coordinates of all blue pixels in the grid
    """
    blue_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                blue_pixels.append((i, j))
    return blue_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid.copy()
    blue_pixels = find_blue_pixels(input_grid)
    new_blue_pixels = shift_blue_pixels(blue_pixels)
    output_grid = fill_blue_pixels(new_blue_pixels, output_grid)
    output_grid = make_black_pixels_green(output_grid)
    return output_grid