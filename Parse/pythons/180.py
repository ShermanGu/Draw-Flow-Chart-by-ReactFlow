import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def right_symmetric(blue_pixels: List[Tuple[int, int]], origin_area: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    for pixel in blue_pixels:
        (i, j) = pixel
        output_grid[i, 8 - j] = origin_area[i, j]
    return output_grid

def left_symmetric(blue_pixels: List[Tuple[int, int]], origin_area: np.ndarray, output_grid: np.ndarray) -> np.ndarray:
    for pixel in blue_pixels:
        (i, j) = pixel
        output_grid[i, 2 - j] = origin_area[i, j]
    return output_grid

def find_teal_pixels(origin_area: np.ndarray) -> List[Tuple[int, int]]:
    teal_pixels = []
    for i in range(3):
        for j in range(3):
            if origin_area[i, j] == teal:
                teal_pixels.append((i, j))
    return teal_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid.copy()
    origin_area = input_grid[0:3, 3:6]
    blue_pixels = find_teal_pixels(origin_area)
    if input_grid[3:6, 3:6][0, 0] == yellow:
        output_grid = left_symmetric(blue_pixels, origin_area, output_grid)
    elif input_grid[3:6, 3:6][0, 2] == yellow:
        output_grid = right_symmetric(blue_pixels, origin_area, output_grid)
    return output_grid