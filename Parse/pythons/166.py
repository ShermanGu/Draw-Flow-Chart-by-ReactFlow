import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def generate_new_grid(cnt: int) -> np.ndarray:
    """
    This function takes in a count of unique colors present in the input grid.
    It generates a new 3*3 grid with black pixels and modifies it based on the count of unique colors.
    If cnt is one, it makes the top 3 squares gray.
    If cnt is two, it makes a diagonal line from top left to bottom right gray, again 3 pixels.
    If cnt is three, it makes a diagonal line from top right to bottom left gray, again 3 pixels.
    It returns the modified grid.
    """
    new_grid = np.zeros((3, 3))
    if cnt == 1:
        new_grid[:3, :] = grey
    elif cnt == 2:
        new_grid[0, 0] = grey
        new_grid[1, 1] = grey
        new_grid[2, 2] = grey
    elif cnt == 3:
        new_grid[0, 2] = grey
        new_grid[1, 1] = grey
        new_grid[2, 0] = grey
    return new_grid

def count_color_types(input_grid: np.ndarray) -> int:
    """
    This function takes in a numpy array representing a grid of pixels with different colors.
    It counts the number of unique colors present in the grid and returns the count.
    """
    return len(np.unique(input_grid))

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    cnt = count_color_types(input_grid)
    ans_grid = generate_new_grid(cnt)
    return ans_grid