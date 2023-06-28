import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_blue_pixels_black(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid.copy()
    blue_pixels = np.where(output_grid == blue)
    output_grid[blue_pixels] = black
    return output_grid

def extract_pixels(upper_left: Tuple[int, int], lower_right: Tuple[int, int], input_grid: np.ndarray) -> np.ndarray:
    return input_grid[upper_left[0]:upper_left[0] + 2, upper_left[1]:upper_left[1] + 2]

def find_corners(input_grid: np.ndarray) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    non_blue_pixels = np.where(input_grid != blue)
    upper_left = (np.min(non_blue_pixels[0]), np.min(non_blue_pixels[1]))
    lower_right = (np.max(non_blue_pixels[0]), np.max(non_blue_pixels[1]))
    return (upper_left, lower_right)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid.copy()
    (upper_left, lower_right) = find_corners(input_grid)
    output_grid = extract_pixels(upper_left, lower_right, input_grid)
    output_grid = make_blue_pixels_black(output_grid)
    return output_grid