import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def same_color_positions(grid1: np.ndarray, grid2: np.ndarray, color: int) -> bool:
    return np.array_equal(np.where(grid1 == color), np.where(grid2 == color))

def find_all_colors(grid: np.ndarray) -> List[int]:
    return [color for color in np.unique(grid) if color != black]

def find_different_color_neighbours(grid: np.ndarray, i: int, j: int) -> bool:
    neighbours = grid[i - 1:i + 2, j - 1:j + 2]
    (unique, counts) = np.unique(neighbours, return_counts=True)
    for (color, count) in zip(unique, counts):
        if color != black and color != grid[i][j] and (count >= 2):
            return True
    return False

def compare_grids(grid1, grid2):
    colors = find_all_colors(grid2)
    for color in colors:
        if same_color_positions(grid1, grid2, color):
            return True
    return False

def find_patterns(grid: np.ndarray) -> List[np.ndarray]:
    patterns = []
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            if grid[i][j] != black:
                if find_different_color_neighbours(grid, i, j):
                    patterns.append(grid[i - 1:i + 2, j - 1:j + 2])
    return patterns

def main(input_grid: np.ndarray) -> np.ndarray:
    patterns = find_patterns(input_grid)
    output_grid = input_grid.copy()
    for i in range(1, input_grid.shape[0] - 1):
        for j in range(1, input_grid.shape[1] - 1):
            for pattern in patterns:
                if compare_grids(output_grid[i - 1:i + 2, j - 1:j + 2], pattern):
                    output_grid[i - 1:i + 2, j - 1:j + 2] = pattern
                    break
    return output_grid