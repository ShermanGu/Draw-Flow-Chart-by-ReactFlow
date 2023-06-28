import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def move_green_pixels_next_to_red_pixel(output_grid: np.ndarray, red_pixel: Tuple[int, int], green_pixels: List[Tuple[int, int]]) -> np.ndarray:
    """                                                                                                                                                                   
    Given an output grid, the coordinates of the red pixel and a list of coordinates of the green pixels,                                                                 
    moves the green pixels next to the red pixel in the output grid.                                                                                                      
                                                                                                                                                                          
    Args:                                                                                                                                                                 
    output_grid: A numpy array representing the output grid.                                                                                                              
    red_pixel: A tuple containing the x and y coordinates of the red pixel in the output grid.                                                                            
    green_pixels: A list of tuples containing the x and y coordinates of the green pixels in the output grid.                                                             
                                                                                                                                                                          
    Returns:                                                                                                                                                              
    A numpy array representing the output grid with the green pixels moved next to the red pixel.                                                                         
    """
    for i in range(len(green_pixels)):
        if red_pixel[0] == green_pixels[i][0] and red_pixel[1] < green_pixels[i][1]:
            output_grid[red_pixel[0]][red_pixel[1] + 1] = green
        elif red_pixel[0] == green_pixels[i][0] and red_pixel[1] > green_pixels[i][1]:
            output_grid[red_pixel[0]][red_pixel[1] - 1] = green
        elif red_pixel[1] == green_pixels[i][1] and red_pixel[0] > green_pixels[i][0]:
            output_grid[red_pixel[0] + 1][red_pixel[1]] = green
        elif red_pixel[1] == green_pixels[i][1] and red_pixel[0] < green_pixels[i][0]:
            output_grid[red_pixel[0] - 1][red_pixel[1]] = green
        output_grid[green_pixels[i][0]][green_pixels[i][1]] = black
    return output_grid

def move_orange_pixels_next_to_blue_pixel(output_grid: np.ndarray, blue_pixel: Tuple[int, int], orange_pixels: List[Tuple[int, int]]) -> np.ndarray:
    """                                                                                                                                                                   
    Given an output grid, the coordinates of the blue pixel and a list of coordinates of the orange pixels,                                                               
    moves the orange pixels next to the blue pixel in the output grid.                                                                                                    
                                                                                                                                                                          
    Args:                                                                                                                                                                 
    output_grid: A numpy array representing the output grid.                                                                                                              
    blue_pixel: A tuple containing the x and y coordinates of the blue pixel in the output grid.                                                                          
    orange_pixels: A list of tuples containing the x and y coordinates of the orange pixels in the output grid.                                                           
                                                                                                                                                                          
    Returns:                                                                                                                                                              
    A numpy array representing the output grid with the orange pixels moved next to the blue pixel.                                                                       
    """
    for i in range(len(orange_pixels)):
        if blue_pixel[0] == orange_pixels[i][0] and blue_pixel[1] < orange_pixels[i][1]:
            output_grid[blue_pixel[0]][blue_pixel[1] + 1] = orange
        elif blue_pixel[0] == orange_pixels[i][0] and blue_pixel[1] > orange_pixels[i][1]:
            output_grid[blue_pixel[0]][blue_pixel[1] - 1] = orange
        elif blue_pixel[1] == orange_pixels[i][1] and blue_pixel[0] > orange_pixels[i][0]:
            output_grid[blue_pixel[0] + 1][blue_pixel[1]] = orange
        elif blue_pixel[1] == orange_pixels[i][1] and blue_pixel[0] < orange_pixels[i][0]:
            output_grid[blue_pixel[0] - 1][blue_pixel[1]] = orange
        output_grid[orange_pixels[i][0]][orange_pixels[i][1]] = black
    return output_grid

def find_green_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of coordinates of the green pixels in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples containing the x and y coordinates of the green pixels in the grid.
    """
    green_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == green:
                green_pixels.append((i, j))
    return green_pixels

def find_orange_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of coordinates of the orange pixels in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples containing the x and y coordinates of the orange pixels in the grid.
    """
    orange_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == orange:
                orange_pixels.append((i, j))
    return orange_pixels

def find_red_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given an input grid, returns the coordinates of the red pixel in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A tuple containing the x and y coordinates of the red pixel in the grid.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                return (i, j)

def find_blue_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given an input grid, returns the coordinates of the blue pixel in the grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A tuple containing the x and y coordinates of the blue pixel in the grid.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                return (i, j)

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                   
    in the input grid, you can see a blue pixel, a red pixel, some orange pixels, some green pixels.
    the output is the same size of the input grid.
    to make the output, find the blue pixel, the red pixel, the green pixels, the orange pixels.
    move the oranges pixels next to the blue
    move the green pixels next to the orange.                                      
    """
    output_grid = input_grid.copy()
    blue_pixel = find_blue_pixel(input_grid)
    red_pixel = find_red_pixel(input_grid)
    orange_pixels = find_orange_pixels(input_grid)
    green_pixels = find_green_pixels(input_grid)
    output_grid = move_orange_pixels_next_to_blue_pixel(output_grid, blue_pixel, orange_pixels)
    output_grid = move_green_pixels_next_to_red_pixel(output_grid, red_pixel, green_pixels)
    return output_grid