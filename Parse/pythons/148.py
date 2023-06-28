import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_pixel_blue(output_grid: np.ndarray, pink_numbers: List[int]) -> np.ndarray:
    """
    This function takes in an output grid and a list of pink numbers and colors the corresponding pixel of output grid with blue if the number equals 2.
    
    Args:
    - output_grid: a 3x3 numpy array representing the output grid
    - pink_numbers: a list of 9 integers representing the number of pink pixels in each 3x3 grid
    
    Returns:
    - output_grid: a 3x3 numpy array representing the output grid with blue pixels where the number of pink pixels equals 2
    """
    for i in range(3):
        for j in range(3):
            if pink_numbers[i * 3 + j] == 2:
                output_grid[i][j] = blue
    return output_grid

def count_pink_pixels(input_grid: np.ndarray) -> List[int]:
    pink_numbers = []
    for i in range(3):
        for j in range(3):
            sub_grid = input_grid[i * 3 + i:(i + 1) * 3 + i, j * 3 + j:(j + 1) * 3 + j]
            pink_numbers.append(np.count_nonzero(sub_grid == pink))
    return pink_numbers

def make_empty_grid() -> np.ndarray:
    return np.zeros((3, 3))

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see a 11x11 input gird, the 4th and 8th col are teal, the 4th and 8th row are teal.                                                        
    the teal rows and cols cuts the input grid into 9 3x3 grid.                                                                                                         
    each grid contains one pink pixel or two pink pixels.                                                                                                               
    The output grid is 3x3, each pixel corresponds a 3x3 grid.                                                                                                          
    To make the output, you have to count the number of pink pixels in each 3x3 grid, if the number equals 2, color the corresponding pixel of output grid with blue    
    """
    output_grid = make_empty_grid()
    pink_numbers = count_pink_pixels(input_grid)
    output_grid = color_pixel_blue(output_grid, pink_numbers)
    return output_grid