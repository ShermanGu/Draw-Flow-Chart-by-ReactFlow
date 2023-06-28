import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def copy_area_to_new_location(input_grid: np.ndarray, a: Tuple[int, int, int, int], n: List[Tuple[int, int]]) -> np.ndarray:
    out = np.copy(input_grid)
    for (i, j) in n:
        out[i][j] = input_grid[a[0] + i - n[0][0]][a[2] + j - n[0][1]]
    return out

def get_centered_3x3_area_index(x: int, y: int) -> List[Tuple[int, int]]:
    return [(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)]

def find_grey_pixel(input_grid: np.ndarray) -> Tuple[int, int]:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == grey:
                return (i, j)

def find_grey_centered_3x3_area(a: Tuple[int, int, int, int], input_grid: np.ndarray) -> np.ndarray:
    (x, y) = find_grey_pixel(input_grid)
    n = get_centered_3x3_area_index(x, y)
    out = copy_area_to_new_location(input_grid, a, n)
    return out

def find_covering_area(input_grid: np.ndarray, p: List[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    (min_i, min_j) = input_grid.shape
    max_i = max_j = 0
    for (i, j) in p:
        min_i = min(min_i, i)
        max_i = max(max_i, i)
        min_j = min(min_j, j)
        max_j = max(max_j, j)
    return (min_i, max_i + 1, min_j, max_j + 1)

def find_non_black_grey_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    non_black_grey_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] not in [black, grey]:
                non_black_grey_pixels.append((i, j))
    return non_black_grey_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    p = find_non_black_grey_pixels(input_grid)
    a = find_covering_area(input_grid, p)
    out = find_grey_centered_3x3_area(a, input_grid)
    return out