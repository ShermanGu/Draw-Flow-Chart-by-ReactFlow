import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_black_pixels_with_red(out: np.ndarray, m1: np.ndarray, m2: np.ndarray) -> np.ndarray:
    for i in range(3):
        for j in range(3):
            if m1[i][j] == black and m2[i][j] == black:
                out[i][j] = red
    return out

def build_black_matrix() -> np.ndarray:
    return np.full((3, 3), black)

def divide_into_2_matrices(input_grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    m1 = input_grid[:3, :]
    m2 = input_grid[3:, :]
    return (m1, m2)

def main(input_grid: np.ndarray) -> np.ndarray:
    (m1, m2) = divide_into_2_matrices(input_grid)
    out = build_black_matrix()
    out = replace_black_pixels_with_red(out, m1, m2)
    return out