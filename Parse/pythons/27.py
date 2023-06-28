import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def flip_and_concat(shape1: np.ndarray, shape2: np.ndarray) -> np.ndarray:
    flipped_shape2 = np.flipud(shape2)
    return np.concatenate((shape1, flipped_shape2), axis=0)

def draw_shape(color):
    out = np.zeros((5, 10), dtype=int)
    out[0, :] = color
    out[2, :] = color
    out[:, 0] = color
    out[:, -1] = color
    return out

def find_non_black_color(row: np.ndarray) -> int:
    """
    This function takes a numpy array as input and returns the non-black color in the array.
    """
    for color in row:
        if color != black:
            return color
    return black

def main(input_grid: np.ndarray) -> np.ndarray:
    color1 = find_non_black_color(input_grid[2])
    color2 = find_non_black_color(input_grid[7])
    shape1 = draw_shape(color1)
    shape2 = draw_shape(color2)
    out = flip_and_concat(shape1, shape2)
    return out