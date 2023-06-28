import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def arrange_pixels(color_list: List[int]) -> np.ndarray:
    """
    Given a list of colors, arrange them in a 3x3 grid in order and return the resulting grid.
    """
    ans_grid = np.zeros((3, 3), dtype=int)
    for i in range(9):
        ans_grid[i // 3][i % 3] = color_list[i]
    return ans_grid

def get_column_colors(grid: np.ndarray) -> List[int]:
    """
    Traverse each column, if there is a non-black pixel in this column, add the color of the pixel to the return list.
    After the traversal is complete, return the answer list.
    """
    color_list = []
    for col in range(grid.shape[1]):
        for row in range(grid.shape[0]):
            if grid[row][col] != black:
                color_list.append(grid[row][col])
                break
    return color_list

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    color_list = get_column_colors(input_grid)
    ans_grid = arrange_pixels(color_list)
    ans_grid[1, :] = ans_grid[1, ::-1]
    return ans_grid