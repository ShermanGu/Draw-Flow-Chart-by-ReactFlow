import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def move_left_two_points(input_grid: np.ndarray, current_point: Tuple[int, int]) -> Tuple[int, int]:
    """
    Given a 2D numpy array and a tuple of coordinates, returns the coordinates of the point two columns to the left of the current point.
    """
    (row, col) = current_point
    return (row, col - 2)

def draw_left_points_grey(input_grid: np.ndarray, current_point: Tuple[int, int]) -> np.ndarray:
    """
    Given a 2D numpy array and a tuple of coordinates, draws the two left adjacent points of the current point to grey.
    """
    (row, col) = current_point
    if col > 0:
        input_grid[row][col - 1] = grey
    if col > 1:
        input_grid[row][col - 2] = grey
    return input_grid

def move_down_two_points(input_grid: np.ndarray, current_point: Tuple[int, int]) -> Tuple[int, int]:
    """
    Given a 2D numpy array and a tuple of coordinates, returns the coordinates of the point two rows below the current point.
    """
    (row, col) = current_point
    return (row + 2, col)

def draw_lower_points_grey(input_grid: np.ndarray, current_point: Tuple[int, int]) -> np.ndarray:
    """
    Given a 2D numpy array and a tuple of coordinates, draws the two lower adjacent points of the current point to grey.
    """
    (row, col) = current_point
    if row < input_grid.shape[0] - 1:
        input_grid[row + 1][col] = grey
    if row < input_grid.shape[0] - 2:
        input_grid[row + 2][col] = grey
    return input_grid

def move_right_two_points(input_grid: np.ndarray, current_point: Tuple[int, int]) -> Tuple[int, int]:
    """
    Given a 2D numpy array and a tuple of coordinates, returns the coordinates of the point two columns to the right of the current point.
    """
    (row, col) = current_point
    return (row, col + 2)

def draw_right_points_grey(input_grid: np.ndarray, current_point: Tuple[int, int]) -> np.ndarray:
    """
    Given a 2D numpy array and a tuple of coordinates, draws the two right adjacent points of the current point to grey.
    """
    (row, col) = current_point
    if col < input_grid.shape[1] - 1:
        input_grid[row][col + 1] = grey
    if col < input_grid.shape[1] - 2:
        input_grid[row][col + 2] = grey
    return input_grid

def move_up_two_points(input_grid: np.ndarray, current_point: Tuple[int, int]) -> Tuple[int, int]:
    """
    Given a 2D numpy array and a tuple of coordinates, returns the coordinates of the point two rows above the current point.
    """
    (row, col) = current_point
    return (row - 2, col)

def draw_upper_points_grey(input_grid: np.ndarray, current_point: Tuple[int, int]) -> np.ndarray:
    """
    Given a 2D numpy array and a tuple of coordinates, draws the two upper points of the current point to grey.
    """
    (row, col) = current_point
    if row > 0:
        input_grid[row - 1][col] = grey
    if row > 1:
        input_grid[row - 2][col] = grey
    return input_grid

def _check_boundary(input_grid: np.ndarray, current_point: Tuple[int, int]) -> bool:
    """
    Given a 2D numpy array and a tuple of coordinates, returns True if the coordinates are within the boundaries of the array.
    """
    (rows, cols) = input_grid.shape
    (row, col) = current_point
    return 0 <= row < rows and 0 <= col < cols

def find_teal_point(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Given a 2D numpy array, returns the coordinates of the first occurrence of the value "teal".
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == teal:
                return (i, j)
    raise ValueError('Teal point not found in input grid.')

def main(input_grid: np.ndarray) -> np.ndarray:
    teal_point = find_teal_point(input_grid)
    current_point = teal_point
    while _check_boundary(input_grid, current_point):
        input_grid = draw_upper_points_grey(input_grid, current_point)
        current_point = move_up_two_points(input_grid, current_point)
        if _check_boundary(input_grid, current_point) == False:
            break
        input_grid = draw_right_points_grey(input_grid, current_point)
        current_point = move_right_two_points(input_grid, current_point)
    current_point = teal_point
    while _check_boundary(input_grid, current_point):
        input_grid = draw_lower_points_grey(input_grid, current_point)
        current_point = move_down_two_points(input_grid, current_point)
        if _check_boundary(input_grid, current_point) == False:
            break
        input_grid = draw_left_points_grey(input_grid, current_point)
        current_point = move_left_two_points(input_grid, current_point)
    return input_grid