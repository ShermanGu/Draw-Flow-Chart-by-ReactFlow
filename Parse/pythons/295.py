import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_non_black_pixels_indices(grid: np.ndarray) -> List[Tuple[int, int]]:
    non_black_pixels = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != black:
                non_black_pixels.append((i, j))
    return non_black_pixels

def get_corners(input_grid: np.ndarray) -> List[np.ndarray]:
    corners = []
    corners.append(input_grid[:2, :2])
    corners.append(input_grid[:2, -2:])
    corners.append(input_grid[-2:, :2])
    corners.append(input_grid[-2:, -2:])
    return corners

def main(input_grid: np.ndarray) -> np.ndarray:
    corners = get_corners(input_grid)
    output_grid = np.zeros([3, 3], dtype=np.int32)
    for i in range(len(corners)):
        non_black_pixels = get_non_black_pixels_indices(corners[i])
        color = corners[i][non_black_pixels[0][0], non_black_pixels[0][1]]
        for p in non_black_pixels:
            (x, y) = p
            output_grid[i // 2:2 + i // 2, i % 2:2 + i % 2][x, y] = color
    return output_grid