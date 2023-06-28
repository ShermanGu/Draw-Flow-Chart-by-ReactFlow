import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def traverse_yellow_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    Traverse yellow pixel in the whole input, turn it to grey first, and then move it to the left until touch the grey pixels.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the output grid with yellow pixels traversed and moved to the left.
    """
    output_grid = input_grid.copy()
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i][j] == yellow:
                output_grid[i][j] = grey
                k = j
                while k > 0 and output_grid[i][k - 1] != grey:
                    k -= 1
                (output_grid[i][j], output_grid[i][k]) = (output_grid[i][k], output_grid[i][j])
    return output_grid

def turn_yellow_to_grey(input_grid: np.ndarray) -> np.ndarray:
    """
    Traverse yellow pixel in the left 6 columns, turn every yellow pixel to grey.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the output grid with yellow pixels turned to grey.
    """
    output_grid = input_grid.copy()
    for i in range(output_grid.shape[0]):
        for j in range(6):
            if output_grid[i][j] == yellow:
                output_grid[i][j] = grey
    return output_grid

def move_yellow_pixels_right(input_grid: np.ndarray) -> np.ndarray:
    """
    Traverse yellow pixel in the left 6 columns, move every yellow pixel to the right until touch the grey pixels.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the output grid with yellow pixels moved to the right.
    """
    output_grid = input_grid.copy()
    for i in range(output_grid.shape[0]):
        for j in range(6):
            if output_grid[i][j] == yellow:
                k = j
                while k < output_grid.shape[1] - 1 and output_grid[i][k + 1] != grey:
                    k += 1
                (output_grid[i][j], output_grid[i][k]) = (output_grid[i][k], output_grid[i][j])
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = move_yellow_pixels_right(input_grid)
    output_grid = turn_yellow_to_grey(output_grid)
    output_grid = traverse_yellow_pixels(output_grid)
    return output_grid