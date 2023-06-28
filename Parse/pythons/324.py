import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_teal_pixels_black(grid: np.ndarray, i: int, j: int) -> np.ndarray:
    """
    This function takes a grid and the indices of a teal pixel and makes all the teal pixels in the same shape black.
    
    Parameters:
    grid (np.ndarray): A numpy array representing the input grid
    i (int): The row index of the teal pixel
    j (int): The column index of the teal pixel
    
    Returns:
    np.ndarray: A numpy array representing the output grid with all the teal pixels in the same shape as the input pixel black
    """
    if i < 0 or j < 0 or i >= len(grid) or (j >= len(grid[0])) or (grid[i][j] != teal):
        return grid
    grid[i][j] = black
    grid = make_teal_pixels_black(grid, i - 1, j)
    grid = make_teal_pixels_black(grid, i + 1, j)
    grid = make_teal_pixels_black(grid, i, j - 1)
    grid = make_teal_pixels_black(grid, i, j + 1)
    return grid

def create_teal_line(grid: np.ndarray, number_of_shapes: int) -> np.ndarray:
    """                                                                                                                                                                   
    This function takes a grid and the number of shapes and creates a line from the top left corner to the base right corner with the same color as the shapes in the inpu
                                                                                                                                                                          
    Parameters:                                                                                                                                                           
    grid (np.ndarray): A numpy array representing the input grid                                                                                                          
    number_of_shapes (int): The number of shapes in the input grid                                                                                                        
                                                                                                                                                                          
    Returns:                                                                                                                                                              
    np.ndarray: A numpy array representing the output grid with a line from the top left corner to the base right corner with the same color as the shapes in the input gr
    """
    for i in range(number_of_shapes):
        grid[i][i] = teal
    return grid

def find_number_of_teal_shapes(input_grid: np.ndarray) -> int:
    """                                                                                                                                                                   
    This function takes an input grid and returns the number of teal shapes in it.                                                                                        
                                                                                                                                                                          
    Parameters:                                                                                                                                                           
    input_grid (np.ndarray): A numpy array representing the input grid                                                                                                    
                                                                                                                                                                          
    Returns:                                                                                                                                                              
    int: The number of teal shapes in the input grid                                                                                                                      
    """
    count = 0
    for i in range(len(input_grid)):
        for j in range(len(input_grid[i])):
            if input_grid[i][j] == teal:
                count += 1
                input_grid = make_teal_pixels_black(input_grid, i, j)
    return count

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                   
    In the input, you should see a grid contains several seperate grid, you should find the number of teal shapes and create a grid with the same number of shapes        
    The output grid size is the number of shapes the input grid has.                                                                                                      
    To make the output, you have to take the same color as the shapes in the input grid and create a line from the top left corner to the base right corner               
    """
    number_of_shapes = find_number_of_teal_shapes(input_grid)
    output_grid = np.zeros((number_of_shapes, number_of_shapes))
    output_grid = create_teal_line(output_grid, number_of_shapes)
    return output_grid