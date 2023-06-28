import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_columns(sorted_color_list: List[int], max_color_num_list: List[int]) -> np.ndarray:
    output = np.zeros((max(max_color_num_list), len(sorted_color_list)))
    for (i, color) in enumerate(sorted_color_list):
        output[:max_color_num_list[i], i] = color
    return output

def sort_colors_by_position(color_list: List[int], color_position_list: List[int]) -> List[int]:
    return [color for (_, color) in sorted(zip(color_position_list, color_list))]

def compare_colors(color_list: List[int], color_num_list: List[int]) -> Tuple[List[int], List[int]]:
    max_color_list = []
    max_color_num_list = []
    max_color_num = max(color_num_list)
    for i in range(len(color_list)):
        if color_num_list[i] == max_color_num:
            max_color_list.append(color_list[i])
            max_color_num_list.append(color_num_list[i])
    return (max_color_list, max_color_num_list)

def find_leftmost_position(input_grid: np.ndarray, color_list: List[int]) -> List[int]:
    leftmost_positions = []
    for color in color_list:
        for col in range(input_grid.shape[1]):
            if color in input_grid[:, col]:
                leftmost_positions.append(col)
                break
    return leftmost_positions

def count_colors(input_grid: np.ndarray, color_list: List[int]) -> List[int]:
    color_num_list = []
    for color in color_list:
        color_num_list.append(np.count_nonzero(input_grid == color))
    return color_num_list

def get_colors(input_grid: np.ndarray) -> List[int]:
    return list(set(input_grid.flatten()))[1:]

def main(input_grid: np.ndarray) -> np.ndarray:
    color_list = get_colors(input_grid)
    color_num_list = count_colors(input_grid, color_list)
    color_position_list = find_leftmost_position(input_grid, color_list)
    (max_color_list, max_color_num_list) = compare_colors(color_list, color_num_list)
    sorted_color_list = sort_colors_by_position(max_color_list, color_position_list)
    output = paint_columns(sorted_color_list, max_color_num_list)
    return output