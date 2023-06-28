import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_points_between(input_grid: np.ndarray, non_black_point: Tuple[int, int], i: int, j: int) -> None:
    (x, y) = non_black_point
    color = input_grid[x, y]
    if i == x:
        for k in range(min(j, y), max(j, y)):
            if input_grid[i, k] == black:
                input_grid[i, k] = color
    elif j == y:
        for k in range(min(i, x), max(i, x)):
            if input_grid[k, j] == black:
                input_grid[k, j] = color

def color_black_points(input_grid: np.ndarray, corner: Tuple[int, int]) -> None:
    (i, j) = corner
    row = input_grid[i, :]
    col = input_grid[:, j]
    row_non_black = np.where(row != black)[0]
    col_non_black = np.where(col != black)[0]
    if len(row_non_black) > 1:
        non_black_point = (i, row_non_black[0])
        color_points_between(input_grid, non_black_point, i, j)
        non_black_point = (i, row_non_black[-1])
        color_points_between(input_grid, non_black_point, i, j)
    if len(col_non_black) > 1:
        non_black_point = (col_non_black[0], j)
        color_points_between(input_grid, non_black_point, i, j)
        non_black_point = (col_non_black[-1], j)
        color_points_between(input_grid, non_black_point, i, j)

def find_green_area(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes a numpy array as input and returns the left-up coordinate of the 2*2 green area in the grid.
    
    Args:
    input_grid: A numpy array representing the grid.
    
    Returns:
    A tuple of two integers representing the left-up coordinate of the 2*2 green area in the grid.
    """
    (i, j) = np.where(input_grid == green)
    return (i[0], j[0])

def main(input_grid: np.ndarray) -> np.ndarray:
    (i, j) = find_green_area(input_grid)
    green_square = [(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)]
    for corner in green_square:
        color_black_points(input_grid, corner)
    return input_grid