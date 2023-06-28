import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_intersection_with_red(output_grid: np.ndarray, intersection: List[Tuple[int, int]]) -> None:
    for pixel in intersection:
        output_grid[pixel[0]][pixel[1]] = red

def find_intersection(black_pixels_top: List[Tuple[int, int]], black_pixels_bottom: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    intersection = []
    for pixel_top in black_pixels_top:
        if pixel_top in black_pixels_bottom:
            intersection.append(pixel_top)
    return intersection

def find_black_pixels(grid: np.ndarray) -> List[Tuple[int, int]]:
    black_pixels = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == black:
                black_pixels.append((i, j))
    return black_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    top_grid = input_grid[:4, :]
    bottom_grid = input_grid[4:, :]
    black_pixels_top = find_black_pixels(top_grid)
    black_pixels_bottom = find_black_pixels(bottom_grid)
    output_grid = np.zeros([4, 4])
    intersection = find_intersection(black_pixels_top, black_pixels_bottom)
    fill_intersection_with_red(output_grid, intersection)
    return output_grid