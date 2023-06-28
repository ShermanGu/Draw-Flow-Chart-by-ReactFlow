import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_point_to_teal(grid: np.ndarray, point: Tuple[int, int]) -> np.ndarray:
    (x, y) = point
    if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
        grid[point] = teal
    return grid

def find_min_max_green_coordinates(grid: np.ndarray) -> Tuple[int, int, int, int]:
    green_indices = np.where(grid == green)
    (xmin, xmax) = (np.min(green_indices[0]), np.max(green_indices[0]))
    (ymin, ymax) = (np.min(green_indices[1]), np.max(green_indices[1]))
    return (xmin, xmax, ymin, ymax)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.copy(input_grid)
    (xmin, xmax, ymin, ymax) = find_min_max_green_coordinates(output_grid)
    length = int((xmax - xmin + 1) / 2)
    for i in range(length):
        for j in range(length):
            if xmax + 1 + i <= input_grid.shape[0] and ymax + 1 + j <= input_grid.shape[1]:
                output_grid = turn_point_to_teal(output_grid, (xmax + 1 + i, ymax + 1 + j))
            if xmin - 1 - i >= 0 and ymin - 1 - j >= 0:
                output_grid = turn_point_to_teal(output_grid, (xmin - 1 - i, ymin - 1 - j))
    return output_grid