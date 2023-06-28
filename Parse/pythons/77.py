import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def move_red_squares_up_by_distance(grid: np.ndarray, column_distance: Tuple[int, int]) -> np.ndarray:
    (col, distance) = column_distance
    red_indices = np.where(grid[:, col] == red)[0]
    for index in red_indices:
        grid[index - distance, col] = red
        grid[index, col] = black
    return grid

def generate_column_distances(output_grid: np.ndarray) -> Dict[int, int]:
    column_distances = {}
    for col in range(output_grid.shape[1]):
        if red in output_grid[:, col]:
            red_index = np.where(output_grid[:, col] == red)[0][0]
            black_index = np.where(output_grid[:, col] == black)[0][0]
            distance = red_index - black_index
            column_distances[col] = distance
    return column_distances

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.copy(input_grid)
    dict = generate_column_distances(output_grid)
    for kv in dict.items():
        output_grid = move_red_squares_up_by_distance(output_grid, kv)
    return output_grid