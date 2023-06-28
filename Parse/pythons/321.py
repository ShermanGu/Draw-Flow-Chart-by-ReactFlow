import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_blocks_below(input_grid: np.ndarray, x: int, y: int) -> np.ndarray:
    """
    This function takes a numpy array and the indexes of a colored block as input and fills the blocks below it with its color.
    
    Args:
    input_grid: A numpy array representing the input grid.
    x: An integer representing the row index of the colored block.
    y: An integer representing the column index of the colored block.
    
    Returns:
    A numpy array with the blocks below the colored block filled with its color.
    """
    color = input_grid[x][y]
    for i in range(x + 1, input_grid.shape[0]):
        if input_grid[i][y] == black:
            input_grid[i][y] = color
        else:
            break
    return input_grid

def find_non_black_indexes(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    This function takes a numpy array as input and returns a list of tuples containing the indexes of non-black blocks in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples containing the indexes of non-black blocks in the grid.
    """
    non_black_indexes = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                non_black_indexes.append((i, j))
    return non_black_indexes

def main(input_grid: np.ndarray) -> np.ndarray:
    colored_index_list = find_non_black_indexes(input_grid)
    for (x, y) in colored_index_list:
        input_grid = fill_blocks_below(input_grid, x, y)
    return input_grid