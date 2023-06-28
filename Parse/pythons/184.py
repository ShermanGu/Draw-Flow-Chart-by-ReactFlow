import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def check_non_black_pixels_in_first_row_and_column(temp_grid: np.ndarray) -> bool:
    if np.any(temp_grid[0] != black) and np.any(temp_grid[:, 0] != black):
        return True
    return False

def assign_colors_to_temp_grid(input_grid: np.ndarray, temp_grid: np.ndarray, i: int, j: int, n: int) -> np.ndarray:
    temp_grid[0][0] = input_grid[i][j]
    temp_grid[0][1] = input_grid[i][j + n + 1]
    temp_grid[0][2] = input_grid[i][j + 2 * n + 2]
    temp_grid[1][0] = input_grid[i + n + 1][j]
    temp_grid[1][1] = input_grid[i + n + 1][j + n + 1]
    temp_grid[1][2] = input_grid[i + n + 1][j + 2 * n + 2]
    temp_grid[2][0] = input_grid[i + 2 * n + 2][j]
    temp_grid[2][1] = input_grid[i + 2 * n + 2][j + n + 1]
    temp_grid[2][2] = input_grid[i + 2 * n + 2][j + 2 * n + 2]
    return temp_grid

def assign_color_to_n_by_n_area(input_grid: np.ndarray, i: int, j: int, n: int, c_now: int) -> np.ndarray:
    input_grid[i + 1:i + n + 1, j + 1:j + n + 1] = c_now
    return input_grid

def check_adjacent_colors(input_grid: np.ndarray, i: int, j: int, n: int, c_now: int) -> bool:
    if i + n + 1 < input_grid.shape[0] and input_grid[i + n + 1][j] != c_now:
        return False
    if j + n + 1 < input_grid.shape[1] and input_grid[i][j + n + 1] != c_now:
        return False
    if i + n + 1 < input_grid.shape[0] and j + n + 1 < input_grid.shape[1] and (input_grid[i + n + 1][j + n + 1] != c_now):
        return False
    return True

def is_adjacent_pixels_same_color_except_current_pixel(input_grid: np.ndarray, i: int, j: int, c: int) -> bool:
    if i > 0 and input_grid[i - 1][j] != c:
        return False
    if i < input_grid.shape[0] - 1 and input_grid[i + 1][j] != c:
        return False
    if j > 0 and input_grid[i][j - 1] != c:
        return False
    if j < input_grid.shape[1] - 1 and input_grid[i][j + 1] != c:
        return False
    if input_grid[i][j] == c:
        return False
    return True

def get_color_and_spacing(input_grid: np.ndarray) -> Tuple[int, int]:
    c = 0
    n = 0
    for i in range(input_grid.shape[1]):
        if input_grid[0][i] != black:
            c = input_grid[0][i]
            n = i
            break
    return (c, n)

def main(input_grid: np.ndarray) -> np.ndarray:
    (c, n) = get_color_and_spacing(input_grid)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if is_adjacent_pixels_same_color_except_current_pixel(input_grid, i, j, c):
                c_now = input_grid[i, j]
                if check_adjacent_colors(input_grid, i, j, n, c_now):
                    input_grid = assign_color_to_n_by_n_area(input_grid, i, j, n, c_now)
    for i in range(0, input_grid.shape[0] - 2 * n - 1, n + 1):
        for j in range(0, input_grid.shape[1] - 2 * n - 1, n + 1):
            temp_grid = np.zeros((3, 3), dtype=np.int32)
            temp_grid = assign_colors_to_temp_grid(input_grid, temp_grid, i, j, n)
            if check_non_black_pixels_in_first_row_and_column(temp_grid):
                return temp_grid
    return np.zeros((3, 3), dtype=np.int32)