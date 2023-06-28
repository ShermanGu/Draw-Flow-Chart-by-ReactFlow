import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def _hole2(input_grid: np.ndarray, loc: Tuple[int, int]) -> int:
    (row, col) = loc
    symmetric_col = input_grid.shape[1] - 1 - col
    return input_grid[row][symmetric_col]

def change_pixel_color(output_grid: np.ndarray, loc: Tuple[int, int], color: int) -> np.ndarray:
    """
    Given an output grid, a location and a color, changes the color of the pixel at the given location to the given color.
    
    Args:
    output_grid: A numpy array representing the output grid.
    loc: A tuple representing the location of the pixel.
    color: An integer representing the new color of the pixel.
    
    Returns:
    A numpy array representing the output grid with the color of the pixel at the given location changed to the given color.
    """
    (row, col) = loc
    output_grid[row][col] = color
    return output_grid

def replace_yellow_pixels(input_grid: np.ndarray) -> np.ndarray:
    locs = find_yellow_pixels(input_grid)
    output_grid = input_grid
    for loc in locs:
        color = find_symmetric_pixel_color(input_grid, loc)
        if color is yellow:
            color = _hole2(input_grid, loc)
        output_grid = change_pixel_color(output_grid, loc, color)
    return output_grid

def find_symmetric_pixel_color(input_grid: np.ndarray, loc: Tuple[int, int]) -> int:
    """
    Given an input grid and a location, returns the color of the pixel which is symmetric above and below with the given location.
    
    Args:
    input_grid: A numpy array representing the input grid.
    loc: A tuple representing the location of the pixel.
    
    Returns:
    An integer representing the color of the pixel which is symmetric above and below with the given location.
    """
    (row, col) = loc
    symmetric_row = input_grid.shape[0] - 1 - row
    return input_grid[symmetric_row][col]

def find_yellow_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples representing the location of all pixels which are yellow.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples representing the location of all pixels which are yellow.
    """
    yellow_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == yellow:
                yellow_pixels.append((i, j))
    return yellow_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    locs = find_yellow_pixels(input_grid)
    output_grid = input_grid
    for loc in locs:
        color = find_symmetric_pixel_color(input_grid, loc)
        if color is yellow:
            color = replace_yellow_pixels(input_grid, loc)
        output_grid = change_pixel_color(output_grid, loc, color)
    return output_grid