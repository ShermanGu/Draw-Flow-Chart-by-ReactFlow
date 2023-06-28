import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_input_points_to_input_color(output_grid: np.ndarray, color: int, points: List[Tuple[int, int]]) -> np.ndarray:
    for point in points:
        output_grid[point[0]][point[1]] = color
    return output_grid

def find_color_of_non_black_square_on_lower_right(input_grid: np.ndarray) -> int:
    for i in range(input_grid.shape[0] - 1):
        for j in range(input_grid.shape[1] - 1):
            if input_grid[i][j] == black and input_grid[i + 1][j] != black and (input_grid[i][j + 1] != black):
                return input_grid[i + 1][j + 1]
    return -1

def find_non_black_square_on_lower_left(input_grid: np.ndarray) -> int:
    for i in range(input_grid.shape[0] - 1):
        for j in range(input_grid.shape[1] - 1):
            if input_grid[i][j] == black and input_grid[i + 1][j] != black and (input_grid[i][j - 1] != black):
                return input_grid[i][j - 1]
    return -1

def find_non_black_square_on_upper_right(input_grid: np.ndarray) -> int:
    for i in range(1, input_grid.shape[0]):
        for j in range(1, input_grid.shape[1]):
            if input_grid[i][j] == black and input_grid[i - 1][j] != black and (input_grid[i][j + 1] != black):
                return input_grid[i][j + 1]
    return -1

def find_color(input_grid: np.ndarray) -> int:
    for i in range(1, input_grid.shape[0]):
        for j in range(1, input_grid.shape[1]):
            if input_grid[i][j] == black and input_grid[i - 1][j] != black and (input_grid[i][j - 1] != black):
                return input_grid[i][j - 1]
    return -1

def main(input_grid: np.ndarray) -> np.ndarray:
    color1 = find_color(input_grid)
    color2 = find_non_black_square_on_upper_right(input_grid)
    color3 = find_non_black_square_on_lower_left(input_grid)
    color4 = find_color_of_non_black_square_on_lower_right(input_grid)
    output_grid = np.zeros((4, 4), dtype=int)
    output_grid = change_input_points_to_input_color(output_grid, color1, [(0, 0), (0, 1), (1, 0)])
    output_grid = change_input_points_to_input_color(output_grid, color2, [(0, 2), (0, 3), (1, 3)])
    output_grid = change_input_points_to_input_color(output_grid, color3, [(2, 0), (3, 0), (3, 1)])
    output_grid = change_input_points_to_input_color(output_grid, color4, [(2, 3), (3, 2), (3, 3)])
    return output_grid