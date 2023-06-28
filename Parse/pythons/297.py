import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def generate_new_grid(input_grid: np.ndarray, color_list: List[int]) -> np.ndarray:
    """
    Generate a new grid with the same size as the inputgrid. The four edges of the new grid are painted as the first item in the colorlist. 
    The second outer layer of the new grid is painted as the second item in the color_list; 
    the innermost layer (that is, the centermost 2* 2grid) painted as the third item in the colorlist,
    return the new grid
    
    Args:
    input_grid: A numpy array of size n*n representing the input grid
    color_list: A list of integers representing the colors
    
    Returns:
    A numpy array of size n*n representing the new grid
    """
    n = input_grid.shape[0]
    new_grid = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or (j == n - 1):
                new_grid[i][j] = color_list[0]
            elif i == 1 or i == n - 2 or j == 1 or (j == n - 2):
                new_grid[i][j] = color_list[1]
            elif i == n // 2 or i == n // 2 + 1 or j == n // 2 or (j == n // 2 + 1):
                new_grid[i][j] = color_list[2]
    return new_grid

def insert_last_to_first(color_list: List[int]) -> List[int]:
    """
    This function takes a list of integers and inserts the last item in the list before the first item.
    
    Args:
    color_list: A list of integers representing the colors
    
    Returns:
    A list of integers representing the colors with the last item inserted before the first item
    """
    color_list.insert(0, color_list.pop())
    return color_list

def get_color_list(input_grid: np.ndarray) -> List[int]:
    """
    Count the number of pixels of various colors in the entire inputgrid, and return the color list from more to less
    
    Args:
    input_grid: A numpy array of size n*n representing the input grid
    
    Returns:
    A list of integers representing the colors in descending order of their count in the input grid
    """
    color_dict = {}
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            color_dict[input_grid[i, j]] = color_dict.get(input_grid[i, j], 0) + 1
    color_list = sorted(color_dict, key=color_dict.get, reverse=True)
    return color_list

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    color_list = get_color_list(input_grid)
    color_list = insert_last_to_first(color_list)
    ans_grid = generate_new_grid(input_grid, color_list)
    return ans_grid