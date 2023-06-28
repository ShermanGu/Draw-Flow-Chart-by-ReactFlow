import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def flip_pattern(input_grid: np.ndarray) -> np.ndarray:
    """
    Flips the input grid vertically
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the flipped grid
    """
    return np.flipud(input_grid)

def create_output_grid(input_grid: np.ndarray) -> np.ndarray:
    """
    Creates a new output grid with the same width as the input grid and four times the height minus three
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the output grid
    """
    output_grid = np.zeros((input_grid.shape[0] * 4 - 3, input_grid.shape[1]), dtype=int)
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see the whole grid as a pattern                                                                                                            
    The output grid size...is the same horizontally and multiplied by 4 vertically (and subtract 3)                                                                     
    To make the output, flip the pattern vertically 3 times to create a continuous pattern that is symmetrical both vertically and horizontally                         
    """
    output_grid = create_output_grid(input_grid)
    original_pattern = input_grid
    fliped_pattern = flip_pattern(input_grid)
    output_grid[:original_pattern.shape[0], :] = original_pattern
    output_grid[input_grid.shape[0] - 1:input_grid.shape[0] * 2 - 1, :] = fliped_pattern
    output_grid[input_grid.shape[0] * 2 - 2:input_grid.shape[0] * 3 - 2, :] = input_grid
    output_grid[input_grid.shape[0] * 3 - 3:input_grid.shape[0] * 4 - 3, :] = fliped_pattern
    return output_grid