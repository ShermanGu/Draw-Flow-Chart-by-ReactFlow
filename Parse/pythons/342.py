import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def cover_columns_with_pattern(input_grid: np.ndarray, pattern_grid: np.ndarray) -> np.ndarray:
    for j in range(input_grid.shape[1]):
        input_grid[:, j] = pattern_grid[:, j % 4]
    return input_grid

def get_pattern_grid(input_grid: np.ndarray) -> np.ndarray:
    pattern_grid = input_grid[:input_grid.shape[0], :4]
    return pattern_grid

def get_input_dimensions(input_grid: np.ndarray) -> Tuple[int, int]:
    (h, w) = input_grid.shape[:2]
    return (h, w)

def main(input_grid: np.ndarray) -> np.ndarray:
    (h, w) = get_input_dimensions(input_grid)
    pattern_grid = get_pattern_grid(input_grid)
    input_grid = cover_columns_with_pattern(input_grid, pattern_grid)
    return input_grid