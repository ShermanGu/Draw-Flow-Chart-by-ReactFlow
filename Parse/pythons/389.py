import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_symmetric_pixel(input_grid: np.ndarray, x: int, y: int) -> Tuple[int, int]:
    """
    Given an input grid and a pixel (x,y), this function finds the red pixel (x2,y2) with the absolute distance closest to
    the pixel among all the red pixels. The symmetric pixel with respect to (x2,y2) is returned.
    """
    min_dist = float('inf')
    red_pixels = np.where(input_grid == red)
    for i in range(len(red_pixels[0])):
        dist = abs(x - red_pixels[0][i]) + abs(y - red_pixels[1][i])
        if dist < min_dist:
            min_dist = dist
            (x2, y2) = (red_pixels[0][i], red_pixels[1][i])
    x_symmetric = 2 * x2 - x
    y_symmetric = 2 * y2 - y
    return (x_symmetric, y_symmetric)

def find_gray_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, this function returns a list of all gray pixels in the grid.
    """
    gray_pixels = np.where(input_grid == grey)
    return list(zip(gray_pixels[0], gray_pixels[1]))

def symmetric_grid(input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid, this function returns a new grid where all gray pixels are replaced with their symmetric pixels
    with respect to the closest red pixel.
    """
    ans_grid = np.copy(input_grid)
    gray_pixels = find_gray_pixels(input_grid)
    for (x, y) in gray_pixels:
        (x_symmetric, y_symmetric) = find_symmetric_pixel(input_grid, x, y)
        ans_grid[x_symmetric, y_symmetric] = input_grid[x, y]
        ans_grid[x, y] = black
    return ans_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*m grid with multiple color pixels.
    """
    ans_grid = symmetric_grid(input_grid)
    return ans_grid