import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_red_black(input_grid: np.ndarray) -> np.ndarray:
    """
    This function takes in a numpy array as input_grid and colors all the red grids black.
    
    Args:
    input_grid: A numpy array of shape (n, m) representing the input grid.
    
    Returns:
    A numpy array of shape (n, m) representing the updated input grid with black colored red grids.
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                input_grid[i][j] = black
    return input_grid

def color_holes_green(locations: List[Tuple[Tuple[int, int], Tuple[int, int]]], input_grid: np.ndarray) -> np.ndarray:
    """
    This function takes in a list of tuples containing the location of red boxes in the input_grid and the input_grid itself.
    It then locates the holes in each red box and colors them green in the input_grid. The function returns the updated input_grid.
    
    Args:
    locations: A list of tuples, where each tuple contains the location of a red box in the input_grid.
    input_grid: A numpy array of shape (n, m) representing the input grid.
    
    Returns:
    A numpy array of shape (n, m) representing the updated input grid with green holes in each red box.
    """
    for location in locations:
        left_top = location[0]
        down_right = location[1]
        for i in range(left_top[0] + 1, down_right[0]):
            for j in range(left_top[1] + 1, down_right[1]):
                input_grid[i][j] = green
    return input_grid

def get_red_box_locations(input_grid: np.ndarray) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    This function takes in a numpy array as input_grid and returns a list of tuples, where each tuple contains the 
    location of a red box in the input_grid. The location of a box is its left-top corner and the down-right corner.
    
    Args:
    input_grid: A numpy array of shape (n, m) representing the input grid.
    
    Returns:
    A list of tuples, where each tuple contains the location of a red box in the input_grid.
    """
    red_boxes = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                left_top = (i, j)
                down_right = (i, j)
                while down_right[0] < input_grid.shape[0] and input_grid[down_right[0]][down_right[1]] == red:
                    down_right = (down_right[0] + 1, down_right[1])
                while down_right[1] < input_grid.shape[1] and input_grid[left_top[0]][down_right[1]] == red:
                    down_right = (down_right[0], down_right[1] + 1)
                red_boxes.append((left_top, (down_right[0] - 1, down_right[1] - 1)))
    return red_boxes

def main(input_grid: np.ndarray) -> np.ndarray:
    locations = get_red_box_locations(input_grid)
    output = color_holes_green(locations, input_grid)
    output = color_red_black(output)
    return output