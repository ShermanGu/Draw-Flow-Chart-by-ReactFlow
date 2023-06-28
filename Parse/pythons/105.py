import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def put_input_grid_at_bottom_left(input_grid: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    output_grid[-input_grid.shape[0]:, :input_grid.shape[1]] = input_grid
    return output_grid

def put_input_grid_at_bottom_right(input_grid: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    output_grid[-input_grid.shape[0]:, -input_grid.shape[1]:] = input_grid
    return output_grid

def put_input_grid_at_top_right(input_grid: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    output_grid[:input_grid.shape[0], -input_grid.shape[1]:] = input_grid
    return output_grid

def rotate_90_degrees_clockwise(input_grid: np.ndarray) -> np.ndarray:
    return np.rot90(input_grid, k=-1)

def put_input_grid_at_top_left(input_grid: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    output_grid[:input_grid.shape[0], :input_grid.shape[1]] = input_grid
    return output_grid

def get_empty_grid(input_grid: np.ndarray) -> np.ndarray:
    return np.zeros((input_grid.shape[0] * 2, input_grid.shape[1] * 2))

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = get_empty_grid(input_grid)
    output_grid = put_input_grid_at_top_left(input_grid, output_grid)
    input_grid = rotate_90_degrees_clockwise(input_grid)
    output_grid = put_input_grid_at_top_right(input_grid, output_grid)
    input_grid = rotate_90_degrees_clockwise(input_grid)
    output_grid = put_input_grid_at_bottom_right(input_grid, output_grid)
    input_grid = rotate_90_degrees_clockwise(input_grid)
    output_grid = put_input_grid_at_bottom_left(input_grid, output_grid)
    return output_grid