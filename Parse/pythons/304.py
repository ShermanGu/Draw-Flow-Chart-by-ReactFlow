import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_black_pixel_with_neighbour_color(grid: np.ndarray, locs: Tuple) -> np.ndarray:
    for i in range(len(locs[0])):
        (row, col) = (locs[0][i], locs[1][i])
        if row < grid.shape[0] - 1 and col > 0 and (grid[row + 1][col - 1] != black):
            grid[row][col] = grid[row + 1][col - 1]
        elif row > 0 and col < grid.shape[1] - 1 and (grid[row - 1][col + 1] != black):
            grid[row][col] = grid[row - 1][col + 1]
    return grid

def find_black_pixel_locations(grid: np.ndarray) -> Tuple:
    return np.where(grid == black)

def has_black_pixel(grid: np.ndarray) -> bool:
    return np.any(grid == black)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid
    while has_black_pixel(output_grid):
        locs = find_black_pixel_locations(output_grid)
        output_grid = replace_black_pixel_with_neighbour_color(output_grid, locs)
    return output_grid