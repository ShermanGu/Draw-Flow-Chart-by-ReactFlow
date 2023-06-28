import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_rows_below_red(r: int, l: int, input_grid: np.ndarray) -> np.ndarray:
    """
    Colors the rows below the red horizontal line in blue, with the length of line in the row next to r and below r
    being 1 less than l, and the length in each row below being 1 less than the row above it. 
    Stops when the length equals to 0.

    Args:
    - r: an integer representing the index of the red horizontal line
    - l: an integer representing the length of the red horizontal line
    - input_grid: a 2D numpy array representing the input grid

    Returns:
    - a 2D numpy array representing the updated grid
    """
    length = l - 1
    for i in range(r + 1, input_grid.shape[0]):
        if length == 0:
            break
        input_grid[i, :length] = blue
        length -= 1
    return input_grid

def color_rows_above_red(r: int, l: int, input_grid: np.ndarray) -> np.ndarray:
    """
    Colors the rows above the red horizontal line in green, with the length of line in the row next to r and above r
    being 1 more than l, and the length in each row above being 1 more than the row below it.

    Args:
    - r: an integer representing the index of the red horizontal line
    - l: an integer representing the length of the red horizontal line
    - input_grid: a 2D numpy array representing the input grid

    Returns:
    - a 2D numpy array representing the updated grid
    """
    for i in range(r - 1, -1, -1):
        input_grid[i, :l + 1] = green
        l += 1
    return input_grid

def find_red_horizontal_line(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Finds the index and length of a red horizontal line in the input grid.

    Args:
    - input_grid: a 2D numpy array representing the input grid

    Returns:
    - a tuple of two integers representing the index and length of the red horizontal line
    """
    red_line = np.where(input_grid == red)[0]
    index = red_line[0]
    length = len(red_line)
    return (index, length)

def main(input_grid: np.ndarray) -> np.ndarray:
    (r, l) = find_red_horizontal_line(input_grid)
    above = color_rows_above_red(r, l, input_grid)
    out = color_rows_below_red(r, l, above)
    return out