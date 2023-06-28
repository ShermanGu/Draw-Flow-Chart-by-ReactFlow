import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_area(pixel: int, area: Tuple[slice, slice], new: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    if pixel == orange:
        new[area] = np.copy(input_grid)
    elif pixel == black:
        new[area] = np.zeros((3, 3))
    return new

def choose_area(i: int, j: int) -> Tuple[slice, slice]:
    if i == 0 and j == 0:
        return (slice(0, 3), slice(0, 3))
    elif i == 0 and j == 1:
        return (slice(0, 3), slice(3, 6))
    elif i == 0 and j == 2:
        return (slice(0, 3), slice(6, 9))
    elif i == 1 and j == 0:
        return (slice(3, 6), slice(0, 3))
    elif i == 1 and j == 1:
        return (slice(3, 6), slice(3, 6))
    elif i == 1 and j == 2:
        return (slice(3, 6), slice(6, 9))
    elif i == 2 and j == 0:
        return (slice(6, 9), slice(0, 3))
    elif i == 2 and j == 1:
        return (slice(6, 9), slice(3, 6))
    elif i == 2 and j == 2:
        return (slice(6, 9), slice(6, 9))
    else:
        raise ValueError('Invalid indices')

def process_grid(new, input_grid: np.ndarray) -> np.ndarray:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            pixel = input_grid[i][j]
            area = choose_area(i, j)
            new = fill_area(pixel, area, new, input_grid)
    return new

def create_black_grid() -> np.ndarray:
    return np.full((9, 9), black)

def main(input_grid: np.ndarray) -> np.ndarray:
    new = create_black_grid()
    out = process_grid(new, input_grid)
    return out