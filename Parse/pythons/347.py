import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_num_orange_and_y_index(input_grid: np.ndarray) -> Tuple[int, int]:
    num_orange = np.count_nonzero(input_grid == orange)
    y_indices = np.where(input_grid == orange)[1]
    y_index = np.mean(y_indices).astype(int)
    return (num_orange, y_index)

def main(input_grid: np.ndarray) -> np.ndarray:
    (num_orange, y) = get_num_orange_and_y_index(input_grid)
    dist = 1
    output_grid = input_grid.copy()
    while dist < num_orange:
        if dist % 2 == 1:
            if y - dist >= 0:
                output_grid[:num_orange - dist, y - dist] = teal
            if y + dist < input_grid.shape[1]:
                output_grid[:num_orange - dist, y + dist] = teal
        else:
            if y - dist >= 0:
                output_grid[:num_orange - dist, y - dist] = orange
            if y + dist < input_grid.shape[1]:
                output_grid[:num_orange - dist, y + dist] = orange
        dist += 1
    return output_grid