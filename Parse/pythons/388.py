import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_color_pixels_to_black(input_grid: np.ndarray, color_pixels: List[Tuple[int, int]]) -> np.ndarray:
    output_grid = input_grid.copy()
    for pixel in color_pixels:
        output_grid[pixel] = black
    return output_grid

def change_grey_to_color(input_grid: np.ndarray, color: int) -> np.ndarray:
    output_grid = input_grid.copy()
    output_grid[output_grid == grey] = color
    return output_grid

def find_special_color_pixels(special_color: int, input_grid: np.ndarray) -> List[Tuple[int, int]]:
    special_color_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == special_color:
                special_color_pixels.append((i, j))
    return special_color_pixels

def get_color(input_grid: np.ndarray) -> int:
    (colors, counts) = np.unique(input_grid, return_counts=True)
    color_counts = dict(zip(colors, counts))
    color_counts.pop(grey, None)
    return max(color_counts, key=color_counts.get)

def main(input_grid: np.ndarray) -> np.ndarray:
    special_color = get_color(input_grid)
    color_pixels = find_special_color_pixels(special_color, input_grid)
    output_grid = input_grid.copy()
    output_grid = change_grey_to_color(output_grid, special_color)
    output_grid = change_color_pixels_to_black(output_grid, color_pixels)
    return output_grid