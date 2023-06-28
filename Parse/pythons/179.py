import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_color_with_grey_4x4(out: np.ndarray, b: np.ndarray) -> np.array:
    out[:4, :4][b[:4, :4] != black] = grey
    return out

def replace_color_with_grey(out: np.ndarray, b: np.ndarray) -> np.array:
    out = replace_color_with_grey_4x4(out, b)
    return out

def replace_color_with_pink(out: np.ndarray, c: np.ndarray) -> np.ndarray:
    out[:4, :4][c[:4, :4] == pink] = pink
    return out

def replace_color_with_maroon(out: np.ndarray, d: np.ndarray) -> np.ndarray:
    out[:4, :4][d[:4, :4] == maroon] = maroon
    return out

def replace_color(out: np.ndarray, a: np.ndarray) -> np.ndarray:
    out[:4, :4][a[:4, :4] == yellow] = yellow
    return out

def build_black_matrix() -> np.ndarray:
    return np.full((4, 4), black)

def divide_into_4(input_grid: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    a = input_grid[:4, :4]
    b = input_grid[:4, 4:]
    c = input_grid[4:, :4]
    d = input_grid[4:, 4:]
    return (a, b, c, d)

def main(input_grid: np.ndarray) -> np.ndarray:
    (a, b, c, d) = divide_into_4(input_grid)
    out = build_black_matrix()
    out = replace_color(out, a)
    out = replace_color_with_maroon(out, d)
    out = replace_color_with_pink(out, c)
    out = replace_color_with_grey(out, b)
    return out