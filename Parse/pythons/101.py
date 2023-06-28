import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_surrounded_squares_red(grid: np.ndarray, square: Tuple[int, int, int]) -> None:
    (i, j, size) = square
    if i > 0 and j > 0 and (i + size < grid.shape[0]) and (j + size < grid.shape[1]):
        if np.all(grid[i - 1:i + size + 1, j - 1] == 5) and np.all(grid[i - 1:i + size + 1, j + size] == 5) and np.all(grid[i - 1, j - 1:j + size + 1] == 5) and np.all(grid[i + size, j - 1:j + size + 1] == 5):
            grid[i:i + size, j:j + size] = red

def find_black_squares(grid: np.ndarray) -> List[Tuple[int, int, int]]:
    black_squares = []
    for size in range(1, min(grid.shape) + 1):
        for i in range(grid.shape[0] - size + 1):
            for j in range(grid.shape[1] - size + 1):
                if np.all(grid[i:i + size, j:j + size] == black):
                    black_squares.append((i, j, size))
    return black_squares

def main(input_grid: np.ndarray) -> np.ndarray:
    black_squares = find_black_squares(input_grid)
    for square in black_squares:
        color_surrounded_squares_red(input_grid, square)
    return input_grid