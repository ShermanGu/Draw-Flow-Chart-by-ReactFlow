import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def copy_non_grey_pixels(sub1: np.ndarray, sub2: np.ndarray, new: np.ndarray) -> np.ndarray:
    """
    Copies the non-grey pixels from sub2 to new at the same position.

    Args:
    sub1: A numpy array representing the first sub-grid.
    sub2: A numpy array representing the second sub-grid.
    new: A numpy array representing the new grid.

    Returns:
    A numpy array representing the updated new grid.
    """
    (height, width) = sub1.shape
    for i in range(height):
        for j in range(width):
            if sub2[i][j] != black and sub1[i][j] != grey:
                new[i][j] = sub2[i][j]
    return new

def create_new_grid(sub1: np.ndarray, sub2: np.ndarray) -> np.ndarray:
    """
    Creates a new grid in the shape of sub1 using sub1 and sub2.

    Args:
    sub1: A numpy array representing the first sub-grid.
    sub2: A numpy array representing the second sub-grid.

    Returns:
    A numpy array representing the new grid.
    """
    (height, width) = sub1.shape
    new = np.zeros((height, width), dtype=int)
    for i in range(height):
        for j in range(width):
            if sub1[i][j] == grey:
                new[i][j] = sub2[i][j]
            else:
                new[i][j] = sub1[i][j]
    return new

def split_along_grey_line(input_grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Finds the grey line in the input grid and splits it into two sub-grids.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple of two numpy arrays representing the two sub-grids.
    """
    (height, width) = input_grid.shape
    grey_line = None
    for i in range(height):
        if grey_line is not None:
            break
        for j in range(width):
            if input_grid[i][j] == grey:
                grey_line = i
                break
    sub1 = input_grid[:grey_line, :]
    sub2 = input_grid[grey_line + 1:, :]
    return (sub1, sub2)

def main(input_grid: np.ndarray) -> np.ndarray:
    (sub1, sub2) = split_along_grey_line(input_grid)
    new = create_new_grid(sub1, sub2)
    out = copy_non_grey_pixels(sub1, sub2, new)
    return out