import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_black_pixels_to_green_in_columns(column_indices: List[int], output_grid: np.ndarray) -> np.ndarray:
    """
    This function takes in a list of column indices and a numpy array as input and changes the black pixels in the specified columns to green.
    
    Args:
    - column_indices: a list of column indices to change the black pixels to green
    - output_grid: a numpy array representing the output grid
    
    Returns:
    - A numpy array with the specified black pixels changed to green
    """
    for column_index in column_indices:
        output_grid[:, column_index][output_grid[:, column_index] == black] = green
    return output_grid

def change_black_pixels_to_green_in_rows(row_indices: List[int], output_grid: np.ndarray) -> np.ndarray:
    """
    This function takes in a list of row indices and a numpy array as input and changes the black pixels in the specified rows to green.
    
    Args:
    - row_indices: a list of row indices to change the black pixels to green
    - output_grid: a numpy array representing the output grid
    
    Returns:
    - A numpy array with the specified black pixels changed to green
    """
    for row_index in row_indices:
        output_grid[row_index][output_grid[row_index] == black] = green
    return output_grid

def find_columns_with_most_black_pixels(input_grid: np.ndarray) -> List[int]:
    """
    This function takes in a numpy array as input and returns a list of column indices that contain the most black pixels.
    If there are multiple columns with the same number of black pixels, all of them are returned.
    
    Args:
    - input_grid: a numpy array representing the input grid
    
    Returns:
    - A list of column indices that contain the most black pixels
    """
    column_sums = np.sum(input_grid == black, axis=0)
    max_sum = np.max(column_sums)
    return [i for (i, sum) in enumerate(column_sums) if sum == max_sum]

def find_rows_with_most_black_pixels(input_grid: np.ndarray) -> List[int]:
    """
    This function takes in a numpy array as input and returns a list of row indices that contain the most black pixels.
    If there are multiple rows with the same number of black pixels, all of them are returned.
    
    Args:
    - input_grid: a numpy array representing the input grid
    
    Returns:
    - A list of row indices that contain the most black pixels
    """
    row_sums = np.sum(input_grid == black, axis=1)
    max_sum = np.max(row_sums)
    return [i for (i, sum) in enumerate(row_sums) if sum == max_sum]

def main(input_grid: np.ndarray) -> np.ndarray:
    row_indices = find_rows_with_most_black_pixels(input_grid)
    column_indices = find_columns_with_most_black_pixels(input_grid)
    output_grid = input_grid.copy()
    output_grid = change_black_pixels_to_green_in_rows(row_indices, output_grid)
    output_grid = change_black_pixels_to_green_in_columns(column_indices, output_grid)
    return output_grid