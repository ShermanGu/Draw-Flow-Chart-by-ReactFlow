import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_pos_to_teal(grid: np.ndarray, pos: List[Tuple[int, int]]) -> np.ndarray:
    for (i, j) in pos:
        grid[i, j] = teal
    return grid

def get_black_pixels_indices(region1: np.ndarray, region2: np.ndarray) -> List[Tuple[int, int]]:
    black_pixels = []
    for i in range(region1.shape[0]):
        for j in range(region1.shape[1]):
            if region1[i, j] == black and region2[i, j] == black:
                black_pixels.append((i, j))
    return black_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    region1 = input_grid[:, :3]
    region2 = input_grid[:, -3:]
    output_grid = np.zeros((5, 3), dtype=int)
    black_pixels = get_black_pixels_indices(region1, region2)
    pos = black_pixels
    output_grid = change_pos_to_teal(output_grid, pos)
    return output_grid