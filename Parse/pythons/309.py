import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_bottom_right_index(input_grid: np.ndarray, color: int) -> Tuple[int, int]:
    for i in range(input_grid.shape[0] - 1, -1, -1):
        for j in range(input_grid.shape[1] - 1, -1, -1):
            if input_grid[i][j] == color:
                return (i, j)
    return (-1, -1)

def find_top_left_index(input_grid: np.ndarray, color: int) -> Tuple[int, int]:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == color:
                return (i, j)
    return (-1, -1)

def find_color_with_fewest_occurrences(input_grid: np.ndarray) -> int:
    (unique, counts) = np.unique(input_grid, return_counts=True)
    color_counts = dict(zip(unique, counts))
    return min(color_counts, key=color_counts.get)

def main(input_grid: np.ndarray) -> np.ndarray:
    edge_color = find_color_with_fewest_occurrences(input_grid)
    (xmin, ymin) = find_top_left_index(input_grid, edge_color)
    (xmax, ymax) = find_bottom_right_index(input_grid, edge_color)
    output_grid = input_grid[xmin:xmax + 1, ymin:ymax + 1]
    return output_grid