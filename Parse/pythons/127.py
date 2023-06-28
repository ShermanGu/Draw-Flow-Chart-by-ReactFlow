import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_gray_squares_to_black(grid: np.ndarray) -> np.ndarray:
    gray_indices = np.where(grid == grey)
    gray_rows = gray_indices[0]
    gray_columns = gray_indices[1]
    for i in range(len(gray_rows)):
        grid[gray_rows[i]][gray_columns[i]] = black
    return grid

def move_blue_matrix_up(grid: np.ndarray, num_rows: int) -> np.ndarray:
    blue_indices = np.where(grid == blue)
    blue_rows = blue_indices[0]
    blue_columns = blue_indices[1]
    min_row = np.min(blue_rows)
    max_row = np.max(blue_rows)
    if min_row - num_rows >= 0:
        for i in range(len(blue_rows)):
            grid[blue_rows[i]][blue_columns[i]] = 0
            grid[blue_rows[i] - num_rows][blue_columns[i]] = blue
    else:
        for i in range(len(blue_rows)):
            grid[blue_rows[i]][blue_columns[i]] = 0
            grid[blue_rows[i] + max_row - min_row + 1][blue_columns[i]] = blue
    return grid

def move_yellow_matrix_up(grid: np.ndarray, num_rows: int) -> np.ndarray:
    yellow_indices = np.where(grid == yellow)
    yellow_rows = yellow_indices[0]
    yellow_columns = yellow_indices[1]
    min_row = np.min(yellow_rows)
    max_row = np.max(yellow_rows)
    if min_row - num_rows >= 0:
        for i in range(len(yellow_rows)):
            grid[yellow_rows[i]][yellow_columns[i]] = 0
            grid[yellow_rows[i] - num_rows][yellow_columns[i]] = yellow
    else:
        for i in range(len(yellow_rows)):
            grid[yellow_rows[i]][yellow_columns[i]] = 0
            grid[yellow_rows[i] + max_row - min_row + 1][yellow_columns[i]] = yellow
    return grid

def move_red_squares_up(grid: np.ndarray, num_rows: int) -> np.ndarray:
    red_indices = np.where(grid == red)
    red_rows = red_indices[0]
    red_columns = red_indices[1]
    for i in range(len(red_rows)):
        if red_rows[i] - num_rows >= 0:
            grid[red_rows[i]][red_columns[i]] = 0
            grid[red_rows[i] - num_rows][red_columns[i]] = red
    return grid

def find_blue_matrix_size(grid: np.ndarray) -> Tuple[int, int]:
    blue_indices = np.where(grid == blue)
    rows = np.unique(blue_indices[0]).size
    columns = np.unique(blue_indices[1]).size
    return (rows, columns)

def find_yellow_matrix_size(grid: np.ndarray) -> Tuple[int, int]:
    yellow_indices = np.where(grid == yellow)
    rows = np.unique(yellow_indices[0]).size
    columns = np.unique(yellow_indices[1]).size
    return (rows, columns)

def find_red_matrix_size(grid: np.ndarray) -> Tuple[int, int]:
    red_indices = np.where(grid == red)
    rows = np.unique(red_indices[0]).size
    columns = np.unique(red_indices[1]).size
    return (rows, columns)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.copy(input_grid)
    (red_row, red_column) = find_red_matrix_size(output_grid)
    (yellow_row, yellow_column) = find_yellow_matrix_size(output_grid)
    (blue_row, blue_column) = find_blue_matrix_size(output_grid)
    output_grid = move_red_squares_up(output_grid, red_row)
    output_grid = move_yellow_matrix_up(output_grid, yellow_row)
    output_grid = move_blue_matrix_up(output_grid, blue_row)
    output_grid = turn_gray_squares_to_black(output_grid)
    return output_grid