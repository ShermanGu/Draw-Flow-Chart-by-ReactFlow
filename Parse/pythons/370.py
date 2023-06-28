import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def draw_green_cross(input_grid: np.ndarray, x: int, y: int) -> np.ndarray:
    """
    Given a 2D numpy array, draw a green cross of length 3 centered on (x,y).
    
    Args:
    input_grid: A 2D numpy array representing the input grid.
    x: An integer representing the x-coordinate of the center of the cross.
    y: An integer representing the y-coordinate of the center of the cross.
    
    Returns:
    A 2D numpy array representing the output grid with the green cross drawn on it.
    """
    output_grid = input_grid.copy()
    output_grid[x, y - 1:y + 2] = green
    output_grid[x - 1:x + 2, y] = green
    return output_grid

def find_middle_point(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given a 2D numpy array, find the middle point of two blue pixels in the grid.
    
    Args:
    input_grid: A 2D numpy array representing the input grid.
    
    Returns:
    A tuple of two integers representing the middle point of two blue pixels in the grid.
    """
    (rows, cols) = input_grid.shape
    blue_pixels = []
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == blue:
                blue_pixels.append((i, j))
    ((x1, y1), (x2, y2)) = blue_pixels
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    return (x, y)

def main(input_grid: np.ndarray) -> np.ndarray:
    (x, y) = find_middle_point(input_grid)
    output_grid = draw_green_cross(input_grid, x, y)
    return output_grid