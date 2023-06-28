import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_row(input_grid: np.ndarray, in_color: int, out_color: int, i: int) -> None:
    for j in range(0, input_grid.shape[1]):
        if input_grid[i][j] == in_color:
            input_grid[i][j] = out_color
        elif input_grid[i][j] == black:
            input_grid[i][j] = in_color

def color_column(input_grid: np.ndarray, in_color: int, out_color: int, j: int) -> None:
    for i in range(0, input_grid.shape[0]):
        if input_grid[i][j] == in_color:
            input_grid[i][j] = out_color
        elif input_grid[i][j] == black:
            input_grid[i][j] = in_color

def find_in_color_points(input_grid: np.ndarray, in_color: int, out_color: int) -> List[Tuple[int, int]]:
    in_color_points = []
    for i in range(1, input_grid.shape[0] - 1):
        for j in range(1, input_grid.shape[1] - 1):
            if input_grid[i][j] == in_color:
                neighbors = (input_grid[i - 1][j], input_grid[i + 1][j], input_grid[i][j - 1], input_grid[i][j + 1])
                if neighbors.count(out_color) == 3 and neighbors.count(in_color) == 1:
                    in_color_points.append((i, j))
    return in_color_points

def find_out_in_colors(input_grid: np.ndarray, color1: int, color2: int) -> Tuple[int, int]:
    if np.min(np.where(input_grid == color1)[1]) < np.min(np.where(input_grid == color2)[1]):
        return (color1, color2)
    else:
        return (color2, color1)

def main(input_grid: np.ndarray) -> np.ndarray:
    color1 = np.unique(input_grid)[1]
    color2 = np.unique(input_grid)[2]
    (out_color, in_color) = find_out_in_colors(input_grid, color1, color2)
    points = find_in_color_points(input_grid, in_color, out_color)
    for point in points:
        (i, j) = point
        if input_grid[i - 1][j] == in_color or input_grid[i + 1][j] == in_color:
            color_column(input_grid, in_color, out_color, j)
        if input_grid[i][j + 1] == in_color or input_grid[i][j - 1] == in_color:
            color_row(input_grid, in_color, out_color, i)
    return input_grid