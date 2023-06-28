import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_with_green(input_grid: np.ndarray, r1: int, r2: int, j: int, gap: int) -> np.ndarray:
    out = np.copy(input_grid)
    out[r1 - gap:r2 + gap + 1, j - gap:j + gap + r2 - r1 + 1][out[r1 - gap:r2 + gap + 1, j - gap:j + gap + r2 - r1 + 1] != maroon] = green
    return out

def get_maroon_rows(input_grid: np.ndarray, j: int) -> Tuple[int, int]:
    maroon_rows = np.where(input_grid[:, j] == maroon)[0]
    return (maroon_rows[0], maroon_rows[-1])

def has_maroon_and_no_green_below_maroon(input_grid: np.ndarray, j: int) -> bool:
    if maroon in input_grid[:, j]:
        maroon_row = np.where(input_grid[:, j] == maroon)[0][0]
        if green not in input_grid[maroon_row + 1:, j]:
            return True
    return False

def get_width(grid: np.ndarray) -> int:
    return grid.shape[1]

def replace_black_with_blue_below_maroon(input_grid: np.ndarray) -> np.ndarray:
    out = np.copy(input_grid)
    for j in range(out.shape[1]):
        if maroon in out[:, j]:
            maroon_row = np.where(out[:, j] == maroon)[0][0]
            out[maroon_row + 1:, j][out[maroon_row + 1:, j] == black] = blue
    return out

def main(input_grid: np.ndarray) -> np.ndarray:
    out = replace_black_with_blue_below_maroon(input_grid)
    w = get_width(out)
    for j in range(w):
        flag = has_maroon_and_no_green_below_maroon(out, j)
        if flag:
            (r1, r2) = get_maroon_rows(out, j)
            gap = (r2 - r1 + 1) // 2
            out = replace_with_green(out, r1, r2, j, gap)
    return out