import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_blue_pixels_on_top_and_bottom(row: int, col: int, grid: np.ndarray) -> bool:
    """                                                                                                                                                                 
    Given a row and column index, and a grid, this function returns a boolean value indicating                                                                          
    whether there is a blue pixel on the top and bottom of the given pixel.                                                                                             
    """
    up_red_pixel = False
    down_red_pixel = False
    for i in range(row - 1, -1, -1):
        if grid[i][col] == red:
            up_red_pixel = True
            break
    for i in range(row + 1, grid.shape[1]):
        if grid[i][col] == red:
            down_red_pixel = True
            break
    return (up_red_pixel, down_red_pixel)

def find_red_pixels_on_left_and_right(row: int, col: int, grid: np.ndarray) -> Tuple[bool, bool]:
    """
    Given a row and column index, and a grid, this function returns a tuple of two boolean values.
    The first boolean value indicates whether there is a red pixel on the left of the given pixel.
    The second boolean value indicates whether there is a red pixel on the right of the given pixel.
    """
    left_red_pixel = False
    right_red_pixel = False
    for i in range(col - 1, -1, -1):
        if grid[row][i] == red:
            left_red_pixel = True
            break
    for i in range(col + 1, grid.shape[1]):
        if grid[row][i] == red:
            right_red_pixel = True
            break
    return (left_red_pixel, right_red_pixel)

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see on the black grid, a structure composed by red pixels,                                                                                 
    color the black pixels that inside the red structure to blue.                                                                                                       
    """
    output_grid = input_grid.copy()
    for row in range(output_grid.shape[0]):
        for col in range(output_grid.shape[1]):
            if output_grid[row][col] == black:
                have_pixels_left_right = find_red_pixels_on_left_and_right(row, col, output_grid)
                have_pixels_up_down = find_blue_pixels_on_top_and_bottom(row, col, output_grid)
                if have_pixels_left_right[0] and have_pixels_left_right[1] and have_pixels_up_down[0] and have_pixels_up_down[1]:
                    output_grid[row][col] = blue
    return output_grid