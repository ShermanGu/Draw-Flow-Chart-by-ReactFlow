import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_black_pixels_with_red(input_grid: np.ndarray, m: np.ndarray) -> np.ndarray:
    """
    For each submatrix of input grid, which has the same shape as m, if the corresponding pixels of red pixels in m are all black, replace them as red
    
    Args:
    input_grid: A numpy ndarray representing the input grid
    m: A numpy ndarray representing the smallest matrix which includes all red pixels in the input grid
    
    Returns:
    A numpy ndarray representing the modified input grid with black pixels replaced by red pixels
    """
    submatrices = []
    for i in range(input_grid.shape[0] - m.shape[0] + 1):
        for j in range(input_grid.shape[1] - m.shape[1] + 1):
            submatrices.append(input_grid[i:i + m.shape[0], j:j + m.shape[1]])
    for submatrix in submatrices:
        red_pixels = np.where(m == red)
        if np.all(submatrix[red_pixels] == black):
            submatrix[red_pixels] = red
    return input_grid

def get_smallest_matrix_with_red_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function returns the smallest matrix which includes all red pixels in the input grid.
    
    Args:
    input_grid: A numpy ndarray representing the input grid
    
    Returns:
    A numpy ndarray representing the smallest matrix which includes all red pixels in the input grid
    """
    m = np.zeros_like(input_grid)
    m[input_grid == red] = 1
    rows = np.any(m, axis=1)
    cols = np.any(m, axis=0)
    (min_row, max_row) = np.where(rows)[0][[0, -1]]
    (min_col, max_col) = np.where(cols)[0][[0, -1]]
    out = input_grid[min_row:max_row + 1, min_col:max_col + 1]
    return out

def main(input_grid: np.ndarray) -> np.ndarray:
    m = get_smallest_matrix_with_red_pixels(input_grid)
    out = replace_black_pixels_with_red(input_grid, m)
    return out