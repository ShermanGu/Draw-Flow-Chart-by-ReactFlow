import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def flip_grid_left_right(input_grid: np.ndarray) -> np.ndarray:
    return np.fliplr(input_grid)

def find_min_columns(input_grid: np.ndarray, col: int) -> int:
    num_cols_left = col
    num_cols_right = input_grid.shape[1] - col - 1
    return min(num_cols_left, num_cols_right)

def elementwise_max(input_grid1: np.ndarray, input_grid2: np.ndarray) -> np.ndarray:
    return np.maximum(input_grid1, input_grid2)

def flip_grid_upside_down(input_grid: np.ndarray) -> np.ndarray:
    return np.flipud(input_grid)

def find_min_rows(input_grid: np.ndarray, row: int) -> int:
    num_rows_above = row
    num_rows_below = input_grid.shape[0] - row - 1
    return min(num_rows_above, num_rows_below)

def flip_columns_right(input_grid: np.ndarray, col: int) -> np.ndarray:
    num = find_min_columns(input_grid, col)
    sub_grid = input_grid[:, col - num:col + num + 1]
    sub_grid_flip = flip_grid_left_right(sub_grid)
    sub_grid_out = elementwise_max(sub_grid, sub_grid_flip)
    output_grid = np.copy(input_grid)
    output_grid[:, col - num:col + num + 1] = sub_grid_out
    return output_grid

def flip_rows_below(input_grid: np.ndarray, row: int) -> np.ndarray:
    num = find_min_rows(input_grid, row)
    sub_grid = input_grid[row - num:row + num + 1, :]
    sub_grid_flip = flip_grid_upside_down(sub_grid)
    sub_grid_out = elementwise_max(sub_grid, sub_grid_flip)
    output_grid = np.copy(input_grid)
    output_grid[row - num:row + num + 1, :] = sub_grid_out
    return output_grid

def find_top_left_color_index(input_grid: np.ndarray, color: int) -> Tuple[int, int]:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == color:
                return (i, j)
    return (-1, -1)

def find_least_common_color(input_grid: np.ndarray) -> int:
    (colors, counts) = np.unique(input_grid, return_counts=True)
    return colors[np.argmin(counts)]

def main(input_grid: np.ndarray) -> np.ndarray:
    color = find_least_common_color(input_grid)
    (x, y) = find_top_left_color_index(input_grid, color)
    (x, y) = (x + 1, y + 1)
    output_grid = np.copy(input_grid)
    output_grid = flip_rows_below(output_grid, x)
    output_grid = flip_columns_right(output_grid, y)
    return output_grid