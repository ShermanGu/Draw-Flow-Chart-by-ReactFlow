import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def count_colors_except_black(input_grid: np.ndarray) -> int:
    """
    This function takes in a 3x3 grid with any number of colors and counts the number of colors except black.
    
    Args:
    input_grid: A numpy array of shape (3,3) containing integers representing colors.
    
    Returns:
    An integer representing the count of colors except black in the input grid.
    """
    unique_colors = np.unique(input_grid)
    count = len(unique_colors) - 1 if 0 in unique_colors else len(unique_colors)
    return count

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see...a 3x3 with any number of colors                                                                                                      
    The output grid size...it get large enough to contain each color in more blocks                                                                                     
    To make the output, you have to...zoom out and give each block its on space                                                                                         
    """
    number = count_colors_except_black(input_grid)
    output_grid = np.zeros((input_grid.shape[0] * number, input_grid.shape[1] * number), dtype=int)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            output_grid[i * number:(i + 1) * number, j * number:(j + 1) * number] = input_grid[i][j]
    return output_grid