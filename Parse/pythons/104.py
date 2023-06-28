import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_black_points_red_in_row_or_column_with_more_than_two_blue_points(input_grid: np.ndarray, x: int, y: int, minx: int, miny: int, maxx: int, maxy: int):
    row = input_grid[minx + 1:maxx, y]
    col = input_grid[x, miny + 1:maxy]
    if np.count_nonzero(row == blue) >= 2:
        input_grid[minx + 1:maxx, y][input_grid[minx + 1:maxx, y] == black] = red
    elif np.count_nonzero(col == blue) >= 2:
        input_grid[x, miny + 1:maxy][input_grid[x, miny + 1:maxy] == black] = red
    return input_grid

def find_blue_points_within_area(input_grid: np.ndarray, minx: int, miny: int, maxx: int, maxy: int) -> Tuple[int, int]:
    """
    This function takes in a numpy array as input_grid and the minimum and maximum x and y coordinates of an area and returns the coordinates of the blue point within that area.

    Args:
    input_grid: A numpy array of shape (n, m) containing integers from 0 to 9 representing different colors.
    minx: An integer representing the minimum x coordinate of the area.
    miny: An integer representing the minimum y coordinate of the area.
    maxx: An integer representing the maximum x coordinate of the area.
    maxy: An integer representing the maximum y coordinate of the area.

    Returns:
    A tuple of two integers (x, y) representing the coordinates of the blue point within the area.
    """
    blue_points = np.where(input_grid[minx + 1:maxx, miny + 1:maxy] == blue)
    if blue_points[0].size == 0:
        return (-1, -1)
    (x, y) = (blue_points[0][0] + minx + 1, blue_points[1][0] + miny + 1)
    return (x, y)

def color_edge_black_points_red(input_grid: np.ndarray, minx: int, miny: int, maxx: int, maxy: int) -> np.ndarray:
    for i in range(minx, maxx + 1):
        if input_grid[i][miny] == black:
            input_grid[i][miny] = red
        if input_grid[i][maxy] == black:
            input_grid[i][maxy] = red
    for j in range(miny, maxy + 1):
        if input_grid[minx][j] == black:
            input_grid[minx][j] = red
        if input_grid[maxx][j] == black:
            input_grid[maxx][j] = red
    return input_grid

def find_blue_points(input_grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    This function takes in a numpy array as input_grid and returns the minimum and maximum x and y coordinates of all the blue points in the grid.

    Args:
    input_grid: A numpy array of shape (n, m) containing integers from 0 to 9 representing different colors.

    Returns:
    A tuple of four integers (minx, miny, maxx, maxy) representing the minimum and maximum x and y coordinates of all the blue points in the grid.
    """
    blue_points = np.where(input_grid == blue)
    (minx, miny) = np.min(blue_points, axis=1)
    (maxx, maxy) = np.max(blue_points, axis=1)
    return (minx, miny, maxx, maxy)

def main(input_grid: np.ndarray) -> np.ndarray:
    (minx, miny, maxx, maxy) = find_blue_points(input_grid)
    grid1 = color_edge_black_points_red(input_grid, minx, miny, maxx, maxy)
    (x, y) = find_blue_points_within_area(grid1, minx, miny, maxx, maxy)
    output_grid = color_black_points_red_in_row_or_column_with_more_than_two_blue_points(grid1, x, y, minx, miny, maxx, maxy)
    return output_grid