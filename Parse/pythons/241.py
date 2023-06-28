import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_and_subgrid(input_grid: np.ndarray, tx: int, ty: int) -> np.ndarray:
    """
    Rotate the input grid 90 degrees clockwise, and return the subgrid with (tx,ty) as the upper left corner and shape as (3,3)
    """
    rotated_grid = np.rot90(input_grid)
    subgrid = rotated_grid[tx:tx + 3, ty:ty + 3]
    return subgrid

def find_first_black_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Traverse the input grid from top to bottom, from left to right, and return the coordinates of the first black pixel (tx, ty)
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == black:
                return (i, j)
    return (-1, -1)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    (tx, ty) = find_first_black_pixel(input_grid)
    ans_grid = rotate_and_subgrid(input_grid, tx, ty)
    return ans_grid