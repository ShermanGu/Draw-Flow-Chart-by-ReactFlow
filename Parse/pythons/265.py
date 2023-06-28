import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_red_pixel_to_black(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function finds the first red pixel and turns it into black. 
    Then, it colors the neighboring pixels of the red pixel with specific colors and returns the updated grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the updated grid.
    """
    p = find_red_pixel(input_grid)
    input_grid[p[0]][p[1]] = black
    color = color_neighbors(p, input_grid)
    return color

def color_neighbors(p: Tuple[int, int], input_grid: np.ndarray) -> np.ndarray:
    """
    Given a pixel coordinate and an input grid, this function colors the neighboring pixels of the given pixel
    with specific colors and returns the updated grid.
    
    Args:
    p: A tuple containing the row and column indices of the pixel to be colored.
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the updated grid.
    """
    if p[0] > 0:
        if p[1] > 0:
            input_grid[p[0] - 1][p[1] - 1] = green
        if p[1] < input_grid.shape[1] - 1:
            input_grid[p[0] - 1][p[1] + 1] = pink
    if p[0] < input_grid.shape[0] - 1:
        if p[1] > 0:
            input_grid[p[0] + 1][p[1] - 1] = teal
        if p[1] < input_grid.shape[1] - 1:
            input_grid[p[0] + 1][p[1] + 1] = orange
    return input_grid

def find_red_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given an input grid, this function returns the coordinates of the first red pixel found.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A tuple containing the row and column indices of the first red pixel found.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                return (i, j)

def main(input_grid: np.ndarray) -> np.ndarray:
    p = find_red_pixel(input_grid)
    color = color_neighbors(p, input_grid)
    out = turn_red_pixel_to_black(color)
    return out