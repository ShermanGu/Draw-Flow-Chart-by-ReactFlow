import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def build_matrix(a: int, b: int, c: int) -> np.ndarray:
    return np.array([a, b, c]).reshape(3, 1)

def get_colors(input_grid: np.ndarray) -> Tuple[int, int, int]:
    """
    This function takes an input grid and returns the third most, fourth most, and fifth most colors in sequence.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple of three integers representing the third most, fourth most, and fifth most colors in sequence.
    """
    color_counts = np.bincount(input_grid.flatten())
    sorted_colors = np.argsort(-color_counts)
    return (sorted_colors[2], sorted_colors[3], sorted_colors[4])

def main(input_grid: np.ndarray) -> np.ndarray:
    (a, b, c) = get_colors(input_grid)
    out = build_matrix(a, b, c)
    return out