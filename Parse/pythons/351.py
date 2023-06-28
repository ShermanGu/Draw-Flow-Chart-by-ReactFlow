import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_adjacent_black_grids(input_grid: np.ndarray, red_grids: List[Tuple[int, int]]) -> np.ndarray:
    """
    This function takes in a numpy array as input_grid and a list of tuples containing the positions of all the red grids in the input as red_grids.
    It colors all black grids(diagonally adjacent included) that are adjacent to the red grids with blue.
    
    Args:
    input_grid: A numpy array representing the input grid
    red_grids: A list of tuples containing the positions of all the red grids in the input.
    
    Returns:
    A numpy array with the black grids adjacent to the red grids colored blue.
    """
    blue_grids = []
    for (r, c) in red_grids:
        for i in range(r - 1, r + 2):
            for j in range(c - 1, c + 2):
                if i >= 0 and j >= 0 and (i < input_grid.shape[0]) and (j < input_grid.shape[1]) and (input_grid[i][j] == black):
                    input_grid[i][j] = blue
                    blue_grids.append((i, j))
    return input_grid

def find_red_grids(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    This function takes in a numpy array as input_grid and returns a list of tuples containing the positions of all the red grids in the input.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A list of tuples containing the positions of all the red grids in the input.
    """
    red_grids = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                red_grids.append((i, j))
    return red_grids

def main(input_grid: np.ndarray) -> np.ndarray:
    red_grids = find_red_grids(input_grid)
    output = color_adjacent_black_grids(input_grid, red_grids)
    return output