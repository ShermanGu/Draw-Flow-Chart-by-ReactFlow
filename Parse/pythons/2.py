import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_blue_to_red(input_grid: np.ndarray) -> np.ndarray:
    output = np.copy(input_grid)
    output[output == blue] = red
    return output

def copy_bottom_to_output_bottom_three_rows(bottom: np.ndarray, output: np.ndarray) -> np.ndarray:
    output[-3:, :] = bottom[:3, :]
    return output

def symmetrical_left_right(input_grid: np.ndarray) -> np.ndarray:
    return np.concatenate((input_grid[:, ::-1], input_grid), axis=1)[:, :3]

def copy_up_six_rows(input_grid: np.ndarray, output: np.ndarray) -> np.ndarray:
    output[:6, :] = input_grid
    return output

def create_array() -> np.ndarray:
    return np.zeros((9, 3), dtype=int)

def main(input_grid: np.ndarray) -> np.ndarray:
    output = create_array()
    output = copy_up_six_rows(input_grid, output)
    bottom = symmetrical_left_right(input_grid)
    output = copy_bottom_to_output_bottom_three_rows(bottom, output)
    output = turn_blue_to_red(output)
    return output