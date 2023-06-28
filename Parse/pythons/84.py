import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_middle_rows(input_grid: np.ndarray) -> List[int]:
    """                                                                                                                                                                 
    Given an input grid, find the middle row of each rectangle shape, in this row, its top and down line are not black.                                                 
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A numpy array representing the input grid.                                                                                                              
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A list of integers representing the row indices of the middle row of each rectangle shape.                                                                          
    """
    middle_rows = []
    for i in range(1, input_grid.shape[0] - 1):
        for j in range(1, input_grid.shape[1] - 1):
            if input_grid[i][j] != black and input_grid[i - 1][j] != black and (input_grid[i + 1][j] != black):
                middle_rows.append(i)
                break
    return middle_rows

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    find the middle row of each rectangle shape, in this row, it's top and down line are not black.
    in the row to modify, for the first pixel from left to right that is not black, make is unchange, color the second to black, then third unchange, forth color to black, etc.                                                   
    """
    output_grid = input_grid.copy()
    row_indices = find_middle_rows(output_grid)
    for row in row_indices:
        count = 0
        for i in range(output_grid.shape[1]):
            if output_grid[row][i] != black:
                count += 1
            if count % 2 == 0:
                output_grid[row][i] = black
    return output_grid