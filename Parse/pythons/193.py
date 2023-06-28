import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_and_copy_bottom_right_to_bottom_left(input_grid: List[List[int]]) -> List[List[int]]:
    bottom_right = [row[3:] for row in input_grid[3:]]
    bottom_left = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            bottom_left[i][j] = bottom_right[2 - j][i]
    for i in range(3):
        for j in range(3):
            input_grid[i + 3][j] = bottom_left[i][j]
    return input_grid

def rotate_and_copy_top_right_to_bottom_right(input_grid: List[List[int]]) -> List[List[int]]:
    top_right = [row[3:] for row in input_grid[:3]]
    bottom_right = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            bottom_right[i][j] = top_right[2 - j][i]
    for i in range(3):
        for j in range(3):
            input_grid[i + 3][j + 3] = bottom_right[i][j]
    return input_grid

def rotate_and_copy_top_left_to_top_right(input_grid: List[List[int]]) -> List[List[int]]:
    top_left = [row[:3] for row in input_grid[:3]]
    top_right = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            top_right[i][j] = top_left[2 - j][i]
    for i in range(3):
        for j in range(3):
            input_grid[i][j + 3] = top_right[i][j]
    return input_grid

def copy_to_top_left(input_grid: np.ndarray, output_grid: List[List[int]]) -> List[List[int]]:
    for i in range(3):
        for j in range(3):
            output_grid[i][j] = input_grid[i][j]
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = [[0 for i in range(6)] for j in range(6)]
    output_grid = copy_to_top_left(input_grid, output_grid)
    output_grid = rotate_and_copy_top_left_to_top_right(output_grid)
    output_grid = rotate_and_copy_top_right_to_bottom_right(output_grid)
    output_grid = rotate_and_copy_bottom_right_to_bottom_left(output_grid)
    return output_grid