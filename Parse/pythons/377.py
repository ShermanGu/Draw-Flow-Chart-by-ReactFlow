import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def inside_grid(grid: np.ndarray, coordinate: Tuple[int, int]) -> bool:
    (x, y) = coordinate
    return 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]

def draw_diagonal_line_after_meeting_color(grid, line_color, other_color, start_coordinate, direction):
    (x, y) = start_coordinate
    has_meet = False
    while inside_grid(grid, start_coordinate):
        if grid[x][y] == black and has_meet:
            grid[x][y] = line_color
        elif grid[x][y] == other_color:
            has_meet = True
        x += direction[0]
        y += direction[1]
        start_coordinate = (x, y)

def find_rectangle_corners(grid: np.ndarray, color: int) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
    (x, y) = np.where(grid == color)
    (left, top) = (np.min(y), np.min(x))
    (right, bottom) = (np.max(y), np.max(x))
    return ((top, left), (bottom, left), (top, right), (bottom, right))

def is_color_area_rectangle(color: int, grid: np.ndarray) -> bool:
    (x, y) = np.where(grid == color)
    if len(x) == 0:
        return False
    (left, top) = (np.min(y), np.min(x))
    (right, bottom) = (np.max(y), np.max(x))
    return np.all(grid[top:bottom + 1, left:right + 1] == color)

def find_all_colors_except_black(input_grid: np.ndarray) -> Tuple[int, int]:
    colors = set(np.unique(input_grid))
    colors.discard(black)
    return tuple(colors)

def main(input_grid: np.ndarray) -> np.ndarray:
    (color1, color2) = find_all_colors_except_black(input_grid)
    if is_color_area_rectangle(color1, input_grid):
        (rectangle_color, other_color) = (color1, color2)
    else:
        (rectangle_color, other_color) = (color2, color1)
    (left_top, left_bottom, right_top, right_bottom) = find_rectangle_corners(input_grid, rectangle_color)
    draw_diagonal_line_after_meeting_color(input_grid, rectangle_color, other_color, left_top, (-1, -1))
    draw_diagonal_line_after_meeting_color(input_grid, rectangle_color, other_color, left_bottom, (1, -1))
    draw_diagonal_line_after_meeting_color(input_grid, rectangle_color, other_color, right_top, (-1, 1))
    draw_diagonal_line_after_meeting_color(input_grid, rectangle_color, other_color, right_bottom, (1, 1))
    return input_grid