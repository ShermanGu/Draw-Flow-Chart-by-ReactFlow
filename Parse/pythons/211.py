import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def draw_red_lines(input_grid: np.ndarray, x_gray: int, locs_red_a: List[Tuple[int, int]], locs_red_b: List[Tuple[int, int]]) -> np.ndarray:
    """
    Given an input grid, the location of red pixels above and below the gray line, this function draws red lines from red pixels towards the g

    Args:
    input_grid: A numpy array representing the input grid.
    x_gray: An integer representing the location of the gray line.
    locs_red_a: A list of tuples representing the location of red pixels above the gray line.
    locs_red_b: A list of tuples representing the location of red pixels below the gray line.

    Returns:
    A numpy array representing the updated grid.
    """
    for (i, j) in locs_red_b:
        for k in range(i - 1, x_gray, -1):
            if input_grid[k][j] != red:
                input_grid[k][j] = red
    for (i, j) in locs_red_a:
        for k in range(i + 1, x_gray):
            if input_grid[k][j] != red:
                input_grid[k][j] = red
    return input_grid

def draw_blue_lines(input_grid: np.ndarray, locs_blue_a: List[Tuple[int, int]], locs_blue_b: List[Tuple[int, int]]) -> np.ndarray:
    """
    Given an input grid, the location of blue pixels above and below the gray line, this function draws blue lines from blue pixels away from the gray line to the boundary of the grid.

    Args:
    input_grid: A numpy array representing the input grid.
    locs_blue_a: A list of tuples representing the location of blue pixels above the gray line.
    locs_blue_b: A list of tuples representing the location of blue pixels below the gray line.

    Returns:
    A numpy array representing the updated grid.
    """
    for (i, j) in locs_blue_a:
        for k in range(i):
            if input_grid[k][j] != blue:
                input_grid[k][j] = blue
    for (i, j) in locs_blue_b:
        for k in range(i + 1, input_grid.shape[0]):
            if input_grid[k][j] != blue:
                input_grid[k][j] = blue
    return input_grid

def find_red_pixels_below_gray_line(input_grid: np.ndarray, x_gray: int) -> List[Tuple[int, int]]:
    """
    Given an input grid and the location of the gray line, this function finds the location of red pixels which are below the gray line.

    Args:
    input_grid: A numpy array representing the input grid.
    x_gray: An integer representing the location of the gray line.

    Returns:
    A list of tuples representing the location of red pixels which are below the gray line.
    """
    red_pixels = []
    for i in range(x_gray, input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                red_pixels.append((i, j))
    return red_pixels

def find_red_pixels_above_gray_line(input_grid: np.ndarray, x_gray: int) -> List[Tuple[int, int]]:
    """
    Given an input grid and the location of the gray line, this function finds the location of red pixels which are above the gray line.

    Args:
    input_grid: A numpy array representing the input grid.
    x_gray: An integer representing the location of the gray line.

    Returns:
    A list of tuples representing the location of red pixels which are above the gray line.
    """
    red_pixels = []
    for i in range(x_gray):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                red_pixels.append((i, j))
    return red_pixels

def find_blue_pixels_below_gray_line(input_grid: np.ndarray, x_gray: int) -> List[Tuple[int, int]]:
    """
    Given an input grid and the location of the gray line, this function finds the location of blue pixels which are below the gray line.

    Args:
    input_grid: A numpy array representing the input grid.
    x_gray: An integer representing the location of the gray line.

    Returns:
    A list of tuples representing the location of blue pixels which are below the gray line.
    """
    blue_pixels = []
    for i in range(x_gray, input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                blue_pixels.append((i, j))
    return blue_pixels

def find_blue_pixels_above_gray_line(input_grid: np.ndarray, x_gray: int) -> List[Tuple[int, int]]:
    """
    Given an input grid and the location of the gray line, this function finds the location of blue pixels which are above the gray line.

    Args:
    input_grid: A numpy array representing the input grid.
    x_gray: An integer representing the location of the gray line.

    Returns:
    A list of tuples representing the location of blue pixels which are above the gray line.
    """
    blue_pixels = []
    for i in range(x_gray):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                blue_pixels.append((i, j))
    return blue_pixels

def find_gray_line_location(input_grid: np.ndarray) -> int:
    """
    Given an input grid, this function finds the location of the gray line.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    An integer representing the location of the gray line.
    """
    for i in range(input_grid.shape[0]):
        if np.array_equal(input_grid[i], np.array([grey] * input_grid.shape[1])):
            return i
    return -1

def main(input_grid: np.ndarray) -> np.ndarray:
    x_gray = find_gray_line_location(input_grid)
    locs_blue_a = find_blue_pixels_above_gray_line(input_grid, x_gray)
    locs_blue_b = find_blue_pixels_below_gray_line(input_grid, x_gray)
    locs_red_a = find_red_pixels_above_gray_line(input_grid, x_gray)
    locs_red_b = find_red_pixels_below_gray_line(input_grid, x_gray)
    out_grid = draw_blue_lines(input_grid, locs_blue_a, locs_blue_b)
    out_grid = draw_red_lines(out_grid, x_gray, locs_red_a, locs_red_b)
    return out_grid