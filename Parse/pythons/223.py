import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def connect_p2_p4_with_color3(input_grid: np.ndarray, color3: int, p2: Tuple[int, int], p4: Tuple[int, int]) -> np.ndarray:
    """
    Given an input grid, color3, p2 and p4, this function connects p2 and p4 with a line of color3.

    Args:
    input_grid: A numpy array representing the input grid.
    color3: An integer representing the third color present in the grid.
    p2: A tuple of two integers representing the coordinates of point p2.
    p4: A tuple of two integers representing the coordinates of point p4.

    Returns:
    A numpy array representing the updated grid.
    """
    (x2, y2) = p2
    (x4, y4) = p4
    if x2 == x4:
        for y in range(min(y2, y4), max(y2, y4) + 1):
            input_grid[x2][y] = color3
    elif y2 == y4:
        for x in range(min(x2, x4), max(x2, x4) + 1):
            input_grid[x][y2] = color3
    return input_grid

def connect_p1_p3_with_color3(input_grid: np.ndarray, color3: int, p1: Tuple[int, int], p3: Tuple[int, int]) -> np.ndarray:
    """
    Given an input grid, color3, p1 and p3, this function connects p1 and p3 with a line of color3.

    Args:
    input_grid: A numpy array representing the input grid.
    color3: An integer representing the third color present in the grid.
    p1: A tuple of two integers representing the coordinates of point p1.
    p3: A tuple of two integers representing the coordinates of point p3.

    Returns:
    A numpy array representing the updated grid.
    """
    (x1, y1) = p1
    (x3, y3) = p3
    if x1 == x3:
        for y in range(min(y1, y3), max(y1, y3) + 1):
            input_grid[x1][y] = color3
    elif y1 == y3:
        for x in range(min(x1, x3), max(x1, x3) + 1):
            input_grid[x][y1] = color3
    return input_grid

def connect_p3_p4_with_color3(input_grid: np.ndarray, color3: int, p3: Tuple[int, int], p4: Tuple[int, int]) -> np.ndarray:
    """
    Given an input grid, color3, p3 and p4, this function connects p3 and p4 with a line of color3.

    Args:
    input_grid: A numpy array representing the input grid.
    color3: An integer representing the third color present in the grid.
    p3: A tuple of two integers representing the coordinates of point p3.
    p4: A tuple of two integers representing the coordinates of point p4.

    Returns:
    A numpy array representing the updated grid.
    """
    (x3, y3) = p3
    (x4, y4) = p4
    if x3 == x4:
        for y in range(min(y3, y4), max(y3, y4) + 1):
            input_grid[x3][y] = color3
    elif y3 == y4:
        for x in range(min(x3, x4), max(x3, x4) + 1):
            input_grid[x][y3] = color3
    return input_grid

def connect_p1_p2_with_color3(input_grid: np.ndarray, color3: int, p1: Tuple[int, int], p2: Tuple[int, int]) -> np.ndarray:
    """
    Given an input grid, color3, p1 and p2, this function connects p1 and p2 with a line of color3.

    Args:
    input_grid: A numpy array representing the input grid.
    color3: An integer representing the third color present in the grid.
    p1: A tuple of two integers representing the coordinates of point p1.
    p2: A tuple of two integers representing the coordinates of point p2.

    Returns:
    A numpy array representing the updated grid.
    """
    (x1, y1) = p1
    (x2, y2) = p2
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            input_grid[x1][y] = color3
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            input_grid[x][y1] = color3
    return input_grid

def find_gray_coordinates(input_grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    Given an input grid, this function returns the minimum and maximum x and y coordinates of the gray cells.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple of four integers representing the minimum and maximum x and y coordinates of the gray cells.
    """
    gray_indices = np.where(input_grid == grey)
    xmin = np.min(gray_indices[0])
    xmax = np.max(gray_indices[0])
    ymin = np.min(gray_indices[1])
    ymax = np.max(gray_indices[1])
    return (xmin, xmax, ymin, ymax)

def find_third_color(input_grid: np.ndarray) -> int:
    """
    Given an input grid, this function returns the third color (besides black and gray) present in the grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    An integer representing the third color present in the grid.
    """
    (colors, counts) = np.unique(input_grid, return_counts=True)
    for (color, count) in zip(colors, counts):
        if color not in [black, grey] and count > 0:
            return color

def main(input_grid: np.ndarray) -> np.ndarray:
    color3 = find_third_color(input_grid)
    (xmin, xmax, ymin, ymax) = find_gray_coordinates(input_grid)
    p1 = (xmin + 1, ymin + 1)
    p2 = (xmin + 1, ymax - 1)
    p3 = (xmax - 1, ymin + 1)
    p4 = (xmax - 1, ymax - 1)
    output_grid = np.copy(input_grid)
    output_grid = connect_p1_p2_with_color3(output_grid, color3, p1, p2)
    output_grid = connect_p3_p4_with_color3(output_grid, color3, p3, p4)
    output_grid = connect_p1_p3_with_color3(output_grid, color3, p1, p3)
    output_grid = connect_p2_p4_with_color3(output_grid, color3, p2, p4)
    return output_grid