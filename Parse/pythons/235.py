import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_green(grid: np.ndarray) -> None:
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == red or grid[i][j] == blue:
                grid[i][j] = green

def color_dark(grid: np.ndarray) -> None:
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] != red and grid[i][j] != blue:
                grid[i][j] = black

def process_grid(input1: np.ndarray, input2: np.ndarray) -> np.ndarray:
    output_grid = np.zeros((4, 4), dtype=int)
    output_grid = input1 + input2
    color_dark(output_grid)
    color_green(output_grid)
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    up = input_grid[0:4, :]
    down = input_grid[5:9, :]
    output_grid = process_grid(up, down)
    return output_grid