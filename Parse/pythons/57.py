import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_pixel_to_green(grid: np.ndarray, loc: Tuple[int, int]) -> np.ndarray:
    (row, col) = loc
    grid[row][col] = green
    return grid

def follow_direction_if_not_green(grid: np.ndarray, loc: Tuple[int, int], dir: Tuple[int, int]) -> Tuple[np.ndarray, Tuple[int, int], Tuple[int, int]]:
    while not is_next_pixel_valid(grid, loc, dir):
        (grid, loc) = change_pixel_to_green_and_get_next_loc(grid, loc, dir)
    return (grid, loc, dir)

def rotate_direction_clockwise(dir: Tuple[int, int]) -> Tuple[int, int]:
    return (dir[1], -dir[0])

def change_pixel_to_green_and_get_next_loc(grid: np.ndarray, loc: Tuple[int, int], dir: Tuple[int, int]) -> Tuple[np.ndarray, Tuple[int, int]]:
    (row, col) = loc
    grid[row][col] = green
    (next_row, next_col) = (row + dir[0], col + dir[1])
    return (grid, (next_row, next_col))

def is_next_pixel_valid(grid: np.ndarray, loc: Tuple[int, int], dir: Tuple[int, int]) -> bool:
    (row, col) = loc
    (next_row, next_col) = (row + dir[0], col + dir[1])
    if not (0 <= next_row < grid.shape[0] and 0 <= next_col < grid.shape[1]):
        return True
    if grid[next_row][next_col] == green:
        return True
    else:
        (next_row, next_col) = (next_row + dir[0], next_col + dir[1])
        if not (0 <= next_row < grid.shape[0] and 0 <= next_col < grid.shape[1]):
            return False
        if grid[next_row][next_col] == green:
            return True
    return False

def check_green_in_next_two_pixels(grid: np.ndarray, loc: Tuple[int, int], dir: Tuple[int, int]) -> bool:
    (row, col) = loc
    (next_row, next_col) = (row + dir[0], col + dir[1])
    if not (0 <= next_row < grid.shape[0] and 0 <= next_col < grid.shape[1]):
        return False
    if grid[next_row][next_col] == green:
        return True
    else:
        (next_row, next_col) = (next_row + dir[0], next_col + dir[1])
        if not (0 <= next_row < grid.shape[0] and 0 <= next_col < grid.shape[1]):
            return False
        if grid[next_row][next_col] == green:
            return True
    return False

def get_right_direction() -> Tuple[int, int]:
    return (0, 1)

def get_start_location() -> Tuple[int, int]:
    return (0, 0)

def main(input_grid: np.ndarray) -> np.ndarray:
    loc = get_start_location()
    dir = get_right_direction()
    out_grid = input_grid
    while True:
        if check_green_in_next_two_pixels(out_grid, loc, dir):
            break
        else:
            while not is_next_pixel_valid(out_grid, loc, dir):
                (out_grid, loc) = change_pixel_to_green_and_get_next_loc(out_grid, loc, dir)
            dir = rotate_direction_clockwise(dir)
    if follow_direction_if_not_green(out_grid, loc, dir):
        out_grid = change_pixel_to_green(out_grid, loc)
    return out_grid