import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_pixels_between_red_and_green(red: Tuple[int, int], green: Tuple[int, int], f: Tuple[int, int], input_grid: np.ndarray) -> np.ndarray:
    input_grid[f] = teal
    if red[1] < f[1]:
        input_grid[red[0], red[1] + 1:f[1]] = teal
    else:
        input_grid[red[0], f[1] + 1:red[1]] = teal
    if green[0] < f[0]:
        input_grid[green[0] + 1:f[0], green[1]] = teal
    else:
        input_grid[f[0] + 1:green[0], green[1]] = teal
    return input_grid

def find_pixel_same_row_as_red_and_same_column_as_green(red: Tuple[int, int], green: Tuple[int, int]) -> Tuple[int, int]:
    return (red[0], green[1])

def find_red_green_pixels(input_grid: np.ndarray) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    red_pixels = np.where(input_grid == red)
    green_pixels = np.where(input_grid == green)
    return ((red_pixels[0][0], red_pixels[1][0]), (green_pixels[0][0], green_pixels[1][0]))

def main(input_grid: np.ndarray) -> np.ndarray:
    (r, g) = find_red_green_pixels(input_grid)
    f = find_pixel_same_row_as_red_and_same_column_as_green(r, g)
    out = color_pixels_between_red_and_green(r, g, f, input_grid)
    return out