import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_pixels_to_orange(grid: np.ndarray, locs: List[Tuple[int, int]]) -> np.ndarray:
    for loc in locs:
        grid[loc] = orange
    return grid

def find_black_pixels_with_two_non_black_neighbours(grid: np.ndarray) -> List[Tuple[int, int]]:
    black_pixels = np.where(grid == black)
    locs = []
    for i in range(len(black_pixels[0])):
        (row, col) = (black_pixels[0][i], black_pixels[1][i])
        neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        non_black_neighbours = [n for n in neighbours if 0 <= n[0] < grid.shape[0] and 0 <= n[1] < grid.shape[1] and (grid[n] != black)]
        if len(non_black_neighbours) >= 2:
            locs.append((row, col))
    return locs

def has_more_than_63_black_pixels(grid: np.ndarray) -> bool:
    return np.count_nonzero(grid == black) > 63

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid
    while has_more_than_63_black_pixels(output_grid):
        locs = find_black_pixels_with_two_non_black_neighbours(output_grid)
        output_grid = change_pixels_to_orange(output_grid, locs)
    return output_grid