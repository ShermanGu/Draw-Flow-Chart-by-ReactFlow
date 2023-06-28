import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def deduplicate_and_arrange(target_line: np.ndarray) -> np.ndarray:
    """
    This function takes in a numpy array representing a target line of colored pixels and removes any repeated colors, 
    then arranges the colors in the order of their appearance in the original target line.

    Args:
    - target_line (np.ndarray): A numpy array representing a target line of colored pixels.

    Returns:
    - deduplicated (np.ndarray): The deduplicated and arranged target line.
    """
    deduplicated = []
    for color in target_line:
        if color not in deduplicated:
            deduplicated.append(color)
    deduplicated = np.array(deduplicated)
    return deduplicated

def get_target_line(input_grid: np.ndarray, cnt: int) -> np.ndarray:
    """
    This function takes in a numpy array representing a grid of colored pixels and the number of unique colors present in the grid.
    If the number of colors in the first row is equal to cnt, return the first row; otherwise, return the first column.

    Args:
    - input_grid (np.ndarray): A numpy array representing a grid of colored pixels.
    - cnt (int): The number of unique colors present in the grid.

    Returns:
    - target_line (np.ndarray): The target line of the input grid.
    """
    if len(input_grid) > 0:
        first_row = input_grid[0]
        if len(np.unique(first_row)) == cnt:
            target_line = first_row
        else:
            target_line = input_grid[:, 0]
    else:
        target_line = np.array([])
    return target_line

def count_color_types(input_grid: np.ndarray) -> int:
    """
    This function takes in a numpy array representing a grid of colored pixels and returns the number of unique colors present in the grid.

    Args:
    - input_grid (np.ndarray): A numpy array representing a grid of colored pixels.

    Returns:
    - cnt (int): The number of unique colors present in the grid.
    """
    cnt = len(np.unique(input_grid))
    return cnt

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    cnt = count_color_types(input_grid)
    target_line = get_target_line(input_grid, cnt)
    ans_grid = deduplicate_and_arrange(target_line)
    if len(ans_grid.shape) == 1:
        ans_grid = np.expand_dims(ans_grid, axis=0)
    return ans_grid