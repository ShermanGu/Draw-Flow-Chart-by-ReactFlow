import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def move_green_to_yellow(output_grid: np.ndarray, pos_green: Tuple[int, int], pos_yellow: Tuple[int, int]) -> np.ndarray:
    """                                                                                                                                                                 
    This function takes an input grid, the position of the green pixel, and the position of the yellow pixel.                                                           
    It moves the green pixel one block closer to the yellow pixel, no matter if it is horizontal, diagonal, or vertical.                                                
    Move green to yellow, not yellow to green!                                                                                                                          
                                                                                                                                                                        
    Args:                                                                                                                                                               
    output_grid: A numpy array representing the input grid.                                                                                                              
    pos_green: A tuple (row, column) representing the position of the green pixel.                                                                                      
    pos_yellow: A tuple (row, column) representing the position of the yellow pixel.                                                                                    
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A numpy array representing the output grid with the green pixel moved one block closer to the yellow pixel.                                                         
    """
    row_diff = pos_green[0] - pos_yellow[0]
    col_diff = pos_green[1] - pos_yellow[1]
    if row_diff == 0:
        if col_diff > 0:
            output_grid[pos_green[0], pos_green[1] - 1] = green
        else:
            output_grid[pos_green[0], pos_green[1] + 1] = green
    elif col_diff == 0:
        if row_diff > 0:
            output_grid[pos_green[0] - 1, pos_green[1]] = green
        else:
            output_grid[pos_green[0] + 1, pos_green[1]] = green
    elif row_diff > 0:
        if col_diff > 0:
            output_grid[pos_green[0] - 1, pos_green[1] - 1] = green
        else:
            output_grid[pos_green[0] - 1, pos_green[1] + 1] = green
    elif col_diff > 0:
        output_grid[pos_green[0] + 1, pos_green[1] - 1] = green
    else:
        output_grid[pos_green[0] + 1, pos_green[1] + 1] = green
    output_grid[pos_green] = black
    return output_grid

def get_yellow_position(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes an input grid and returns the position of the yellow pixel in the form of a tuple (row, column).
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A tuple (row, column) representing the position of the yellow pixel.
    """
    return np.where(input_grid == yellow)

def get_green_position(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes an input grid and returns the position of the green pixel in the form of a tuple (row, column).
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A tuple (row, column) representing the position of the green pixel.
    """
    return np.where(input_grid == green)

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you can see a green pixel and a yellow pixel.
    The output is the same size as the input.
    To make the output, you have to...move the green square one block closer to the yellow square, no matter if it is horizontal, diagonal, or vertical.                                      
    """
    output_grid = input_grid.copy()
    pos_green = get_green_position(input_grid)
    pos_yellow = get_yellow_position(input_grid)
    output_grid = move_green_to_yellow(output_grid, pos_green, pos_yellow)
    return output_grid