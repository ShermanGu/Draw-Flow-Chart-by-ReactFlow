import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_block(input_grid: np.ndarray, max_row: int, min_row: int, max_col: int, min_col: int) -> np.ndarray:
    """
    Given an input grid and the maximum row, minimum row, maximum column, and minimum column of a block, 
    returns the block as a numpy ndarray.
    
    Args:
    - input_grid: a numpy ndarray representing the input grid
    - max_row: an integer representing the maximum row of the block
    - min_row: an integer representing the minimum row of the block
    - max_col: an integer representing the maximum column of the block
    - min_col: an integer representing the minimum column of the block
    
    Returns:
    - a numpy ndarray representing the block
    """
    return input_grid[min_row:max_row + 1, min_col:max_col + 1]

def get_positions_bounds(positions: List[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    """
    Given a list of positions, returns the maximum row, minimum row, maximum column, and minimum column of the positions.
    
    Args:
    - positions: a list of tuples representing positions
    
    Returns:
    - a tuple of four integers representing the maximum row, minimum row, maximum column, and minimum column of the positions
    """
    max_row = max(positions, key=lambda x: x[0])[0]
    min_row = min(positions, key=lambda x: x[0])[0]
    max_col = max(positions, key=lambda x: x[1])[1]
    min_col = min(positions, key=lambda x: x[1])[1]
    return (max_row, min_row, max_col, min_col)

def find_grey_positions(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples representing the positions of grey elements in the grid.
    
    Args:
    - input_grid: a numpy ndarray representing the input grid
    
    Returns:
    - a list of tuples representing the positions of grey elements in the grid
    """
    grey_positions = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == grey:
                grey_positions.append((i, j))
    return grey_positions

def main(input_grid: np.ndarray) -> np.ndarray:
    grey_positions = find_grey_positions(input_grid)
    (max_row, min_row, max_col, min_col) = get_positions_bounds(grey_positions)
    output_block = find_block(input_grid, max_row + 1, min_row - 1, max_col, min_col)
    return output_block