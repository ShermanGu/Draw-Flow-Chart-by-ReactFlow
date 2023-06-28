import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_column_color(grid: np.ndarray, column_index: int, color: int) -> np.ndarray:
    grid[:, column_index] = color
    return grid

def change_row_color(grid: np.ndarray, row_index: int, color: int) -> np.ndarray:
    grid[row_index] = color
    return grid

def find_diagonal_colors(input_grid: np.ndarray) -> List[int]:
    diagonal_colors = []
    for i in range(len(input_grid)):
        diagonal_colors.append(input_grid[i][i])
    return diagonal_colors

def main(input_grid: np.ndarray) -> np.ndarray:
    list = find_diagonal_colors(input_grid)
    list += list
    num = len(list)
    output_grid = np.zeros((num, num), dtype=int)
    for i in range(num):
        output_grid = change_row_color(output_grid, i, list[i])
        output_grid = change_column_color(output_grid, i, list[i])
    return output_grid