import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_gray_to_neighbour_color(input_grid: np.ndarray) -> np.ndarray:
    for i in range(1, input_grid.shape[0]):
        for j in range(1, input_grid.shape[1]):
            if input_grid[i][j] == grey and input_grid[i - 1][j] != grey and (input_grid[i - 1][j] != black):
                input_grid[i][j] = input_grid[i - 1][j]
            elif input_grid[i][j] == grey and input_grid[i][j - 1] != grey and (input_grid[i][j - 1] != black):
                input_grid[i][j] = input_grid[i][j - 1]
            elif input_grid[i][j] == grey and input_grid[i][j + 1] != grey and (input_grid[i][j + 1] != black):
                input_grid[i][j] = input_grid[i][j + 1]
    return input_grid

def has_gray_pixels(output: np.ndarray) -> bool:
    return np.any(output == grey)

def change_gray_pixels(input_grid: np.ndarray, columns: List[int], colors: List[int]) -> np.ndarray:
    for i in range(1, input_grid.shape[0]):
        for j in columns:
            if input_grid[i][j] == grey:
                input_grid[i][j] = input_grid[0, j]
    return input_grid

def find_first_row_pixels(input_grid: np.ndarray) -> Tuple[List[int], List[int]]:
    first_row = input_grid[0]
    columns = []
    colors = []
    for (i, pixel) in enumerate(first_row):
        if pixel != black:
            columns.append(i)
            colors.append(pixel)
    return (columns, colors)

def main(input_grid: np.ndarray) -> np.ndarray:
    (columns, colors) = find_first_row_pixels(input_grid)
    output = change_gray_pixels(input_grid, columns, colors)
    while has_gray_pixels(output):
        output = change_gray_to_neighbour_color(output)
    return output