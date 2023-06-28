import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def check_surrounding_colors(input_grid: np.ndarray, i: int, j: int) -> int:
    current_color = input_grid[i][j]
    if current_color == black:
        return current_color
    else:
        surrounding_colors = []
        if i > 0:
            surrounding_colors.append(input_grid[i - 1][j])
        if i < input_grid.shape[0] - 1:
            surrounding_colors.append(input_grid[i + 1][j])
        if j > 0:
            surrounding_colors.append(input_grid[i][j - 1])
        if j < input_grid.shape[1] - 1:
            surrounding_colors.append(input_grid[i][j + 1])
        if all((color == current_color for color in surrounding_colors)):
            return black
        else:
            return current_color

def new_function(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.zeros_like(input_grid)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            output_grid[i][j] = check_surrounding_colors(input_grid, i, j)
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = new_function(input_grid)
    return output_grid