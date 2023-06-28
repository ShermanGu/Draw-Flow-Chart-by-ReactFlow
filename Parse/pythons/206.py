import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_different_subgrid(sub_grid_list: List[np.ndarray], count_list: List[int]) -> np.ndarray:
    """
    Traverses count_list, if one of the values is different from the other three values, returns the sub-grid corresponding to the value.
    
    Args:
    sub_grid_list: A list of four numpy arrays representing the four sub-grids.
    count_list: A list of four integers representing the number of non-black blocks in each sub-grid.
    
    Returns:
    A numpy array representing the sub-grid with a different number of non-black blocks.
    """
    for i in range(4):
        if count_list.count(count_list[i]) == 1:
            return sub_grid_list[i]

def count_non_black_blocks(sub_grid_list: List[np.ndarray]) -> List[int]:
    """
    Counts the number of non-black blocks in each sub-grid and returns the answer list.
    
    Args:
    sub_grid_list: A list of four numpy arrays representing the four sub-grids.
    
    Returns:
    A list of four integers representing the number of non-black blocks in each sub-grid.
    """
    count_list = []
    for sub_grid in sub_grid_list:
        count = np.count_nonzero(sub_grid != black)
        count_list.append(count)
    return count_list

def divide_grid(input_grid: np.ndarray) -> List[np.ndarray]:
    """
    Divides the input grid into four 2*2 sub-grids using the third row and the third column as the dividing line.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of four numpy arrays representing the four sub-grids.
    """
    sub_grid_list = []
    sub_grid_list.append(input_grid[:2, :2])
    sub_grid_list.append(input_grid[:2, 3:])
    sub_grid_list.append(input_grid[3:, :2])
    sub_grid_list.append(input_grid[3:, 3:])
    return sub_grid_list

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    sub_grid_list = divide_grid(input_grid)
    count_list = count_non_black_blocks(sub_grid_list)
    ans_grid = get_different_subgrid(sub_grid_list, count_list)
    return ans_grid