import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def translate_pixels_down(input_grid: np.ndarray, pixels: List[Tuple[int, int]]) -> np.ndarray:
    """                                                                                                                                                                 
    Given an input grid and a list of pixels, translates each pixel down for 1 pixel.                                                                                   
                                                                                                                                                                        
    Args:                                                                                                                                                               
    - input_grid: a numpy ndarray representing the input grid                                                                                                           
    - pixels: a list of tuples containing the indices of all non-black pixels                                                                                           
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    - A numpy ndarray representing the output grid with translated pixels                                                                                               
    """
    output_grid = input_grid.copy()
    for pixel in pixels:
        (i, j) = pixel
        output_grid[i][j] = black
    for pixel in pixels:
        (i, j) = pixel
        output_grid[i + 1][j] = input_grid[i][j]
    return output_grid

def find_non_black_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples containing the indices of all non-black pixels.
    
    Args:
    - input_grid: a numpy ndarray representing the input grid
    
    Returns:
    - A list of tuples containing the indices of all non-black pixels.
    """
    non_black_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                non_black_pixels.append((i, j))
    return non_black_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    find the pixels which color is not black, translate each pixel down for 1 pixel.                                                    
    """
    output_grid = input_grid.copy()
    pixels = find_non_black_pixels(input_grid)
    output_grid = translate_pixels_down(output_grid, pixels)
    return output_grid