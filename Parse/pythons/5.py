import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def set_to_2(grid: np.ndarray, x: int, y: int) -> np.ndarray:
    grid[x][y] = 2
    return grid

def both_equal(a: int, b: int, num: int) -> bool:
    return a == b == num

def samepixels(outleft, outright):
    out = np.zeros((3, 3), dtype=int)
    for i in range(0, outleft.shape[0]):
        for j in range(0, outleft.shape[1]):
            if both_equal(a=outleft[i][j], b=outright[i][j], num=1):
                out = set_to_2(out, x=i, y=j)
    return out

def extract_middle_grid(grid: np.ndarray) -> np.ndarray:
    return grid[:, 4:7]

def extract_left_grid(grid: np.ndarray) -> np.ndarray:
    return grid[:, :3]

def main(input_grid: np.ndarray) -> np.ndarray:
    outleft = np.zeros((3, 3), dtype=int)
    outright = np.zeros((3, 3), dtype=int)
    outleft = extract_left_grid(input_grid)
    outright = extract_middle_grid(input_grid)
    out = np.zeros((3, 3), dtype=int)
    out = samepixels(outleft, outright)
    return out