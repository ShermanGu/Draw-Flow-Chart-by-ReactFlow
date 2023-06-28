import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_black_to_teal(input_grid: np.ndarray) -> None:
    input_grid[input_grid == black] = teal

def copy_blue_pixel_left_up(input_grid: np.ndarray, i: int, j: int) -> Tuple[int, int]:
    while i > 0 and j > 0:
        if input_grid[i][j] == blue:
            input_grid[i - 1][j - 1] = blue
        j -= 1
        i -= 1
    return (i, j)

def copy_blue_pixel_right_up(input_grid: np.ndarray, i: int, j: int) -> Tuple[int, int]:
    while i > 0 and j < input_grid.shape[1] - 1:
        if input_grid[i][j] == blue:
            input_grid[i - 1][j + 1] = blue
        j += 1
        i -= 1
    return (i, j)

def is_blue_pixel_reached_top(input_grid: np.ndarray) -> bool:
    return blue in input_grid[0]

def main(input_grid: np.ndarray) -> np.ndarray:
    flag = is_blue_pixel_reached_top(input_grid)
    (i, j) = (input_grid.shape[0] - 1, 0)
    while not flag:
        (i, j) = copy_blue_pixel_right_up(input_grid, i, j)
        (i, j) = copy_blue_pixel_left_up(input_grid, i, j)
        flag = is_blue_pixel_reached_top(input_grid)
    change_black_to_teal(input_grid)
    return input_grid