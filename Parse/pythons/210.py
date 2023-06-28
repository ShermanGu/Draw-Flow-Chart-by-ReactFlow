import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def concatenate_grids(grid1: List[List[int]], grid2: List[List[int]], grid3: List[List[int]]) -> np.ndarray:
    """
    This function concatenates the three input grids to a new numpy array along axis 0.

    Args:
    grid1: A list of lists containing integers representing the first input grid.
    grid2: A list of lists containing integers representing the second input grid.
    grid3: A list of lists containing integers representing the third input grid.

    Returns:
    A numpy array containing integers representing the concatenated grid.
    """
    return np.concatenate((grid1, grid2, grid3), axis=0)

def mirror_top_boundary(input_grid: List[List[int]]) -> List[List[int]]:
    """
    This function mirrors the input grid's symmetry with the top boundary.

    Args:
    input_grid: A list of lists containing integers representing the input grid.

    Returns:
    A list of lists containing integers representing the mirrored grid.
    """
    return input_grid[::-1]

def mirror_left_boundary(input):
    return np.concatenate((input[:, ::-1], input), axis=1)

def main(input_grid):
    t1 = mirror_left_boundary(input_grid)
    t2 = mirror_top_boundary(t1)
    t3 = concatenate_grids(t2, t1, t2)
    return t3