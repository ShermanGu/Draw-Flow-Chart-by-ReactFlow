import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_black_blue(copy_grid: np.ndarray, grid: np.ndarray) -> np.ndarray:
    grey_pixels = np.where(copy_grid == grey)
    for i in range(len(grey_pixels[0])):
        (x, y) = (grey_pixels[0][i], grey_pixels[1][i])
        neighbors = [copy_grid[x, y - 1], copy_grid[x, y + 1], copy_grid[x - 1, y], copy_grid[x + 1, y]]
        if neighbors.count(black) >= 2:
            grid[x, y] = blue
    return grid

def paint_grey_red(copy_grid: np.ndarray, grid: np.ndarray) -> np.ndarray:
    grey_pixels = np.where(copy_grid == grey)
    for i in range(len(grey_pixels[0])):
        (x, y) = (grey_pixels[0][i], grey_pixels[1][i])
        if np.array_equal(copy_grid[x - 1:x + 2, y - 1:y + 2], np.array([[grey] * 3] * 3)):
            grid[x, y] = red
    return grid

def paint_grey_yellow(copy_grid: np.ndarray, grid: np.ndarray) -> np.ndarray:
    grey_pixels = np.where(copy_grid == grey)
    grid[grey_pixels] = yellow
    return grid

def pad_grid(input_grid: np.ndarray) -> np.ndarray:
    return np.pad(input_grid, pad_width=1, mode='constant', constant_values=black)

def main(input_grid: np.ndarray) -> np.ndarray:
    grid = pad_grid(input_grid)
    copy_grid = grid.copy()
    grid = paint_grey_yellow(copy_grid, grid)
    grid = paint_grey_red(copy_grid, grid)
    grid = paint_black_blue(copy_grid, grid)
    return grid[1:-1, 1:-1]