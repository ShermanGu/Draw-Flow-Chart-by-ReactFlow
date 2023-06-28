import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_subgrid(large_grid: np.ndarray, temp_grid: np.ndarray, ii: int, jj: int) -> np.ndarray:
    large_grid[ii:ii + temp_grid.shape[0], jj:jj + temp_grid.shape[1]] = temp_grid
    return large_grid

def modify_non_black_pixels(temp_grid: np.ndarray, c: int) -> np.ndarray:
    temp_grid[temp_grid != black] = c
    return temp_grid

def find_color_at(large_grid: np.ndarray, ii: int, jj: int) -> int:
    return large_grid[ii][jj]

def merge_grids(large_grid: np.ndarray, h: int, small_grid: np.ndarray) -> np.ndarray:
    for i in range(h):
        for j in range(h):
            ii = i * h
            jj = j * h
            c = find_color_at(large_grid, ii, jj)
            temp_grid = small_grid.copy()
            temp_grid = modify_non_black_pixels(temp_grid, c)
            large_grid = replace_subgrid(large_grid, temp_grid, ii, jj)
    return large_grid

def enlarge_grid(grid1: np.ndarray, h: int) -> np.ndarray:
    return np.repeat(np.repeat(grid1, h, axis=0), h, axis=1)

def divide_image(input_grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    (h, w) = get_height_and_width(input_grid)
    if h < w:
        mid = w // 2
        left_half = input_grid[:, :mid]
        right_half = input_grid[:, mid:]
        return (left_half, right_half)
    else:
        mid = h // 2
        upper_half = input_grid[:mid, :]
        lower_half = input_grid[mid:, :]
        return (upper_half, lower_half)

def get_height_and_width(input_grid: np.ndarray) -> Tuple[int, int]:
    (h, w) = input_grid.shape
    return (h, w)

def main(input_grid: np.ndarray) -> np.ndarray:
    (h, w) = get_height_and_width(input_grid)
    (grid1, grid2) = divide_image(input_grid)
    if h < w:
        large_grid = enlarge_grid(grid1, h)
        output_grid = merge_grids(large_grid, h, grid2)
    else:
        large_grid = enlarge_grid(grid1, w)
        output_grid = merge_grids(large_grid, w, grid2)
    return output_grid