import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_symmetrical_pixel(input_grid: np.ndarray, color: int, center: Tuple[int, int]) -> np.ndarray:
    """                                                                                                                                                                 
    Given an input grid, a color, and a center point as a tuple of (row, col),                                                                                          
    this function returns a new grid with a symmetrical pixel of the given color                                                                                        
    added to the input grid at the center point.                                                                                                                        
    """
    output_grid = input_grid.copy()
    (center_row, center_col) = center
    (single_row, single_col, single_color) = color
    if single_col == center_col:
        dist = abs(single_row - center_row)
    elif single_row == center_row:
        dist = abs(single_col - center_col)
    output_grid[center_row + dist][center_col] = single_color
    output_grid[center_row - dist][center_col] = single_color
    output_grid[center_row][center_col + dist] = single_color
    output_grid[center_row][center_col - dist] = single_color
    return output_grid

def find_single_color(input_grid: np.ndarray) -> int:
    """                                                                                                                                                                 
    Given an input grid, this function returns the color that appears only once in the grid.                                                                            
    """
    (unique, counts) = np.unique(input_grid, return_counts=True)
    color_counts = dict(zip(unique, counts))
    single_color = None
    for (color, count) in color_counts.items():
        if count == 1:
            single_color = color
            break
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == single_color:
                return (i, j, single_color)
    return None

def get_shape_center(start_row: int, end_row: int, start_col: int, end_col: int) -> Tuple[int, int]:
    """
    Given the start row, end row, start col, and end col of a colored shape, 
    this function returns the center of the shape as a tuple of (row, col).
    """
    row_center = (start_row + end_row) // 2
    col_center = (start_col + end_col) // 2
    return (row_center, col_center)

def find_color_shape(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see some colored pixels form a colored shape.                                                                                              
    there is one color that only has one pixels.                                                                                                                        
    The output is the same size as the input.                                                                                                                           
    To make the output, you should find the start row, end row, start col, and end col of the colored shape.                                                            
    you should find the center of the shape, and make a symmetrical pixel of the single color according to the center.                                                  
    """
    for i in range(input_grid.shape[0]):
        if input_grid[i].sum() != 0:
            start_row = i
            break
    for i in range(input_grid.shape[0] - 1, -1, -1):
        if input_grid[i].sum() != 0:
            end_row = i
            break
    for i in range(input_grid.shape[1]):
        if input_grid[:, i].sum() != 0:
            start_col = i
            break
    for i in range(input_grid.shape[1] - 1, -1, -1):
        if input_grid[:, i].sum() != 0:
            end_col = i
            break
    return (start_row, end_row, start_col, end_col)

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see some colored pixels form a colored shape.
    there is one color that only has one pixels.
    The output is the same size as the input.
    To make the output, you should find the start row, end row, start col, and end col of the colored shape. 
    you should find the center of the shape, and make a symmetrical pixel of the single color according to the center.          
    """
    output_grid = input_grid.copy()
    (start_row, end_row, start_col, end_col) = find_color_shape(input_grid)
    center = get_shape_center(start_row, end_row, start_col, end_col)
    single_color = find_single_color(input_grid)
    output_grid = make_symmetrical_pixel(output_grid, single_color, center)
    return output_grid