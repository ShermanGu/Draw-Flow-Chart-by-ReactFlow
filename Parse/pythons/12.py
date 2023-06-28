import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def rotate_second_grid_if_needed(first_grid: np.ndarray, second_grid: np.ndarray) -> np.ndarray:
    if first_grid.shape[0] > first_grid.shape[1]:
        return np.rot90(second_grid)
    return second_grid

def repeat_colors_by_distance(input_grid: np.ndarray, color_and_position: List[Tuple[int, Tuple[int, int]]]) -> np.ndarray:
    (first_color, second_color) = (color_and_position[0][0], color_and_position[1][0])
    distance = abs(color_and_position[0][1][1] - color_and_position[1][1][1])
    start_col = min(color_and_position[0][1][1], color_and_position[1][1][1])
    end_col = max(color_and_position[0][1][1], color_and_position[1][1][1])
    for col in range(start_col, input_grid.shape[1], distance):
        color = first_color if (col - start_col) % (2 * distance) < distance else second_color
        for row in range(input_grid.shape[0]):
            input_grid[row][col] = color
    return input_grid

def set_columns_to_color(input_grid: np.ndarray, color_and_position: List[Tuple[int, Tuple[int, int]]]) -> np.ndarray:
    for (color, position) in color_and_position:
        for i in range(input_grid.shape[0]):
            input_grid[i][position[1]] = color
    return input_grid

def find_non_black_elements(input_grid: np.ndarray) -> List[Tuple[int, Tuple[int, int]]]:
    non_black_elements = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                non_black_elements.append((input_grid[i][j], (i, j)))
                if len(non_black_elements) == 2:
                    return non_black_elements
    return non_black_elements

def rotate_grid(input_grid: np.ndarray) -> np.ndarray:
    if input_grid.shape[0] > input_grid.shape[1]:
        return np.rot90(input_grid)
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = rotate_grid(input_grid)
    color_and_position = find_non_black_elements(output_grid)
    output_grid = set_columns_to_color(output_grid, color_and_position)
    output_grid = repeat_colors_by_distance(output_grid, color_and_position)
    output_grid = rotate_second_grid_if_needed(input_grid, output_grid)
    return output_grid