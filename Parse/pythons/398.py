import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def generate_blue_grid(cnt: int) -> np.ndarray:
    """
    Generates a new grid with blue squares based on the count of red squares in the input grid.
    
    Args:
    cnt: An integer representing the count of 2x2 red squares in the input grid.
    
    Returns:
    A numpy array representing the new grid with blue squares.
    """
    grid = np.full((3, 3), black)
    if cnt == 1:
        grid[0][0] = blue
    elif cnt == 2:
        grid[0][0] = blue
        grid[0][2] = blue
    elif cnt == 3:
        grid[0][0] = blue
        grid[0][2] = blue
        grid[1][1] = blue
    elif cnt == 4:
        grid[0][0] = blue
        grid[0][2] = blue
        grid[1][1] = blue
        grid[2][0] = blue
    elif cnt == 5:
        grid[0][0] = blue
        grid[0][2] = blue
        grid[1][1] = blue
        grid[2][0] = blue
        grid[2][2] = blue
    return grid

def count_red_squares(input_grid: np.ndarray) -> int:
    """
    Counts how many 2x2 red squares there are in the input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    An integer representing the number of 2x2 red squares in the input grid.
    """
    cnt = 0
    for i in range(input_grid.shape[0] - 1):
        for j in range(input_grid.shape[1] - 1):
            if input_grid[i][j] == red and input_grid[i + 1][j] == red and (input_grid[i][j + 1] == red) and (input_grid[i + 1][j + 1] == red):
                cnt += 1
    return cnt

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    cnt = count_red_squares(input_grid)
    ans_grid = generate_blue_grid(cnt)
    return ans_grid