import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_all_squares_to_color(input_grid: np.ndarray, color: int) -> np.ndarray:
    """
    Given an input grid and a color, this function returns the grid with all squares changed to the input color.
    
    Args:
    input_grid: A numpy array representing the input grid.
    color: An integer representing the input color.
    
    Returns:
    A numpy array representing the grid with all squares changed to the input color.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            input_grid[i][j] = color
    return input_grid

def find_num_non_black_squares(input_grid: np.ndarray) -> int:
    """
    Given an input grid, this function returns the number of non-black squares.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    An integer representing the number of non-black squares.
    """
    count = 0
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                count += 1
    return count

def find_non_black_color(input_grid: np.ndarray) -> int:
    """
    Given an input grid, this function returns the color of a non-black square.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    An integer representing the color of a non-black square.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                return input_grid[i][j]

def main(input_grid: np.ndarray) -> np.ndarray:
    color = find_non_black_color(input_grid)
    number = find_num_non_black_squares(input_grid)
    output_grid = np.zeros((1, number), dtype=int)
    output_grid = change_all_squares_to_color(output_grid, color)
    return output_grid