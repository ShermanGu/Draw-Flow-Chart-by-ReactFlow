import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_blue_pixels_green(up: int, down: int, left: int, right: int, input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid.copy()
    output_grid[up:down + 1, left:right + 1][output_grid[up:down + 1, left:right + 1] == blue] = green
    return output_grid

def find_teal_pixels(input_grid: np.ndarray) -> Tuple[int, int, int, int]:
    teal_pixels = np.where(input_grid == teal)
    (up, left) = np.min(teal_pixels, axis=1)
    (down, right) = np.max(teal_pixels, axis=1)
    return (up, down, left, right)

def main(input_grid: np.ndarray) -> np.ndarray:
    (up, down, left, right) = find_teal_pixels(input_grid)
    output_grid = make_blue_pixels_green(up, down, left, right, input_grid)
    return output_grid