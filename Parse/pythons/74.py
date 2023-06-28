import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def copy_block_to_blue_points(input_grid: np.ndarray, blue_points: List[Tuple[int, int]]) -> np.ndarray:
    output_grid = np.copy(input_grid)
    block = input_grid[:3, :3]
    for point in blue_points:
        (i, j) = point
        output_grid[i - 1:i + 2, j - 1:j + 2] = block
    return output_grid

def find_blue_points(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    blue_points = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                blue_points.append((i, j))
    return blue_points

def main(input_grid: np.ndarray) -> np.ndarray:
    blue_points = find_blue_points(input_grid)
    output_grid = copy_block_to_blue_points(input_grid, blue_points)
    return output_grid