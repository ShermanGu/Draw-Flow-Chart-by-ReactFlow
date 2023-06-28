import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_different_color_grid(colors: Tuple[int, int, int, int], top_left: np.ndarray, top_right: np.ndarray, bottom_left: np.ndarray, bottom_right: np.ndarray) -> np.ndarray:
    """
    Given four grids and their respective colors, return the grid whose color is different from the others.
    
    Args:
    colors: A tuple of four integers representing the colors of the four grids.
    top_left: A numpy array representing the top left grid.
    top_right: A numpy array representing the top right grid.
    bottom_left: A numpy array representing the bottom left grid.
    bottom_right: A numpy array representing the bottom right grid.
    
    Returns:
    A numpy array representing the grid whose color is different from the others.
    """
    different_color = [color for color in colors if colors.count(color) == 1][0]
    if top_left[0][0] == different_color:
        return top_left
    elif top_right[0][0] == different_color:
        return top_right
    elif bottom_left[0][0] == different_color:
        return bottom_left
    else:
        return bottom_right

def get_other_colors(top_left: np.ndarray, top_right: np.ndarray, bottom_left: np.ndarray, bottom_right: np.ndarray) -> Tuple[int, int, int, int]:
    colors = []
    for grid in [top_left, top_right, bottom_left, bottom_right]:
        unique_colors = np.unique(grid)
        if len(unique_colors) == 1 and unique_colors[0] == black:
            colors.append(grey)
        else:
            colors.append([color for color in unique_colors if color != black][0])
    return tuple(colors)

def get_four_grids(input_grid: np.ndarray, horizontal_lines: List[int], vertical_lines: List[int]) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    top_left = input_grid[:horizontal_lines[0], :vertical_lines[0]]
    top_right = input_grid[:horizontal_lines[0], vertical_lines[-1] + 1:]
    bottom_left = input_grid[horizontal_lines[-1] + 1:, :vertical_lines[0]]
    bottom_right = input_grid[horizontal_lines[-1] + 1:, vertical_lines[-1] + 1:]
    return (top_left, top_right, bottom_left, bottom_right)

def get_consecutive_vertical_lines(input_grid: np.ndarray) -> List[int]:
    consecutive_lines = []
    for i in range(input_grid.shape[1]):
        if np.all(input_grid[:, i] == black):
            consecutive_lines.append(i)
    return consecutive_lines

def get_consecutive_horizontal_lines(input_grid: np.ndarray) -> List[int]:
    consecutive_lines = []
    for i in range(input_grid.shape[0]):
        if np.all(input_grid[i, :] == black):
            consecutive_lines.append(i)
    return consecutive_lines

def main(input_grid: np.ndarray) -> np.ndarray:
    x = get_consecutive_horizontal_lines(input_grid)
    y = get_consecutive_vertical_lines(input_grid)
    (top_left, top_right, bottom_left, bottom_right) = get_four_grids(input_grid, x, y)
    colors = get_other_colors(top_left, top_right, bottom_left, bottom_right)
    output_grid = get_different_color_grid(colors, top_left, top_right, bottom_left, bottom_right)
    return output_grid