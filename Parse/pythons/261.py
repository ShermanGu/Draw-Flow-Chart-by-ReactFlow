import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_row_with_color(i: int, color: int, output_grid: np.ndarray) -> np.ndarray:
    output_grid[i] = color
    return output_grid

def get_color(input_value: int) -> int:
    if input_value == 0:
        return red
    elif input_value == 1:
        return yellow
    elif input_value == 2:
        return green
    else:
        return black

def get_non_black_pixel_column(input_grid: np.ndarray) -> List[int]:
    non_black_pixel_column = []
    for row in input_grid:
        non_black_pixel_column.append(np.where(row != black)[0][0])
    return non_black_pixel_column

def create_output_grid(input_grid: np.ndarray) -> np.ndarray:
    return np.zeros_like(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = create_output_grid(input_grid)
    tmp = get_non_black_pixel_column(input_grid)
    for i in range(3):
        color = get_color(tmp[i])
        output_grid = fill_row_with_color(i, color, output_grid)
    return output_grid