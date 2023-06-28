import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def set_orange_around_position(input_grid: np.ndarray, positions: List[Tuple[int, int]]) -> np.ndarray:
    """
    Sets the elements in up, down, left and right of input positions to orange in input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    positions: A list of tuples representing the positions in the input grid.
    
    Returns:
    A numpy array representing the input grid with orange elements around the input positions.
    """
    for (i, j) in positions:
        if i > 0:
            input_grid[i - 1][j] = orange
        if i < input_grid.shape[0] - 1:
            input_grid[i + 1][j] = orange
        if j > 0:
            input_grid[i][j - 1] = orange
        if j < input_grid.shape[1] - 1:
            input_grid[i][j + 1] = orange
    return input_grid

def set_yellow_around_position(input_grid: np.ndarray, positions: List[Tuple[int, int]]) -> np.ndarray:
    """
    Sets the elements in up-left, up-right, down-left and down-right of input positions to yellow in input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    positions: A list of tuples representing the positions in the input grid.
    
    Returns:
    A numpy array representing the input grid with yellow elements around the input positions.
    """
    for (i, j) in positions:
        if i > 0 and j > 0:
            input_grid[i - 1][j - 1] = yellow
        if i > 0 and j < input_grid.shape[1] - 1:
            input_grid[i - 1][j + 1] = yellow
        if i < input_grid.shape[0] - 1 and j > 0:
            input_grid[i + 1][j - 1] = yellow
        if i < input_grid.shape[0] - 1 and j < input_grid.shape[1] - 1:
            input_grid[i + 1][j + 1] = yellow
    return input_grid

def find_blue_positions(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Returns a list of tuples representing the positions of all blue elements in the input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples representing the positions of all blue elements in the input grid.
    """
    blue_positions = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                blue_positions.append((i, j))
    return blue_positions

def find_red_positions(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Returns a list of tuples representing the positions of all red elements in the input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples representing the positions of all red elements in the input grid.
    """
    red_positions = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                red_positions.append((i, j))
    return red_positions

def identity(input_grid: np.ndarray) -> np.ndarray:
    """
    Returns the input grid as is.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the input grid.
    """
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = identity(input_grid)
    red_positions = find_red_positions(input_grid)
    blue_positions = find_blue_positions(input_grid)
    output_grid = set_yellow_around_position(output_grid, red_positions)
    output_grid = set_orange_around_position(output_grid, blue_positions)
    return output_grid