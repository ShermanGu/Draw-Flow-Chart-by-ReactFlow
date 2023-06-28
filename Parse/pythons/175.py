import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_last_three_black_with_yellow(arr: np.ndarray) -> np.ndarray:
    for i in range(2, len(arr), 12):
        arr[i + 9:i + 12] = yellow
    return arr

def replace_black_with_yellow_in_first_two(arr: np.ndarray) -> np.ndarray:
    for i in range(0, 2):
        if arr[i] == black:
            arr[i] = yellow
    return arr

def replace_black_with_yellow_in_last_three(arr: np.ndarray) -> np.ndarray:
    output_grid = replace_black_with_yellow_in_first_two(arr)
    output_grid = replace_last_three_black_with_yellow(output_grid)
    return output_grid

def replace_black_with_yellow_in_avg_six(arr: np.ndarray) -> np.ndarray:
    for i in range(0, len(arr), 6):
        arr[i:i + 1] = yellow
    return arr

def replace_black_with_yellow(arr: np.ndarray) -> np.ndarray:
    for i in range(5, len(arr), 12):
        arr[i:i + 3] = yellow
    return arr

def create_new_grid(input_grid: np.ndarray) -> np.ndarray:
    return np.zeros_like(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = create_new_grid(input_grid)
    output_grid[0] = replace_black_with_yellow(input_grid[0])
    output_grid[1] = replace_black_with_yellow_in_avg_six(input_grid[1])
    output_grid[2] = replace_black_with_yellow_in_last_three(input_grid[2])
    return output_grid