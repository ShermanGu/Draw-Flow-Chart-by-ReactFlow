import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_max_red_rectangle(input_grid: np.ndarray, teal_rectangles: List[Tuple[int, int, int, int]]) -> np.ndarray:
    """
    Given an input grid and a list of teal rectangles, this function finds the rectangle with the most red pixels.

    Args:
    - input_grid (np.ndarray): a 2D numpy array representing the input grid
    - teal_rectangles (List[Tuple[int, int, int, int]]): a list of tuples containing the starting row index, starting column index, height, and width of each teal rectangle

    Returns:
    - np.ndarray: a 2D numpy array representing the rectangle with the most red pixels
    """
    max_red_rectangle = np.zeros([1, 1])
    max_red_pixels = 0
    for (i, j, h, w) in teal_rectangles:
        red_pixels = np.sum(input_grid[i:i + h, j:j + w] == red)
        if red_pixels > max_red_pixels:
            max_red_pixels = red_pixels
            max_red_rectangle = input_grid[i:i + h, j:j + w]
    return max_red_rectangle

def find_teal_rectangle(input_grid: np.ndarray, i: int, j: int) -> Tuple[int, int]:
    """
    Given an input grid, starting indices i and j, this function finds the height and width of the teal rectangle
    starting at (i, j) and may contain blue and red pixels.

    Args:
    - input_grid (np.ndarray): a 2D numpy array representing the input grid
    - i (int): the starting row index
    - j (int): the starting column index

    Returns:
    - Tuple[int, int]: a tuple containing the height and width of the teal rectangle
    """
    (height, width) = (0, 0)
    if input_grid[i][j] == teal or input_grid[i][j] == red or input_grid[i][j] == blue:
        (height, width) = (1, 1)
        for k in range(i + 1, input_grid.shape[0]):
            if input_grid[k][j] == teal or input_grid[k][j] == blue or input_grid[k][j] == red:
                height += 1
            else:
                break
        for k in range(j + 1, input_grid.shape[1]):
            if input_grid[i][k] == teal or input_grid[i][k] == blue or input_grid[i][k] == red:
                width += 1
            else:
                break
    return (height, width)

def main(input_grid: np.ndarray) -> np.ndarray:
    teal_rectangles = []
    (rows, cols) = input_grid.shape
    flag = np.zeros([rows, cols])
    for i in range(rows):
        for j in range(cols):
            if (input_grid[i][j] == teal or input_grid[i][j] == red or input_grid[i][j] == blue) and (not flag[i, j]):
                (h, w) = find_teal_rectangle(input_grid, i, j)
                if h > 0 and w > 0:
                    teal_rectangles.append((i, j, h, w))
                    flag[i:i + h, j:j + w] = 1
    max_red_rectangle = find_max_red_rectangle(input_grid, teal_rectangles)
    return max_red_rectangle