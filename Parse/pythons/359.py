import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def put_right_part_over_black_pixels(flipped_right_part: np.ndarray, left_part: np.ndarray) -> np.ndarray:
    black_pixels = left_part == black
    left_part[black_pixels] = flipped_right_part[black_pixels]
    return left_part

def flip_horizontally(input_grid: np.ndarray) -> np.ndarray:
    return np.fliplr(input_grid)

def divide_with_grey_column(input_grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    grey_column = input_grid[:, input_grid.shape[1] // 2]
    left_part = input_grid[:, :input_grid.shape[1] // 2]
    right_part = input_grid[:, input_grid.shape[1] // 2 + 1:]
    return (left_part, right_part)

def main(input_grid: np.ndarray) -> np.ndarray:
    (left_part, right_part) = divide_with_grey_column(input_grid)
    flipped_right_part = flip_horizontally(right_part)
    left_part = put_right_part_over_black_pixels(flipped_right_part, left_part)
    return left_part