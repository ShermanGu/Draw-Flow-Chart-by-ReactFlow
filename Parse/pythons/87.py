import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_non_black_pixels_to_color(grid: np.ndarray, color: int) -> np.ndarray:
    """
    Change all non-black pixels in grid to color
    """
    mask = grid != black
    grid[mask] = color
    return grid

def extract_subgrid(input_grid: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> np.ndarray:
    """
    Extract the subgrid with (x1+1, y1+1) as the upper left corner and (x2-1, y2-1) as the lower right corner, and return the grid
    """
    return input_grid[x1 + 1:x2, y1 + 1:y2]

def find_first_last_non_black_pixel(input_grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    From left to right, top to bottom, traverse the entire grid, find the first non-black pixel (x1, y1), 
    the last non-black pixel (x2, y2), return (x1, y1, x2, y2)
    """
    n = input_grid.shape[0]
    (x1, y1, x2, y2) = (n, n, -1, -1)
    for i in range(n):
        for j in range(n):
            print(i)
            print(j)
            if input_grid[i, j] != black:
                x1 = min(x1, i)
                y1 = min(y1, j)
                x2 = max(x2, i)
                y2 = max(y2, j)
    return (x1, y1, x2, y2)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    (x1, y1, x2, y2) = find_first_last_non_black_pixel(input_grid)
    ans_grid = extract_subgrid(input_grid, x1, y1, x2, y2)
    color = input_grid[x1, y1]
    ans_grid = change_non_black_pixels_to_color(ans_grid, color)
    return ans_grid