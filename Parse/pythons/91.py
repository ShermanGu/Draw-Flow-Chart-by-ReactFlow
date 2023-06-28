import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_between_equal_columns(input_grid: np.ndarray) -> np.ndarray:
    for col in input_grid.T:
        non_zero_indices = np.nonzero(col)[0]
        for i in range(len(non_zero_indices) - 1):
            for i in range(1, len(col[non_zero_indices])):
                if col[non_zero_indices[0]] == col[non_zero_indices[i]]:
                    col[non_zero_indices[0] + 1:non_zero_indices[i]] = col[non_zero_indices[0]]
    return input_grid

def fill_between_equal(input_grid: np.ndarray) -> np.ndarray:
    """
    Given a 2D numpy array, this function iterates through each row, and if the row has two equal non-zero elements,
    sets the values between them to all equal to this equal value.

    Args:
    input_grid: A 2D numpy array of integers.

    Returns:
    A 2D numpy array of integers with the values between equal non-zero elements in each row set to the same value.
    """
    for row in input_grid:
        non_zero_indices = np.nonzero(row)[0]
        for i in range(len(non_zero_indices) - 1):
            if row[non_zero_indices[i]] == row[non_zero_indices[i + 1]]:
                row[non_zero_indices[i] + 1:non_zero_indices[i + 1]] = row[non_zero_indices[i]]
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output = fill_between_equal(input_grid)
    output = fill_between_equal_columns(input_grid)
    return output