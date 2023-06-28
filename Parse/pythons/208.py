import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def copy_target_grid_to_first_non_black_non_yellow_pixel(ans_grid: np.ndarray, target_grid: np.ndarray) -> np.ndarray:
    """
    Given ans_grid and target_grid, this function finds the first non-black and non-yellow pixel (x, y) in ans_grid and copies target_grid to this position.
    """
    rows = ans_grid.shape[0]
    cols = ans_grid.shape[1]
    for i in range(rows):
        for j in range(cols):
            if ans_grid[i][j] != black and ans_grid[i][j] != yellow:
                ans_grid[i:i + target_grid.shape[0], j:j + target_grid.shape[1]] = target_grid
                return ans_grid
    return ans_grid

def expand_target_grid(target_grid: np.ndarray, side_length: float) -> np.ndarray:
    """
    Given a target grid and a side length, this function expands the target grid proportionally by the side length times and returns the expanded grid.
    """
    return np.repeat(np.repeat(target_grid, side_length, axis=0), side_length, axis=1)

def count_non_black_pixels(ans_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given an input grid, this function counts the number of unique non-black pixels and their total count and returns them as a tuple (kind, cnt).
    """
    kind = len(np.unique(ans_grid)) - 1
    cnt = np.count_nonzero(ans_grid != black)
    return (kind, cnt)

def update_min_max_coordinates(grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    Given an input grid, this function returns the smallest x, the smallest y, the largest x, and the largest y coordina
    """
    rows = grid.shape[0]
    cols = grid.shape[1]
    (minx, miny, maxx, maxy) = (rows, cols, -1, -1)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != black:
                minx = min(minx, i)
                miny = min(miny, j)
                maxx = max(maxx, i)
                maxy = max(maxy, j)
    return (minx, miny, maxx, maxy)

def find_yellow_pixels(input_grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    Given an input grid, this function finds the first and last yellow pixels and returns their coordinates as a tuple (
    """
    rows = input_grid.shape[0]
    cols = input_grid.shape[1]
    (x1, y1, x2, y2) = (rows, cols, -1, -1)
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == yellow:
                x1 = min(x1, i)
                y1 = min(y1, j)
                x2 = max(x2, i)
                y2 = max(y2, j)
    return (x1, y1, x2, y2)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    (x1, y1, x2, y2) = find_yellow_pixels(input_grid)
    ans_grid = input_grid[x1:x2 + 1, y1:y2 + 1].copy()
    input_grid[x1:x2 + 1, y1:y2 + 1] = black
    (minx, miny, maxx, maxy) = update_min_max_coordinates(input_grid)
    target_grid = input_grid[minx:maxx + 1, miny:maxy + 1]
    (kind, cnt) = count_non_black_pixels(ans_grid)
    import math
    side_length = math.sqrt(cnt / (kind - 1))
    target_grid = expand_target_grid(target_grid, side_length)
    ans = copy_target_grid_to_first_non_black_non_yellow_pixel(ans_grid, target_grid)
    return ans