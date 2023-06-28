import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_same_color_as_toppest(input_grid: np.ndarray, i: int, j: int) -> np.ndarray:
    top_color = input_grid[0][j]
    input_grid[i][j] = top_color
    return input_grid

def is_even_rows(input_grid: np.ndarray, i: int) -> bool:
    return i % 2 == 0

def paint_adjacent_points(input_grid: np.ndarray, i: int, j: int) -> np.ndarray:
    top_color = input_grid[0][j]
    input_grid[i][j - 1] = top_color
    input_grid[i][j + 1] = top_color
    return input_grid

def is_odd_rows(input_grid: np.ndarray, i: int) -> bool:
    return i % 2 != 0

def is_not_black(input_grid: np.ndarray, i: int, j: int) -> bool:
    return input_grid[i][j] != black

def main(input_grid: np.ndarray) -> np.ndarray:
    for j in range(input_grid.shape[1]):
        if is_not_black(input_grid, 0, j):
            for i in range(1, input_grid.shape[0]):
                if is_odd_rows(input_grid, i):
                    input_grid = paint_adjacent_points(input_grid, i, j)
                if is_even_rows(input_grid, i):
                    input_grid = paint_same_color_as_toppest(input_grid, i, j)
    return input_grid