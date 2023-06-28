import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def cover_pattern(input_grid: np.ndarray, pattern_grid1: np.ndarray, pattern_grid2: np.ndarray) -> np.ndarray:
    input_grid[0:3, 4:7] = pattern_grid1
    input_grid[0:3, 8:11] = pattern_grid2
    return input_grid

def rotate_grid_90(input_grid: np.ndarray) -> np.ndarray:
    return np.rot90(input_grid, k=-1)

def extract_3x3_matrix(input_grid: np.ndarray) -> np.ndarray:
    return input_grid[:3, :3]

def main(input_grid: np.ndarray) -> np.ndarray:
    pattern_grid = extract_3x3_matrix(input_grid)
    pattern_grid1 = rotate_grid_90(pattern_grid)
    pattern_grid2 = rotate_grid_90(pattern_grid1)
    output_grid = cover_pattern(input_grid, pattern_grid1, pattern_grid2)
    return output_grid