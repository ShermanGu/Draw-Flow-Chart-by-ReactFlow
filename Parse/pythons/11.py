import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def set_pixel_colors(input_grid: np.ndarray, i: int, j: int, c1: int, c2: int) -> np.ndarray:
    input_grid[i - 1][j - 1] = c1
    input_grid[i - 2][j - 2] = c1
    input_grid[i - 1][j + 1] = c1
    input_grid[i - 2][j + 2] = c1
    input_grid[i + 1][j + 1] = c1
    input_grid[i + 2][j + 2] = c1
    input_grid[i + 1][j - 1] = c1
    input_grid[i + 2][j - 2] = c1
    input_grid[i - 2][j] = c2
    input_grid[i + 2][j] = c2
    input_grid[i][j - 2] = c2
    input_grid[i][j + 2] = c2
    return input_grid

def get_pixel_colors(input_grid: np.ndarray, i: int, j: int) -> Tuple[int, int]:
    c1 = input_grid[i][j]
    c2 = input_grid[i][j - 1]
    return (c1, c2)

def find_center_points(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    centers = []
    for i in range(1, input_grid.shape[0] - 1):
        for j in range(1, input_grid.shape[1] - 1):
            if input_grid[i][j] != black and input_grid[i - 1][j] != black and (input_grid[i + 1][j] != black) and (input_grid[i][j - 1] != black) and (input_grid[i][j + 1] != black):
                centers.append((i, j))
    return centers

def main(input_grid: np.ndarray) -> np.ndarray:
    centers = find_center_points(input_grid)
    for center in centers:
        (i, j) = center
        (c1, c2) = get_pixel_colors(input_grid, i, j)
        input_grid = set_pixel_colors(input_grid, i, j, c1, c2)
    return input_grid