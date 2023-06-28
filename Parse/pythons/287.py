import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def set_element_to_color_of_first_element_of_last_line(input_grid: np.ndarray, positions: Tuple[Tuple[int, int], Tuple[int, int]]) -> np.ndarray:
    color = find_element(input_grid, positions[0])
    for i in range(positions[0][0], positions[1][0] + 1):
        for j in range(positions[0][1], positions[1][1] + 1):
            if input_grid[i][j] == color:
                input_grid[i][j] = input_grid[-1][0]
    return input_grid

def set_line_upper_right(input_grid: np.ndarray, position: Tuple[int, int], color: int) -> np.ndarray:
    for i in range(position[1], len(input_grid)):
        if input_grid[position[0]][i] != color:
            input_grid[position[0] - (i - position[1])][i] = color
        else:
            break
    return input_grid

def set_line_upper_left(input_grid: np.ndarray, position: Tuple[int, int], color: int) -> np.ndarray:
    for i in range(position[1], -1, -1):
        if input_grid[position[0]][i] != color:
            input_grid[position[0] - position[1] + i][i] = color
        else:
            break
    return input_grid

def find_element(input_grid: np.ndarray, position: Tuple[int, int]) -> int:
    return input_grid[position[0] + 1][position[1]]

def find_penultimate_positions(input_grid: np.ndarray) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    penultimate_line = input_grid[-2]
    first_pos = (len(penultimate_line) - 1, 0)
    last_pos = (len(penultimate_line) - 1, len(penultimate_line) - 1)
    for i in range(len(penultimate_line)):
        if penultimate_line[i] != black:
            first_pos = (len(penultimate_line) - 2, i)
            break
    for i in range(len(penultimate_line) - 1, -1, -1):
        if penultimate_line[i] != black:
            last_pos = (len(penultimate_line) - 2, i)
            break
    return (first_pos, last_pos)

def identity(input_grid: np.ndarray) -> np.ndarray:
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = identity(input_grid)
    (position_first, position_last) = find_penultimate_positions(input_grid)
    color = find_element(input_grid, position_first)
    output_grid = set_line_upper_left(output_grid, position_first, color)
    output_grid = set_line_upper_right(output_grid, position_last, color)
    output_grid = set_element_to_color_of_first_element_of_last_line(output_grid, (position_first, position_last))
    return output_grid