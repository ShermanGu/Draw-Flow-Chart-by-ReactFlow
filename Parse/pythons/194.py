import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_black_subgrid_black(input_grid: np.ndarray, output_grid: np.ndarray, rows_of_pattern: List[int], cols_of_pattern: List[int]) -> np.ndarray:
    """                                                                                                                                                                 
    This function takes in a 9x9 numpy array representing the input grid, a 9x9 numpy array representing the output grid, a list of row indices that contain more than t
    It returns a 9x9 numpy array representing the output grid with the sub grid of the 9x9 pattern that is all black set to black.                                      
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A 9x9 numpy array representing the input grid.                                                                                                          
    output_grid: A 9x9 numpy array representing the output grid.                                                                                                        
    rows_of_pattern: A list of row indices that contain more than three grey pixels.                                                                                    
    cols_of_pattern: A list of column indices that contain more than three grey pixels.                                                                                 
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A 9x9 numpy array representing the output grid with the sub grid of the 9x9 pattern that is all black set to black.                                                 
    """
    rows_of_pattern_start = rows_of_pattern[0]
    cols_of_pattern_start = cols_of_pattern[0]
    for i in range(3):
        for j in range(3):
            sub_grid = input_grid[i * 3 + rows_of_pattern_start:i * 3 + 3 + rows_of_pattern_start, j * 3 + cols_of_pattern_start:j * 3 + 3 + cols_of_pattern_start]
            if np.all(sub_grid == black):
                output_grid[i * 3:i * 3 + 3, j * 3:j * 3 + 3] = black
    return output_grid

def replicate_small_grid(small_grid: np.ndarray) -> np.ndarray:
    """
    This function takes in a 3x3 numpy array representing the small grid and replicates it 3 times in row and 3 times in column.
    
    Args:
    small_grid: A 3x3 numpy array representing the small grid.
    
    Returns:
    A 9x9 numpy array representing the replicated small grid.
    """
    replicated_grid = np.zeros((9, 9))
    for i in range(3):
        for j in range(3):
            replicated_grid[i * 3:i * 3 + 3, j * 3:j * 3 + 3] = small_grid
    return replicated_grid

def make_small_grid(input_grid: np.ndarray, rows_of_pattern: List[int], cols_of_pattern: List[int]) -> np.ndarray:
    """
    This function takes in a 9x9 numpy array, a list of row indices that contain more than three grey pixels, and a list of column indices that contain more than three grey pixels.
    It returns a 3x3 numpy array representing the small grid according to the pattern.
    
    Args:
    input_grid: A 9x9 numpy array representing the input grid.
    rows_of_pattern: A list of row indices that contain more than three grey pixels.
    cols_of_pattern: A list of column indices that contain more than three grey pixels.
    
    Returns:
    A 3x3 numpy array representing the small grid according to the pattern.
    """
    small_grid = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            sub_grid = input_grid[rows_of_pattern[i * 3:i * 3 + 3], cols_of_pattern[j * 3:j * 3 + 3]]
            if np.all(sub_grid == black):
                small_grid[i][j] = black
            elif np.all(sub_grid == grey):
                small_grid[i][j] = grey
    return small_grid

def get_cols_with_grey_pixels(input_grid: np.ndarray) -> List[int]:
    """                                                                                                                                                                 
    This function takes in a 9x9 numpy array and returns a list of column indices that contain more than three grey pixels.                                             
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A 9x9 numpy array representing the input grid.                                                                                                          
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A list of column indices that contain more than three grey pixels.                                                                                                  
    """
    cols_with_grey_pixels = []
    for i in range(input_grid.shape[1]):
        if np.count_nonzero(input_grid[:, i] == grey) >= 3:
            cols_with_grey_pixels.append(i)
    return cols_with_grey_pixels

def get_rows_with_grey_pixels(input_grid: np.ndarray) -> List[int]:
    """                                                                                                                                                                 
    This function takes in a 9x9 numpy array and returns a list of row indices that contain more than three grey pixels.                                                
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A 9x9 numpy array representing the input grid.                                                                                                          
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A list of row indices that contain more than three grey pixels.                                                                                                     
    """
    rows_with_grey_pixels = []
    for i in range(input_grid.shape[0]):
        if np.count_nonzero(input_grid[i] == grey) >= 3:
            rows_with_grey_pixels.append(i)
    return rows_with_grey_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see a 9x9 pattern on the black background.                                                                                                 
    The output grid is 9x9.                                                                                                                                             
    To make the output, you should first get the pattern from the input grid, each row of the pattern contains at least three grey pixels, and each column of the patter
    then make a 3x3 grid according to the 9x9 pattern, to do this, divide the 9x9 pattern into nine 3x3 sub grid, if a 3x3 sub grid of the pattern are all black, make t
    if it is all grey, make the corresponding pixel of the make grid grey.grey                                                                                          
    Then replicate the make grid nine times on the output.                                                                                                              
    Finally, if the sub grid of the 9x9 pattern is all black, make the correspoinding position of the output grid all black.                                            
    """
    rows_of_pattern = get_rows_with_grey_pixels(input_grid)
    cols_of_pattern = get_cols_with_grey_pixels(input_grid)
    small_grid = np.zeros((3, 3))
    output_grid = np.zeros((9, 9))
    small_grid = make_small_grid(input_grid, rows_of_pattern, cols_of_pattern)
    output_grid = replicate_small_grid(small_grid)
    output_grid = make_black_subgrid_black(input_grid, output_grid, rows_of_pattern, cols_of_pattern)
    return output_grid