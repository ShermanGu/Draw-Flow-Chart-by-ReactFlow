import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def create_output_grid(input_grid: np.ndarray) -> np.ndarray:
    input_grid4 = np.rot90(input_grid, k=3)
    output_grid = np.zeros_like(input_grid)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                output_grid[i][j] = input_grid[i][j]
            else:
                output_grid[i][j] = input_grid4[i][j]
    return output_grid

def assign_colors_to_pixels2(input_grid: np.ndarray, d: int) -> np.ndarray:
    for i in range(int(d / 2), d):
        c = input_grid[i][i - 2]
        for j in range(i - 4, -1, -2):
            if input_grid[i][j] != black:
                break
            input_grid[i][j] = c
    return input_grid

def assign_colors_to_pixels1(input_grid: np.ndarray, d: int) -> np.ndarray:
    for i in range(int(d / 2)):
        c = input_grid[i][i + 2]
        for j in range(i + 4, d, 2):
            if input_grid[i][j] != black:
                break
            input_grid[i][j] = c
    return input_grid

def rotate_and_stack(input_grid: np.ndarray) -> np.ndarray:
    input_grid1 = np.rot90(input_grid)
    input_grid2 = np.rot90(input_grid1)
    input_grid3 = np.rot90(input_grid2)
    output_grid = np.add(np.add(np.add(input_grid, input_grid1), input_grid2), input_grid3)
    return output_grid

def get_input_matrix_height(input_grid: np.ndarray) -> int:
    return input_grid.shape[0]

def main(input_grid: np.ndarray) -> np.ndarray:
    d = get_input_matrix_height(input_grid)
    input_grid = rotate_and_stack(input_grid)
    input_grid = assign_colors_to_pixels1(input_grid, d)
    input_grid = assign_colors_to_pixels2(input_grid, d)
    output_grid = create_output_grid(input_grid)
    return output_grid