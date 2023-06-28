import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_and_mark(input_grid: np.ndarray, i: int, j: int, length: int) -> None:
    input_grid[i - length:i + length + 1, 0:j] = green
    input_grid[i, 0:j] = red

def color_and_mark_down(input_grid: np.ndarray, i: int, j: int, length: int) -> None:
    input_grid[i:i + length + 1, j - length:j + length + 1] = green
    input_grid[i, j - length:j + length + 1] = red

def num_green_points_up(input_grid: np.ndarray, i: int, j: int) -> int:
    count = 0
    while i >= 0 and input_grid[i][j] != black:
        if input_grid[i][j] == green:
            count += 1
        i -= 1
    return count

def color_and_mark_up(input_grid: np.ndarray, i: int, j: int, length: int) -> None:
    input_grid[0:i + 1, j - length:j + length + 1] = green
    input_grid[0:i + 1, j] = red

def num_green_points_down(input_grid: np.ndarray, i: int, j: int) -> int:
    count = 0
    while i < input_grid.shape[0] and input_grid[i][j] != black:
        if input_grid[i][j] == green:
            count += 1
        i += 1
    return count

def color_and_mark_right(input_grid: np.ndarray, i: int, j: int, length: int) -> None:
    input_grid[i - length:i + length + 1, j:input_grid.shape[1]] = green
    input_grid[i, j:input_grid.shape[1]] = red

def num_green_points_left(input_grid: np.ndarray, i: int, j: int) -> int:
    count = 0
    while j >= 0 and input_grid[i][j] != black:
        if input_grid[i][j] == green:
            count += 1
        j -= 1
    return count

def color_and_mark_areas(input_grid: np.ndarray, i: int, j: int, length: int) -> None:
    color_and_mark(input_grid, i, j, length)

def num_green_points_right(input_grid: np.ndarray, i: int, j: int) -> int:
    count = 0
    while j < input_grid.shape[1] and input_grid[i][j] != black:
        if input_grid[i][j] == green:
            count += 1
        j += 1
    return count

def find_red_points(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    red_points = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                red_points.append((i, j))
    return red_points

def main(input_grid: np.ndarray) -> np.ndarray:
    red_points = find_red_points(input_grid)
    for point in red_points:
        (i, j) = point
        if input_grid[i][j - 1] == black:
            len = num_green_points_right(input_grid, i, j)
            color_and_mark_areas(input_grid, i, j, len)
        elif input_grid[i][j + 1] == black:
            len = num_green_points_left(input_grid, i, j)
            color_and_mark_right(input_grid, i, j, len)
        elif input_grid[i - 1][j] == black:
            len = num_green_points_down(input_grid, i, j)
            color_and_mark_up(input_grid, i, j, len)
        elif input_grid[i + 1][j] == black:
            len = num_green_points_up(input_grid, i, j)
            color_and_mark_down(input_grid, i, j, len)
    return input_grid