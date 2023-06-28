import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def mark_common_black(left: np.ndarray, right: np.ndarray, output: np.ndarray) -> None:
    """
    Marks every location of output to green if left and right in the same location both are black.

    Args:
    left (np.ndarray): The left half of the input grid.
    right (np.ndarray): The right half of the input grid.
    output (np.ndarray): The output grid.
    """
    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            if left[i][j] == black and right[i][j] == black:
                output[i][j] = green

def create_black_array() -> np.ndarray:
    return np.full((4, 3), black)

def split_grid(input_grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Splits the input grid into two 4x3 grids based on the blue color.

    Args:
    input_grid (np.ndarray): The input grid.

    Returns:
    Tuple[np.ndarray, np.ndarray]: The left and right 4x3 grids.
    """
    blue_indices = np.where(input_grid == blue)
    blue_columns = np.unique(blue_indices[1])
    blue_column_index = blue_columns[0]
    left = input_grid[:, :blue_column_index]
    right = input_grid[:, blue_column_index + 1:]
    return (left, right)

def main(input_grid: np.ndarray) -> np.ndarray:
    (left, right) = split_grid(input_grid)
    output = create_black_array()
    mark_common_black(left, right, output)
    return output