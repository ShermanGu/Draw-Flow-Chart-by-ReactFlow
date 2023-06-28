import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def generate_modified_grid(blue_grid_cnt: int) -> np.ndarray:
    """
    Generates a 1*5 grid, paints the left blue_grid_cnt pixel blue, and the other pixel black. Returns the modified new grid.
    """
    modified_grid = np.zeros((1, 5))
    modified_grid[0, :blue_grid_cnt] = blue
    modified_grid[0, blue_grid_cnt:] = black
    return modified_grid

def count_blue_subgrids(input_grid: np.ndarray) -> int:
    """
    Traverses the input_grid, looking for the sub-grid with the shape (2,2) and the color blue in the input_gird, and returns the total number found.
    """
    blue_subgrid_cnt = 0
    for i in range(input_grid.shape[0] - 1):
        for j in range(input_grid.shape[1] - 1):
            if input_grid[i][j] == blue and input_grid[i][j + 1] == blue and (input_grid[i + 1][j] == blue) and (input_grid[i + 1][j + 1] == blue):
                blue_subgrid_cnt += 1
    return blue_subgrid_cnt

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    blue_grid_cnt = count_blue_subgrids(input_grid)
    ans_grid = generate_modified_grid(blue_grid_cnt)
    return ans_grid