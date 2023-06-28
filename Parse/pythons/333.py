import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_color_array(color: int) -> np.ndarray:
    if color == blue:
        return np.array([[0, 5, 0], [5, 5, 5], [0, 5, 0]])
    elif color == red:
        return np.array([[5, 5, 5], [0, 5, 0], [0, 5, 0]])
    elif color == green:
        return np.array([[0, 0, 5], [0, 0, 5], [5, 5, 5]])
    else:
        return np.zeros((3, 3), dtype=int)

def find_first_color(input_grid: np.ndarray) -> int:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                return input_grid[i][j]
    return black

def main(input_grid: np.ndarray) -> np.ndarray:
    c = find_first_color(input_grid)
    output_grid = get_color_array(c)
    return output_grid