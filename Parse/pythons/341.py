import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_non_black_teal_black(input_grid: np.ndarray, non_black_teal: List[Tuple[int, int]]) -> np.ndarray:
    for (i, j) in non_black_teal:
        if input_grid[i][j] != black and input_grid[i][j] != teal:
            input_grid[i][j] = black
    return input_grid

def make_nearest_teal_same_color(input_grid: np.ndarray, color_point: Tuple[int, int]) -> np.ndarray:
    (i, j) = color_point
    if input_grid[i][j] == teal:
        return input_grid
    min_dist = float('inf')
    nearest_teal = None
    for x in range(input_grid.shape[0]):
        for y in range(input_grid.shape[1]):
            if input_grid[x][y] == teal:
                dist = (x - i) ** 2 + (y - j) ** 2
                if dist < min_dist:
                    min_dist = dist
                    nearest_teal = (x, y)
    if nearest_teal is not None:
        input_grid[nearest_teal[0]][nearest_teal[1]] = input_grid[i][j]
    return input_grid

def find_non_black_teal(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    non_black_teal = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black and input_grid[i][j] != teal:
                non_black_teal.append((i, j))
    return non_black_teal

def main(input_grid: np.ndarray) -> np.ndarray:
    non_black_teal = find_non_black_teal(input_grid)
    for color_point in non_black_teal:
        input_grid = make_nearest_teal_same_color(input_grid, color_point)
    input_grid = make_non_black_teal_black(input_grid, non_black_teal)
    return input_grid