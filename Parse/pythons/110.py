import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_3x3_area_below_gray_pixel(input_grid: np.ndarray, x: int, y: int) -> np.ndarray:
    return input_grid[x + 1:x + 4, y - 1:y + 2]

def find_gray_pixel_coordinates(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes in a numpy array representing an image and returns the coordinates of the first gray pixel found.
    
    Args:
    input_grid: A numpy array representing an image.
    
    Returns:
    A tuple containing the x and y coordinates of the first gray pixel found.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == grey:
                return (i, j)
    return (-1, -1)

def main(input_grid: np.ndarray) -> np.ndarray:
    (x, y) = find_gray_pixel_coordinates(input_grid)
    output_grid = get_3x3_area_below_gray_pixel(input_grid, x, y)
    return output_grid