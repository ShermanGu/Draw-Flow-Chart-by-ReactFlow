import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def concat_vertically(input_grid: np.ndarray, mirrored_grid: np.ndarray) -> np.ndarray:
    return np.concatenate((input_grid, mirrored_grid), axis=0)

def flip_up_down(input_grid: np.ndarray) -> np.ndarray:
    return np.flipud(input_grid)

def concat_horizontally(input_grid: np.ndarray, mirrored_grid: np.ndarray) -> np.ndarray:
    return np.concatenate((input_grid, mirrored_grid), axis=1)

def flip_left_right(input_grid: np.ndarray) -> np.ndarray:
    return np.fliplr(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    mirrored_grid = flip_left_right(input_grid)
    output_grid = concat_horizontally(input_grid, mirrored_grid)
    mirrored_output_grid = flip_up_down(output_grid)
    output_grid = concat_vertically(output_grid, mirrored_output_grid)
    return output_grid