import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_red(input_grid: np.ndarray, x1: int, y1: int, x2: int, y2: int) -> np.ndarray:
    input_grid[x1, y2] = red
    input_grid[x2, y1] = red
    return input_grid

def paint_orange(input_grid: np.ndarray) -> Tuple[np.ndarray, int, int]:
    (x2, y2) = (-1, -1)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == orange:
                if x2 == -1 and y2 == -1:
                    (x2, y2) = (i, j)
                    input_grid[i, :] = orange
                    input_grid[:, j] = orange
    return (input_grid, x2, y2)

def paint_teal(input_grid: np.ndarray) -> Tuple[np.ndarray, int, int]:
    (x1, y1) = (-1, -1)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == teal:
                if x1 == -1 and y1 == -1:
                    (x1, y1) = (i, j)
                    input_grid[i, :] = teal
                    input_grid[:, j] = teal
    return (input_grid, x1, y1)

def main(input_grid: np.ndarray) -> np.ndarray:
    (input_grid, x1, y1) = paint_teal(input_grid)
    (input_grid, x2, y2) = paint_orange(input_grid)
    input_grid = paint_red(input_grid, x1, y1, x2, y2)
    return input_grid