import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_non_black_pixels(input_grid: np.ndarray, locations: List[Tuple[int, int]], color: int, pattern: List[Tuple[int, int]]) -> np.ndarray:
    for loc in locations[1:]:
        for i in range(loc[0], loc[0] + 5):
            for j in range(loc[1], loc[1] + 5):
                if (i - loc[0], j - loc[1]) in pattern and np.array_equal(input_grid[i][j], 0):
                    input_grid[i][j] = color
    return input_grid

def find_non_black_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    non_black_pixels = []
    for i in range(5):
        for j in range(5):
            if not np.array_equal(input_grid[i][j], 0):
                non_black_pixels.append((i, j))
    return non_black_pixels

def get_grid_locations() -> List[Tuple[int, int]]:
    locations = []
    for i in range(3):
        for j in range(3):
            x = 0 + j * 6
            y = 0 + i * 6
            locations.append((x, y))
    return locations

def get_color_at_x5(input_grid: np.ndarray) -> int:
    return input_grid[5][0]

def main(input_grid: np.ndarray) -> np.ndarray:
    color = get_color_at_x5(input_grid)
    locs = get_grid_locations()
    pattern = find_non_black_pixels(input_grid)
    output_grid = color_non_black_pixels(input_grid, locs, color, pattern)
    return output_grid