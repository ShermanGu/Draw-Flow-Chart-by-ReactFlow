import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def create_single_pattern_grid(input_grid: np.ndarray, end_col: int) -> np.ndarray:
    """                                                                                                                                                                 
    Given an input grid and the index of the last column of the repeating pattern,                                                                                      
    create a new grid with a single pattern.                                                                                                                            
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A numpy array representing the input grid.                                                                                                              
    end_col: An integer representing the index of the last column of the repeating pattern.                                                                             
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A numpy array representing the new grid with a single pattern.                                                                                                      
    """
    output_grid = input_grid[:, :end_col]
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see... A repeating pattern
    The output grid size... should be set to the equivalent grid size that the singular pattern takes up
    To make the output, you have to... fill the grid up with the singular identified pattern                                                                                      
    """
    end_col = -1
    for col in range(1, input_grid.shape[1]):
        count = 0
        for row in range(input_grid.shape[0]):
            count += 1
            if input_grid[row, col] != input_grid[row, 0]:
                break
            if count == input_grid.shape[0]:
                end_col = col
                break
        if end_col != -1:
            break
    output_grid = create_single_pattern_grid(input_grid, end_col)
    return output_grid