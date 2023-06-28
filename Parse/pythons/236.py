import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_line_in_grid(grid: np.ndarray, line: np.ndarray, index: int) -> np.ndarray:
    grid[index] = line
    return grid

def replace_black_with_last_color(line: np.ndarray, last_color: int) -> np.ndarray:
    output_line = np.zeros_like(line)
    output_line[:-1] = line[:-1]
    output_line[-1] = last_color
    return output_line

def replace_element_behind_non_black(line: np.ndarray, pos: int, color: int) -> np.ndarray:
    output_line = np.zeros_like(line)
    output_line[:pos] = black
    output_line[pos:] = color
    return output_line

def find_non_black_element(line: np.ndarray) -> Tuple[Optional[int], Optional[int]]:
    for (i, color) in enumerate(line):
        if color != black:
            return (i, color)
    return (None, None)

def create_black_grid(input_grid: np.ndarray) -> np.ndarray:
    return np.zeros_like(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = create_black_grid(input_grid)
    last_color = black
    for (index, line) in enumerate(input_grid):
        (pos, color) = find_non_black_element(line)
        if pos != None:
            output_line = replace_element_behind_non_black(line, pos, color)
            last_color = color
        else:
            output_line = replace_black_with_last_color(line, last_color)
        output_grid = replace_line_in_grid(output_grid, output_line, index)
    return output_grid