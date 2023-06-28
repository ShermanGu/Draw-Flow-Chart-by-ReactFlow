import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def symmetric_red_pixels_y_axis(input_grid: np.ndarray, mean_y: float) -> np.ndarray:
    output_grid = input_grid.copy()
    red_pixels = np.where(output_grid == red)
    for i in range(len(red_pixels[0])):
        if red_pixels[0][i] < mean_y:
            output_grid[int(2 * mean_y) - red_pixels[0][i], red_pixels[1][i]] = red
    return output_grid

def symmetric_red_pixels(input_grid: np.ndarray, mean_x: float) -> np.ndarray:
    output_grid = input_grid.copy()
    red_pixels = np.where(output_grid == red)
    for i in range(len(red_pixels[0])):
        if red_pixels[1][i] < mean_x:
            output_grid[red_pixels[0][i], int(2 * mean_x) - red_pixels[1][i]] = red
    return output_grid

def calculate_mean_green_pixels(green_pixels: np.ndarray) -> Tuple[float, float]:
    mean_x = np.mean(green_pixels[0])
    mean_y = np.mean(green_pixels[1])
    return (mean_x, mean_y)

def find_red_and_green_pixels(input_grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    red_pixels = np.where(input_grid == red)
    green_pixels = np.where(input_grid == green)
    return (red_pixels, green_pixels)

def main(input_grid: np.ndarray) -> np.ndarray:
    (red_pixels, green_pixels) = find_red_and_green_pixels(input_grid)
    (mean_x, mean_y) = calculate_mean_green_pixels(green_pixels)
    output_grid = input_grid.copy()
    output_grid = symmetric_red_pixels(output_grid, mean_x)
    output_grid = symmetric_red_pixels_y_axis(output_grid, mean_y)
    return output_grid