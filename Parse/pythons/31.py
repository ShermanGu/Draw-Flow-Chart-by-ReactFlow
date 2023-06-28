import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_bottom_pixels_to_color(input_grid: np.ndarray, column_indices: List[int], colors: List[int], num_pixels: List[int]) -> np.ndarray:
    """
    For each column in column_indices, change the bottom num_pixels pixels to the corresponding color in colors.
    
    Args:
    input_grid: A numpy array representing the input grid.
    column_indices: A list of column indices.
    colors: A list of colors to be used for changing the pixels.
    num_pixels: A list of number of pixels to be changed for each column.
    
    Returns:
    A numpy array representing the updated grid.
    """
    output_grid = input_grid.copy()
    for (i, col) in enumerate(column_indices):
        output_grid[-num_pixels[i]:, col] = colors[i]
    return output_grid

def create_black_grid(input_grid: np.ndarray) -> np.ndarray:
    """
    This function takes an input grid as a numpy array and returns a black grid which has the same shape as the input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing a black grid which has the same shape as the input grid.
    """
    return np.zeros_like(input_grid)

def get_non_black_pixels_count(input_grid: np.ndarray, column_indices: List[int]) -> List[int]:
    """
    This function takes an input grid as a numpy array and a list of column indices and returns a list of the number of pixels which are not black in each of these columns.
    
    Args:
    input_grid: A numpy array representing the input grid.
    column_indices: A list of column indices.
    
    Returns:
    A list of the number of pixels which are not black in each of the columns in the input list.
    """
    non_black_pixels_count = []
    for i in column_indices:
        column = input_grid[:, i]
        non_black_pixels_count.append(np.count_nonzero(column != black))
    return non_black_pixels_count

def get_non_black_columns(input_grid: np.ndarray) -> Tuple[List[int], List[int]]:
    """
    This function takes an input grid as a numpy array and returns two lists:
    1. A list of column indices that have at least one non-black pixel.
    2. A list of colors of the non-black pixels in each of the columns in the first list.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A tuple of two lists. The first list contains the column indices and the second list contains the colors of the non-black pixels in each of the columns in the first list.
    """
    non_black_columns = []
    non_black_colors = []
    for i in range(input_grid.shape[1]):
        column = input_grid[:, i]
        if not np.all(column == black):
            non_black_columns.append(i)
            non_black_colors.append(column[column != black][0])
    return (non_black_columns, non_black_colors)

def main(input_grid: np.ndarray) -> np.ndarray:
    (y, color) = get_non_black_columns(input_grid)
    n = get_non_black_pixels_count(input_grid, y)
    output_grid = create_black_grid(input_grid)
    output_grid = change_bottom_pixels_to_color(output_grid, y, color, n)
    return output_grid