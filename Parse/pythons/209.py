import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def assign_input_to_bottom_half(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    output_grid[3:, :] = input_grid
    return output_grid

def flip_input_grid(input_grid: np.ndarray) -> np.ndarray:
    return np.flipud(input_grid)

def assign_input_to_top_half(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    output_grid[:3, :] = input_grid
    return output_grid

def create_image_matrix() -> np.ndarray:
    return np.zeros((6, 3))

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = create_image_matrix()
    output_grid = assign_input_to_top_half(output_grid, input_grid)
    input_grid = flip_input_grid(input_grid)
    output_grid = assign_input_to_bottom_half(output_grid, input_grid)
    return output_grid