import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_green_pixels(m: np.ndarray, n: np.ndarray) -> np.ndarray:
    """
    Given two input grids m and n, this function divides n into 4 submatrices. For each submatrix, it replaces all green pixels with the color of the corresponding pixel in m.

    Args:
    m: A numpy array representing the 2x2 matrix.
    n: A numpy array representing the input grid.

    Returns:
    A numpy array representing the modified n grid.
    """
    submatrices = np.split(n, 2)
    for i in range(2):
        submatrices[i] = np.split(submatrices[i], 2, axis=1)
        for j in range(2):
            submatrices[i][j][submatrices[i][j] == green] = m[i][j]
        submatrices[i] = np.concatenate(submatrices[i], axis=1)
    return np.concatenate(submatrices)

def get_smallest_green_matrix(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function returns the smallest matrix containing all green pixels.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the smallest matrix containing all green pixels.
    """
    m = np.where(input_grid == green)
    return input_grid[m[0].min():m[0].max() + 1, m[1].min():m[1].max() + 1]

def get_smallest_matrix(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function returns the smallest matrix containing all pixels that are not black, green, or teal.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the smallest matrix containing all pixels that are not black, green, or teal.
    """
    m = np.where((input_grid != black) & (input_grid != green) & (input_grid != teal))
    return input_grid[m[0].min():m[0].max() + 1, m[1].min():m[1].max() + 1]

def main(input_grid: np.ndarray) -> np.ndarray:
    m = get_smallest_matrix(input_grid)
    n = get_smallest_green_matrix(input_grid)
    out = replace_green_pixels(m, n)
    return out