import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_indexes_on_connection_line(point1: Tuple[int, int], point2: Tuple[int, int]) -> List[Tuple[int, int]]:
    (x1, y1) = point1
    (x2, y2) = point2
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 or dy == 0:
        return []
    slope = dy / dx
    if abs(slope) != 1:
        return []
    x_step = 1 if dx > 0 else -1
    y_step = 1 if dy > 0 else -1
    (x, y) = (x1 + x_step, y1 + y_step)
    indexes = []
    while x != x2:
        indexes.append((x, y))
        x += x_step
        y += y_step
    return indexes

def connect_diagonal_blocks(input_grid: np.ndarray, point_list: List[Tuple[int, int]], color: int) -> np.ndarray:
    points = find_indexes_on_connection_line(point_list[0], point_list[1])
    for point in points:
        input_grid[point] = color
    return input_grid

def find_block_indices(input_grid: np.ndarray, color: int) -> List[Tuple[int, int]]:
    indices = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == color:
                indices.append((i, j))
    return indices

def find_non_black_colors(input_grid: np.ndarray) -> List[int]:
    color_list = []
    for row in input_grid:
        for color in row:
            if color != black and color not in color_list:
                color_list.append(color)
    return color_list

def main(input_grid: np.ndarray) -> np.ndarray:
    color_list = find_non_black_colors(input_grid)
    output_grid = np.copy(input_grid)
    for color in color_list:
        point_list = find_block_indices(input_grid, color)
        output_grid = connect_diagonal_blocks(output_grid, point_list, color)
    return output_grid