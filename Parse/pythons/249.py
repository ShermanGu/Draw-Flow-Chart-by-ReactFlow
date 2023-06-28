import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def move_grey_pixel_to_nearest_red_pixel(input_grid: np.ndarray, grey_pixels: List[Tuple[int, int]], red_pixels: List[Tuple[int, int]]) -> np.ndarray:
    """                                                                                                                                                                   
    Given an input grid, a list of grey pixels and a list of red pixels, this function moves each grey pixel to its nearest red pixel until they touch each other.        
                                                                                                                                                                          
    Args:                                                                                                                                                                 
    - input_grid: a numpy ndarray representing the input grid                                                                                                             
    - grey_pixels: a list of tuples containing the indices of all grey pixels in the grid.                                                                                
    - red_pixels: a list of tuples containing the indices of all red pixels in the grid.                                                                                  
                                                                                                                                                                          
    Returns:                                                                                                                                                              
    - A numpy ndarray representing the output grid.                                                                                                                       
    """
    output_grid = input_grid.copy()
    for grey_pixel in grey_pixels:
        min_distance = float('inf')
        nearest_red_pixel = None
        for red_pixel in red_pixels:
            distance = np.sqrt((grey_pixel[0] - red_pixel[0]) ** 2 + (grey_pixel[1] - red_pixel[1]) ** 2)
            if distance < min_distance:
                min_distance = distance
                nearest_red_pixel = red_pixel
        output_grid[grey_pixel[0]][grey_pixel[1]] = black
        if nearest_red_pixel[0] == grey_pixel[0]:
            if grey_pixel[1] < nearest_red_pixel[1]:
                output_grid[nearest_red_pixel[0]][nearest_red_pixel[1] - 1] = grey
            else:
                output_grid[nearest_red_pixel[0]][nearest_red_pixel[1] + 1] = grey
        elif nearest_red_pixel[1] == grey_pixel[1]:
            if grey_pixel[0] < nearest_red_pixel[0]:
                output_grid[nearest_red_pixel[0] - 1][nearest_red_pixel[1]] = grey
            else:
                output_grid[nearest_red_pixel[0] + 1][nearest_red_pixel[1]] = grey
        elif grey_pixel[0] < nearest_red_pixel[0] and grey_pixel[1] < nearest_red_pixel[1]:
            output_grid[nearest_red_pixel[0] - 1][nearest_red_pixel[1] - 1] = grey
        elif grey_pixel[0] < nearest_red_pixel[0] and grey_pixel[1] > nearest_red_pixel[1]:
            output_grid[nearest_red_pixel[0] - 1][nearest_red_pixel[1] + 1] = grey
        elif grey_pixel[0] > nearest_red_pixel[0] and grey_pixel[1] < nearest_red_pixel[1]:
            output_grid[nearest_red_pixel[0] + 1][nearest_red_pixel[1] - 1] = grey
        elif grey_pixel[0] > nearest_red_pixel[0] and grey_pixel[1] > nearest_red_pixel[1]:
            output_grid[nearest_red_pixel[0] + 1][nearest_red_pixel[1] + 1] = grey
    return output_grid

def find_red_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples representing the indices of all red pixels in the grid.
    
    Parameters:
    input_grid (np.ndarray): A numpy array representing the input grid.
    
    Returns:
    List[Tuple[int, int]]: A list of tuples representing the indices of all red pixels in the grid.
    """
    red_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                red_pixels.append((i, j))
    return red_pixels

def find_grey_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples representing the indices of all grey pixels in the grid.
    
    Parameters:
    input_grid (np.ndarray): A numpy array representing the input grid.
    
    Returns:
    List[Tuple[int, int]]: A list of tuples representing the indices of all grey pixels in the grid.
    """
    grey_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == grey:
                grey_pixels.append((i, j))
    return grey_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                   
    in the input grid, you can see grey pixels and red pixels.                                                                                                            
    the output grid is the same size as the input grid.                                                                                                                   
    to make the output, you should move each grey pixel to its nearest red pixels until they touch each other.
    if the grey pixel and its nearest red pixel are on the same row or column, you should move vertically or horizontally
    if the grey pixel and its nearest red pixel are on the same diagonal, you should move diagonal                                            
    """
    output_grid = input_grid.copy()
    grey_pixels = find_grey_pixels(input_grid)
    red_pixels = find_red_pixels(input_grid)
    output_grid = move_grey_pixel_to_nearest_red_pixel(input_grid, grey_pixels, red_pixels)
    return output_grid