import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_pixels_in_bottom_right_direction(grid: np.ndarray, loc: Tuple[int, int], color: int) -> np.ndarray:
    (i, j) = loc
    colour = color
    while i < grid.shape[0] and j < grid.shape[1]:
        if grid[i][j] != black:
            grid[i][j] = colour
        colour = yellow if colour != yellow else color
        i += 1
        j += 1
    return grid

def get_pixel_color(grid: np.ndarray, loc: Tuple[int, int]) -> int:
    return grid[loc[0]][loc[1]]

def get_non_black_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    non_black_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black and (i == 0 or j == 0):
                non_black_pixels.append((i, j))
    return non_black_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid
    locs = get_non_black_pixels(input_grid)
    color = get_pixel_color(input_grid, locs[0])
    for loc in locs:
        output_grid = change_pixels_in_bottom_right_direction(output_grid, loc, color)
    return output_grid