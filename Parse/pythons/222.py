import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def merge_sub_grids(sub_grids: List[np.ndarray]) -> np.ndarray:
    """
    Merges 9 3x3 numpy arrays to a 9x9 numpy array.

    Args:
    sub_grids: A list of 3x3 numpy arrays.

    Returns:
    A 9x9 numpy array.
    """
    output_grid = np.zeros((9, 9))
    for i in range(3):
        for j in range(3):
            output_grid[i * 3:i * 3 + 3, j * 3:j * 3 + 3] = sub_grids[i * 3 + j]
    return output_grid

def convert_to_sub_grids(lst: List[int]) -> List[np.ndarray]:
    """
    Converts each element in the list to a 3x3 numpy array, all of its elements equal to the corresponding element.

    Args:
    lst: A list of integers.

    Returns:
    A list of 3x3 numpy arrays.
    """
    sub_grids = []
    for num in lst:
        sub_grid = np.full((3, 3), num)
        sub_grids.append(sub_grid)
    return sub_grids

def convert_and_flatten(input_grid: np.ndarray) -> List[int]:
    """
    Converts the numpy array to a list and flattens it.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A flattened list representing the input grid.
    """
    return input_grid.flatten().tolist()

def main(input_grid: np.ndarray) -> np.ndarray:
    list = convert_and_flatten(input_grid)
    sub_grid_list = convert_to_sub_grids(list)
    output_grid = merge_sub_grids(sub_grid_list)
    return output_grid