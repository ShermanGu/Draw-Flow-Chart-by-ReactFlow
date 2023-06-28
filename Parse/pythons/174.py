import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_black_pixels(input_grid: np.ndarray, output_grid: np.ndarray, color_in_secondary_diagonal: int) -> np.ndarray:
    """                                                                                                                                                                   
    Given an input grid, this function colors the black pixels in the grid according to the following rules:                                                              
    - If a black pixel has a non-black pixel in its symmetrical position, color it to the color of the symmetrical pixel.                                                 
    - If a black pixel and its symmetrical pixel are both black, color it to the color of its most neighbor pixel.                                                        
    - For black pixels on the secondary diagonal, color it to the color of the first non-black pixel in the secondary diagonal.                                           
                                                                                                                                                                          
    Parameters:                                                                                                                                                           
    input_grid (np.ndarray): A numpy array representing the input grid.                                                                                                   
    output_grid (np.ndarray): A numpy array representing the output grid.                                                                                                 
    color_in_secondary_diagonal (int): The color of the first non-black pixel in the secondary diagonal.                                                                  
                                                                                                                                                                          
    Returns:                                                                                                                                                              
    np.ndarray: The output grid with black pixels colored according to the rules.                                                                                         
    """
    n = input_grid.shape[0]
    for i in range(n):
        for j in range(n):
            if input_grid[i, j] == black:
                if i == j:
                    output_grid[i, j] = color_in_secondary_diagonal
                else:
                    symmetrical_i = j
                    symmetrical_j = i
                    if input_grid[symmetrical_i, symmetrical_j] != black:
                        output_grid[i, j] = input_grid[symmetrical_i, symmetrical_j]
                    else:
                        neighbors = []
                        if i > 0:
                            neighbors.append(input_grid[i - 1, j])
                        if i < n - 1:
                            neighbors.append(input_grid[i + 1, j])
                        if j > 0:
                            neighbors.append(input_grid[i, j - 1])
                        if j < n - 1:
                            neighbors.append(input_grid[i, j + 1])
                        neighbors = [x for x in neighbors if x != black]
                        if neighbors:
                            output_grid[i, j] = max(set(neighbors), key=neighbors.count)
    return output_grid

def find_color_in_secondary_diagonal(input_grid: np.ndarray) -> int:
    """
    Given an input grid, this function finds the color of the first non-black pixel in the secondary diagonal.
    
    Parameters:
    input_grid (np.ndarray): A numpy array representing the input grid.
    
    Returns:
    int: The color of the first non-black pixel in the secondary diagonal.
    """
    n = input_grid.shape[0]
    for i in range(n):
        if input_grid[i, n - i - 1] != black:
            return input_grid[i, n - i - 1]
    return black

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                   
    in the input grid, you can see many pixels, the grid is Symmetrical along the secondary diagonal.                                                                     
    if the pixels are black, color to the color of the pixel in its Symmetrical pixel.                                                                                    
    if the pixel and its Symmetrical pixel are both black, color it to its most neighbor pixel.                                              
    for black pixels on the secondary diagonal, color it to the color of not black pixel on the secondary diagonal.
    """
    output_grid = input_grid.copy()
    color_in_secondary_diagonal = find_color_in_secondary_diagonal(input_grid)
    output_grid = color_black_pixels(input_grid, output_grid, color_in_secondary_diagonal)
    return output_grid