import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_pixels(input_grid: np.ndarray, row_index: int, col_index: int) -> np.ndarray:
    """
    This function takes an input grid, a row index, and a column index and paints the specified pixels with the given colors.
    
    Args:
    input_grid: A numpy array representing the input grid
    row_index: An integer representing the row index of the pixel to be painted yellow
    col_index: An integer representing the column index of the pixel to be painted yellow
    
    Returns:
    A numpy array representing the modified input grid with the specified pixels painted red, teal, and yellow.
    """
    input_grid[row_index, :] = red
    input_grid[:, col_index] = teal
    input_grid[row_index, col_index] = yellow
    return input_grid

def find_row_col_indices(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes an input grid and returns the row index and column index of the first occurrence of a row with two
    red pixels and a column with two teal pixels respectively.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A tuple containing the row index and column index of the first occurrence of a row with two red pixels and a column 
    with two teal pixels respectively.
    """
    row_index = -1
    col_index = -1
    for j in range(input_grid.shape[1]):
        if np.count_nonzero(input_grid[:, j] == teal) == 2:
            col_index = j
            break
    for i in range(input_grid.shape[0]):
        if np.count_nonzero(input_grid[i, :] == red) == 2:
            row_index = i
            break
    return (row_index, col_index)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    (rowIndex, colIndex) = find_row_col_indices(input_grid)
    ans_grid = paint_pixels(input_grid, rowIndex, colIndex)
    return ans_grid