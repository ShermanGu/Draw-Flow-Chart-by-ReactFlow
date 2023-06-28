import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_black_points(input_grid: np.ndarray, color2: int) -> None:
    """
    This function colors all the black points in the input grid with the color2 value.

    Args:
    input_grid: A numpy array of shape (3, 3) containing integers from 0 to 9.
    color2: An integer representing the color to be used for coloring the black points.

    Returns:
    None
    """
    for i in range(3):
        for j in range(3):
            if input_grid[i][j] == black:
                input_grid[i][j] = color2

def copy_color1_points(input_grid: np.ndarray, output: np.ndarray, color1: int) -> None:
    color1_points = np.where(input_grid == color1)
    minx = min(color1_points[0])
    miny = min(color1_points[1])
    for i in range(3):
        for j in range(3):
            if input_grid[minx + i][miny + j] == color1:
                output[i][j] = color1

def get_non_black_colors(input_grid: np.ndarray) -> Tuple[int, int]:
    colors_set = set(input_grid.flatten()) - {black}
    colors = tuple(colors_set)
    c1 = colors[0]
    num1 = np.sum(input_grid == c1)
    c2 = colors[1]
    num2 = np.sum(input_grid == c2)
    if num1 > num2:
        return (colors[0], colors[1])
    else:
        return (colors[1], colors[0])

def main(input_grid: np.ndarray) -> np.ndarray:
    output = np.zeros((3, 3), dtype=int)
    (color1, color2) = get_non_black_colors(input_grid)
    copy_color1_points(input_grid, output, color1)
    color_black_points(output, color2)
    return output