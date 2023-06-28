import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_output_block(input_grid: np.ndarray, longest_list: List[Tuple[int, int]]) -> np.ndarray:
    """
    Given a 2D numpy array and a list of tuples representing positions, returns a new 2D numpy array containing the
    block of elements defined by the maximum and minimum positions in the input list.
    
    Args:
    input_grid: A 2D numpy array of integers representing the color of each element.
    longest_list: A list of tuples representing positions of elements in the input array.
    
    Returns:
    A new 2D numpy array containing the block of elements defined by the maximum and minimum positions in the input list.
    """
    max_pos = max(longest_list)
    min_pos = min(longest_list)
    return input_grid[min_pos[0]:max_pos[0] + 1, min_pos[1]:max_pos[1] + 1]

def find_longest_list(input_lists: List[List]) -> List:
    """
    Given a list of lists, returns the longest list in the input list.
    
    Args:
    input_lists: A list of lists.
    
    Returns:
    The longest list in the input list.
    """
    return max(input_lists, key=len)

def find_color_positions(input_grid: np.ndarray) -> List[List[Tuple[int, int]]]:
    """
    Given a 2D numpy array, returns a list of lists where each inner list contains the positions of non-black elements
    of a specific color in the input array.
    
    Args:
    input_grid: A 2D numpy array of integers representing the color of each element.
    
    Returns:
    A list of lists where each inner list contains the positions of non-black elements of a specific color in the input array.
    """
    color_lists = [[] for _ in range(10)]
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                color_lists[input_grid[i][j]].append((i, j))
    return color_lists

def main(input_grid: np.ndarray) -> np.ndarray:
    ele_lists = find_color_positions(input_grid)
    longest_list = find_longest_list(ele_lists)
    output_grid = find_output_block(input_grid, longest_list)
    return output_grid