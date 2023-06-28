import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def extend_upmost_green_pixel_left(input_grid: np.ndarray) -> np.ndarray:
    """
    Extend only the up most green pixel to the left until it meets a non-black pixel
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the output grid with the up most green pixel extended to the left
    """
    output_grid = np.copy(input_grid)
    for j in range(output_grid.shape[1]):
        for i in range(output_grid.shape[0]):
            if output_grid[i][j] == green:
                k = j - 1
                while k >= 0 and output_grid[i][k] == black:
                    k -= 1
                output_grid[i][k + 1:j + 1] = green
                break
    return output_grid

def extend_rightmost_green_pixel_up(input_grid: np.ndarray) -> np.ndarray:
    """
    Extend only the rightmost green pixel to the up until it meets a non-black pixel
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the output grid with the rightmost green pixel extended to the up
    """
    output_grid = np.copy(input_grid)
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1] - 1, -1, -1):
            if output_grid[i][j] == green:
                k = i - 1
                while k >= 0 and output_grid[k][j] == black:
                    k -= 1
                output_grid[k + 1:i + 1, j] = green
                break
    return output_grid

def extend_green_pixel(input_grid: np.ndarray) -> np.ndarray:
    """
    Extend the green pixel to the right until it meets a non-black pixel
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the output grid with the green pixel extended to the right
    """
    output_grid = np.copy(input_grid)
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i][j] == green:
                k = j + 1
                while k < output_grid.shape[1] and output_grid[i][k] == black:
                    k += 1
                output_grid[i][j:k] = green
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = extend_green_pixel(input_grid)
    output_grid = extend_rightmost_green_pixel_up(output_grid)
    output_grid = extend_upmost_green_pixel_left(output_grid)
    return output_grid