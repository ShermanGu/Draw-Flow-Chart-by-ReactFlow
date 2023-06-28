import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def symmetrical_right_edge_axis(grid: np.ndarray) -> np.ndarray:
    """
    Given a 3x3 grid, this function returns a 3x6 grid after being symmetrical along the right edge axis.

    Args:
    grid: A 3x3 numpy array.

    Returns:
    A 3x6 numpy array after being symmetrical along the right edge axis.
    """
    output_grid = np.concatenate((grid, np.fliplr(grid)), axis=1)
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = symmetrical_right_edge_axis(input_grid)
    return output_grid