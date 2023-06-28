import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def calculate_area_size(x_min: int, x_max: int, y_min: int, y_max: int) -> int:
    """
    Given the top-left and bottom-right coordinates of a rectangle, this function calculates the area size.

    Args:
    x_min: An integer representing the x-coordinate of the top-left corner of the rectangle.
    x_max: An integer representing the x-coordinate of the bottom-right corner of the rectangle.
    y_min: An integer representing the y-coordinate of the top-left corner of the rectangle.
    y_max: An integer representing the y-coordinate of the bottom-right corner of the rectangle.

    Returns:
    An integer representing the area size of the rectangle.
    """
    return (x_max - x_min + 1) * (y_max - y_min + 1)

def find_most_bottom_point(input_grid: np.ndarray, color: int) -> int:
    for i in range(input_grid.shape[0] - 1, -1, -1):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == color:
                return i
    return -1

def find_most_top_point(input_grid: np.ndarray, color: int) -> int:
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == color:
                return i
    return -1

def find_most_right_point(input_grid: np.ndarray, color: int) -> int:
    for j in range(input_grid.shape[1] - 1, -1, -1):
        for i in range(input_grid.shape[0]):
            if input_grid[i][j] == color:
                return j
    return -1

def find_most_left_point(input_grid: np.ndarray, color: int) -> int:
    for j in range(input_grid.shape[1]):
        for i in range(input_grid.shape[0]):
            if input_grid[i][j] == color:
                return j
    return -1

def draw_largest_color_area(area_size_list: List[Tuple[int, int]]) -> np.ndarray:
    sorted_list = sorted(area_size_list, key=lambda x: x[1], reverse=True)
    largest_color = sorted_list[0][0]
    output = np.full((2, 2), largest_color)
    return output

def find_color_areas(input_grid: np.ndarray, color_list: List[int]) -> List[Tuple[int, int]]:
    color_areas = []
    for color in color_list:
        x_min = find_most_left_point(input_grid, color)
        x_max = find_most_right_point(input_grid, color)
        y_min = find_most_top_point(input_grid, color)
        y_max = find_most_bottom_point(input_grid, color)
        area = calculate_area_size(x_min, x_max, y_min, y_max)
        color_areas.append((color, area))
    return color_areas

def find_not_black_colors(input_grid: np.ndarray) -> List[int]:
    """
    Given an input grid, this function returns a list of all the non-black colors present in the grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A list of integers representing the non-black colors present in the grid.
    """
    color_list = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black and input_grid[i][j] not in color_list:
                color_list.append(input_grid[i][j])
    return color_list

def main(input_grid: np.ndarray) -> np.ndarray:
    color_list = find_not_black_colors(input_grid)
    area_size_list = find_color_areas(input_grid, color_list)
    output = draw_largest_color_area(area_size_list)
    return output