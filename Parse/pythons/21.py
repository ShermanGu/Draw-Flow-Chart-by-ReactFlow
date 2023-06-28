
import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def add_grids_and_make_center_grey(grids: List[np.ndarray]) -> np.ndarray:
    """
    Adds all the grids and makes the center pixel gray.

    Args:
    grids: A list of numpy arrays, each representing a 3x3 grid.

    Returns:
    A numpy array representing the output grid.
    """
    output_grid = np.zeros_like(grids[0])
    for grid in grids:
        output_grid += grid
    output_grid[1, 1] = grey
    return output_grid

def get_centered_grids(input_grid: np.ndarray) -> List[np.ndarray]:
    """
    Returns a list of 3x3 grids centered on gray pixels in the input grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A list of numpy arrays, each representing a 3x3 grid centered on a gray pixel.
    """
    gray_pixels = np.where(input_grid == grey)
    centered_grids = []
    for i in range(len(gray_pixels[0])):
        (row, col) = (gray_pixels[0][i], gray_pixels[1][i])
        if row > 0 and row < input_grid.shape[0] - 1 and (col > 0) and (col < input_grid.shape[1] - 1):
            centered_grids.append(input_grid[row - 1:row + 2, col - 1:col + 2])
    return centered_grids

def main(input_grid: np.ndarray) -> np.ndarray:
    grids = get_centered_grids(input_grid)
    output_grid = add_grids_and_make_center_grey(grids)
    return output_grid