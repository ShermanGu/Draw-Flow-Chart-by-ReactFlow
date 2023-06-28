import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def up_down_symmetry(input_grid: np.ndarray) -> np.ndarray:
    return np.flipud(input_grid)

def left_right_symmetry(input_grid: np.ndarray) -> np.ndarray:
    return np.fliplr(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.zeros([input_grid.shape[0] * 2, input_grid.shape[1] * 2])
    output_grid[:input_grid.shape[0], :input_grid.shape[1]] = input_grid
    output_grid[:input_grid.shape[0], input_grid.shape[1]:] = left_right_symmetry(input_grid)
    output_grid[input_grid.shape[0]:, :] = up_down_symmetry(output_grid[:input_grid.shape[0], :])
    return output_grid