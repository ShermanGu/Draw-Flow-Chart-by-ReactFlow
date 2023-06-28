import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_pattern_to_grey(input_grid: np.ndarray, pattern: np.ndarray) -> np.ndarray:
    color = pattern[pattern != black][0]
    for i in range(input_grid.shape[0] - 2):
        for j in range(input_grid.shape[1] - 2):
            if np.array_equal(pattern, input_grid[i:i + 3, j:j + 3]):
                input_grid[i:i + 3, j:j + 3][input_grid[i:i + 3, j:j + 3] == color] = grey
    return input_grid

def find_same_shape_pattern(input_grid: np.ndarray, pattern: np.ndarray) -> np.ndarray:
    for i in range(1, input_grid.shape[0] - 2):
        for j in range(1, input_grid.shape[1] - 2):
            if np.array_equal(pattern, np.where(input_grid[i:i + 3, j:j + 3] != black)):
                return input_grid[i:i + 3, j:j + 3]
    return None

def get_non_black_pattern(left_upper_square: np.ndarray) -> np.ndarray:
    return np.where(left_upper_square != black)

def main(input_grid: np.ndarray) -> np.ndarray:
    left_upper_square = input_grid[:3, :3]
    pattern = get_non_black_pattern(left_upper_square)
    another_pattern = find_same_shape_pattern(input_grid, pattern)
    output_grid = input_grid.copy()
    output_grid = change_pattern_to_grey(output_grid, another_pattern)
    return output_grid