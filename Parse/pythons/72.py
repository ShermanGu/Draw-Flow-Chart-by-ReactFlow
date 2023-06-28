import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_downmost_grey_pixel(blue_pixel: Tuple[int, int], grid: np.ndarray) -> Tuple[int, int]:
    """
    Given a blue pixel and a grid, returns the downmost grey pixel in the same column as the blue pixel.
    
    Args:
    - blue_pixel: a tuple representing the indices of a blue pixel in the grid.
    - grid: a numpy array representing the grid
    
    Returns:
    - A tuple representing the indices of the downmost grey pixel in the same column as the blue pixel.
    """
    for i in range(grid.shape[0] - 1, blue_pixel[0], -1):
        if grid[i][blue_pixel[1]] == grey:
            return (i, blue_pixel[1])
    return blue_pixel

def find_blue_pixels(grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given a grid, returns a list of indices of blue pixels in the grid.
    
    Args:
    - grid: a numpy array representing the grid
    
    Returns:
    - A list of tuples representing the indices of blue pixels in the grid.
    """
    blue_pixels = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == blue:
                blue_pixels.append((i, j))
    return blue_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    find the blue pixels, color the downmost grey pixels that in the same column of the blue pixels to blue, and color origin blue pixels to black.
    """
    output_grid = input_grid.copy()
    blue_pixels = find_blue_pixels(output_grid)
    for blue_pixel in blue_pixels:
        downmost_grey_pixel = find_downmost_grey_pixel(blue_pixel, output_grid)
        output_grid[downmost_grey_pixel[0], downmost_grey_pixel[1]] = blue
        output_grid[blue_pixel[0], blue_pixel[1]] = black
    return output_grid