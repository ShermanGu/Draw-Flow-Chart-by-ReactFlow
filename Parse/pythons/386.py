import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_grey_pixels(left: int, right: int, up: int, down: int, input_grid: np.ndarray) -> np.ndarray:
    """
    Given the left, right, up, and down edges of the blue pixels in the input grid and the input grid itself,
    returns a new grid with all specified pixels filled with grey.

    Args:
    left: An integer representing the left edge of the blue pixels in the input grid.
    right: An integer representing the right edge of the blue pixels in the input grid.
    up: An integer representing the up edge of the blue pixels in the input grid.
    down: An integer representing the down edge of the blue pixels in the input grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the new grid with all specified pixels filled with grey.
    """
    grey_pixels = [(up + 2, left), (up + 4, left), (down - 2, left), (down - 4, left), (up + 2, right), (up + 4, right), (down - 2, right), (down - 4, right), (up, left + 2), (up, left + 4), (up, right - 2), (up, right - 4), (down, left + 2), (down, left + 4), (down, right - 2), (down, right - 4)]
    for (i, j) in grey_pixels:
        input_grid[i][j] = grey
    return input_grid

def find_edges_of_blue_pixels(blueloc: List[Tuple[int, int]]) -> Tuple[int, int, int, int]:
    left = min(blueloc, key=lambda x: x[1])[1]
    right = max(blueloc, key=lambda x: x[1])[1]
    up = min(blueloc, key=lambda x: x[0])[0]
    down = max(blueloc, key=lambda x: x[0])[0]
    return (left, right, up, down)

def fill_yellowloc_with_yellow(yellowloc: List[Tuple[int, int]], input_grid: np.ndarray) -> np.ndarray:
    """
    Given a list of tuples representing the coordinates of all yellow pixels in the input grid and the input grid itself,
    returns a new grid with all the yellow pixels filled with yellow.

    Args:
    yellowloc: A list of tuples representing the coordinates of all yellow pixels in the input grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the new grid with all the yellow pixels filled with yellow.
    """
    for (i, j) in yellowloc:
        input_grid[i][j] = yellow
    return input_grid

def fill_blueloc_with_blue(blueloc: List[Tuple[int, int]], input_grid: np.ndarray) -> np.ndarray:
    """
    Given a list of tuples representing the coordinates of all blue pixels in the input grid and the input grid itself,
    returns a new grid with all the blue pixels filled with blue.

    Args:
    blueloc: A list of tuples representing the coordinates of all blue pixels in the input grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the new grid with all the blue pixels filled with blue.
    """
    for (i, j) in blueloc:
        input_grid[i][j] = blue
    return input_grid

def fill_pixels_around_yellow_with_blue(yellowloc: List[Tuple[int, int]], input_grid: np.ndarray) -> np.ndarray:
    """
    Given a list of tuples representing the coordinates of all yellow pixels in the input grid and the input grid itself,
    returns a new grid with all the pixels around the yellow pixels filled with blue.

    Args:
    yellowloc: A list of tuples representing the coordinates of all yellow pixels in the input grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the new grid with all the pixels around the yellow pixels filled with blue.
    """
    for (i, j) in yellowloc:
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < input_grid.shape[0] and 0 <= y < input_grid.shape[1] and (input_grid[x][y] != yellow):
                    input_grid[x][y] = blue
    return input_grid

def fill_pixels_around_blue_with_yellow(blueloc: List[Tuple[int, int]], input_grid: np.ndarray) -> np.ndarray:
    """
    Given a list of tuples representing the coordinates of all blue pixels in the input grid and the input grid itself,
    returns a new grid with all the pixels around the blue pixels filled with yellow.

    Args:
    blueloc: A list of tuples representing the coordinates of all blue pixels in the input grid.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the new grid with all the pixels around the blue pixels filled with yellow.
    """
    for (i, j) in blueloc:
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < input_grid.shape[0] and 0 <= y < input_grid.shape[1] and (input_grid[x][y] != blue):
                    input_grid[x][y] = yellow
    return input_grid

def find_yellow_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples representing the coordinates of all yellow pixels in the grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A list of tuples representing the coordinates of all yellow pixels in the grid.
    """
    yellow_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == yellow:
                yellow_pixels.append((i, j))
    return yellow_pixels

def find_blue_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples representing the coordinates of all blue pixels in the grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A list of tuples representing the coordinates of all blue pixels in the grid.
    """
    blue_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                blue_pixels.append((i, j))
    return blue_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    blueloc = find_blue_pixels(input_grid)
    yellowloc = find_yellow_pixels(input_grid)
    output_grid = fill_pixels_around_blue_with_yellow(blueloc, input_grid)
    output_grid = fill_pixels_around_yellow_with_blue(yellowloc, output_grid)
    output_grid = fill_blueloc_with_blue(blueloc, output_grid)
    output_grid = fill_yellowloc_with_yellow(yellowloc, output_grid)
    (left, right, up, down) = find_edges_of_blue_pixels(blueloc)
    output_grid = fill_grey_pixels(left, right, up, down, output_grid)
    return output_grid