import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_non_black_to_pink(copy: np.ndarray) -> np.ndarray:
    copy[copy != black] = pink
    return copy

def copy_non_black_pixels(sub1: np.ndarray, sub2: np.ndarray, new: np.ndarray) -> np.ndarray:
    mask = sub2 != black
    new[mask] = sub2[mask]
    return new

def create_sub1_grid(input_grid: np.ndarray) -> np.ndarray:
    sub1 = input_grid[:, :3]
    return sub1

def split_grid(input_grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    sub1 = input_grid[:, :3]
    sub2 = input_grid[:, 3:]
    return (sub1, sub2)

def main(input_grid: np.ndarray) -> np.ndarray:
    (sub1, sub2) = split_grid(input_grid)
    new = create_sub1_grid(sub1)
    copy = copy_non_black_pixels(sub1, sub2, new)
    out = turn_non_black_to_pink(copy)
    return out