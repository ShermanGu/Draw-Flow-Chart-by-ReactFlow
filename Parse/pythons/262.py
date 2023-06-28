import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_grid_with_most_non_black_pixels(sub_grids: List[np.ndarray]) -> np.ndarray:
    max_non_black_pixels = -1
    max_non_black_pixels_grid = None
    for sub_grid in sub_grids:
        non_black_pixels = np.count_nonzero(sub_grid != black)
        if non_black_pixels > max_non_black_pixels:
            max_non_black_pixels = non_black_pixels
            max_non_black_pixels_grid = sub_grid
    return max_non_black_pixels_grid

def divide_into_sub_grids(input_grid: np.ndarray) -> List[np.ndarray]:
    sub_grids = []
    for i in range(0, input_grid.shape[0], 3):
        for j in range(0, input_grid.shape[1], 3):
            sub_grid = input_grid[i:i + 3, j:j + 3]
            sub_grids.append(sub_grid)
    return sub_grids

def main(input_grid: np.ndarray) -> np.ndarray:
    sub_grids = divide_into_sub_grids(input_grid)
    output_grid = find_grid_with_most_non_black_pixels(sub_grids)
    return output_grid