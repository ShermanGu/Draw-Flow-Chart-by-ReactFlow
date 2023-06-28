import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_3x3_pixels(input_grid: np.ndarray, loc: Tuple[int, int]) -> np.ndarray:
    return input_grid[loc[0] - 1:loc[0] + 2, loc[1] - 1:loc[1] + 2]

def find_most_blue_pixels(input_grid: np.ndarray, locs: List[Tuple[int, int]], blue_counts: List[int]) -> Tuple[int, int]:
    max_count = -1
    max_loc = None
    for (i, loc) in enumerate(locs):
        if blue_counts[i] > max_count:
            max_count = blue_counts[i]
            max_loc = loc
    return max_loc

def count_blue_pixels(input_grid: np.ndarray, locs: List[Tuple[int, int]]) -> List[int]:
    blue_counts = []
    for loc in locs:
        (i, j) = loc
        blue_counts.append(np.sum(input_grid[i - 1:i + 2, j - 1:j + 2] == blue))
    return blue_counts

def find_non_black_3x3_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    locs = []
    for i in range(input_grid.shape[0] - 2):
        for j in range(input_grid.shape[1] - 2):
            if np.all(input_grid[i:i + 3, j:j + 3] != black):
                locs.append((i + 1, j + 1))
    return locs

def main(input_grid: np.ndarray) -> np.ndarray:
    locs = find_non_black_3x3_pixels(input_grid)
    n = count_blue_pixels(input_grid, locs)
    loc = find_most_blue_pixels(input_grid, locs, n)
    out_grid = find_3x3_pixels(input_grid, loc)
    return out_grid