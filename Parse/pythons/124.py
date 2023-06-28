import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def update_teal_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    This function updates the color of teal pixels in the input grid based on the given conditions.

    Args:
    input_grid: A numpy array representing the input grid with multiple color pixels.

    Returns:
    A numpy array representing the updated grid after applying the given conditions.
    """
    n = input_grid.shape[0]
    ans_grid = input_grid.copy()
    for i in range(n):
        for j in range(n):
            if ans_grid[i][j] == teal:
                count_green = 0
                count_pink = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if x < 0 or x >= n or y < 0 or (y >= n):
                            continue
                        if ans_grid[x][y] == green:
                            count_green += 1
                        elif ans_grid[x][y] == pink:
                            count_pink += 1
                if count_green >= 2 and count_pink >= 1:
                    ans_grid[i][j] = green
    return ans_grid

def update_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    This function updates the color of pixels in the input grid based on the given conditions.
    
    Args:
    input_grid: A numpy array representing the input grid with multiple color pixels.
    
    Returns:
    A numpy array representing the updated grid after applying the given conditions.
    """
    n = input_grid.shape[0]
    ans_grid = input_grid.copy()
    for i in range(n):
        for j in range(n):
            if ans_grid[i][j] == teal:
                count = 0
                if i > 0 and ans_grid[i - 1][j] == pink:
                    count += 1
                if i < n - 1 and ans_grid[i + 1][j] == pink:
                    count += 1
                if j > 0 and ans_grid[i][j - 1] == pink:
                    count += 1
                if j < n - 1 and ans_grid[i][j + 1] == pink:
                    count += 1
                if count >= 2:
                    ans_grid[i][j] = yellow
                elif count == 1:
                    ans_grid[i][j] = green
    return ans_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    ans_grid = update_pixels(input_grid)
    ans_grid = update_teal_pixels(ans_grid)
    return ans_grid