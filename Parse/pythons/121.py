import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def move_red_pixels(input_grid: np.ndarray, output_grid: np.ndarray, green_directions: List[str]) -> np.ndarray:
    """                                                                                                                                                                   
    This function takes an input grid, an output grid, and a list of directions of the green pixels.                                                                      
    It moves the red pixels right for two pixels if the green pixels are in a row.                                                                                        
    It moves the red pixels down for two pixels if the green pixels are in a column.                                                                                      
    """
    if 'row' in green_directions:
        for i in range(input_grid.shape[0]):
            for j in range(input_grid.shape[1]):
                if red == input_grid[i, j]:
                    output_grid[i, j] = 0
    elif 'col' in green_directions:
        for j in range(input_grid.shape[1]):
            for i in range(input_grid.shape[0]):
                if red == input_grid[i, j]:
                    output_grid[i, j] = 0
    if 'row' in green_directions:
        for i in range(input_grid.shape[0]):
            for j in range(input_grid.shape[1]):
                if red == input_grid[i, j]:
                    output_grid[i, j + 2] = red
    elif 'col' in green_directions:
        for j in range(input_grid.shape[1]):
            for i in range(input_grid.shape[0]):
                if red == input_grid[i, j]:
                    output_grid[i + 2, j] = red
    return output_grid

def find_green_directions(input_grid: np.ndarray) -> List[str]:
    """                                                                                                                                                                   
    This function takes an input grid and returns a list of directions of the green pixels.                                                                               
    If the green pixels are in a row, the direction is 'row'.                                                                                                             
    If the green pixels are in a column, the direction is 'col'.                                                                                                          
    """
    green_directions = []
    for i in range(input_grid.shape[0]):
        if green in input_grid[i, :]:
            green_directions.append('row')
            return green_directions
    for j in range(input_grid.shape[1]):
        if green in input_grid[:, j]:
            green_directions.append('col')
            return green_directions

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                   
    In the input, you should see some green pixels and red pixels, the greens are either in a row or in a col.                                                            
    the output gird is the same size as the input grid.                                                                                                                   
    To make the output, copy the green pixels.                                                                                                                            
    if the green pixels are in a row, move the red pixels right for two pixels.                                                                                           
    if the green pixels are in a col, move the red pixels down for two pixels.                                                                                            
    """
    output_grid = input_grid.copy()
    green_directions = find_green_directions(input_grid)
    output_grid = move_red_pixels(input_grid, output_grid, green_directions)
    return output_grid