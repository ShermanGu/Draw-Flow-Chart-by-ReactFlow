import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def assign_input_to_right_half(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    output_grid[:, 3:] = input_grid
    return output_grid

def flip_left_to_right(input_grid: np.ndarray) -> np.ndarray:
    return np.fliplr(input_grid)

def assign_input_to_left_half(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    output_grid[:, :3] = input_grid
    return output_grid

def create_image_matrix() -> np.ndarray:
    return np.zeros((3, 6))

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = create_image_matrix()
    output_grid = assign_input_to_left_half(output_grid, input_grid)
    input_grid = flip_left_to_right(input_grid)
    output_grid = assign_input_to_right_half(output_grid, input_grid)
    return output_grid