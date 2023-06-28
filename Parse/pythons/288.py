import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def modify_pixel_color(input_grid: np.ndarray, output_grid: np.ndarray, n: int) -> np.ndarray:
    for i in range(len(output_grid)):
        for j in range(len(output_grid[0])):
            output_grid[i][j] = input_grid[int(i / n)][int(j / n)]
    return output_grid

def create_black_image(n: int) -> np.ndarray:
    return np.zeros((3 * n, 3 * n))

def count_colors(input_grid: np.ndarray) -> int:
    n = len(np.unique(input_grid)) - 1
    return n

def main(input_grid: np.ndarray) -> np.ndarray:
    n = count_colors(input_grid)
    output_grid = create_black_image(n)
    output_grid = modify_pixel_color(input_grid, output_grid, n)
    return output_grid