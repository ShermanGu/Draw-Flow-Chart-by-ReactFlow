import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def draw_blue_horizontal_lines(input_grid: np.ndarray, blue_loc: Tuple[int, int]) -> np.ndarray:
    """
    This function takes an input grid and the location of all blue pixels in the grid and draws horizontal blue lines
    passing through each blue pixel.

    Args:
    input_grid: A numpy array representing the input grid.
    blue_loc: A tuple containing the row and column indices of all blue pixels in the grid.

    Returns:
    A numpy array representing the output grid with horizontal blue lines passing through each blue pixel.
    """
    for i in range(len(blue_loc[0])):
        input_grid[blue_loc[0][i], :] = blue
    return input_grid

def draw_green_horizontal_lines(input_grid: np.ndarray, green_loc: Tuple[int, int]) -> np.ndarray:
    """
    This function takes an input grid and the location of all green pixels in the grid and draws horizontal green lines
    passing through each green pixel.

    Args:
    input_grid: A numpy array representing the input grid.
    green_loc: A tuple containing the row and column indices of all green pixels in the grid.

    Returns:
    A numpy array representing the output grid with horizontal green lines passing through each green pixel.
    """
    for i in range(len(green_loc[0])):
        input_grid[green_loc[0][i], :] = green
    return input_grid

def draw_red_vertical_lines(input_grid: np.ndarray, red_loc: Tuple[int, int]) -> np.ndarray:
    """
    This function takes an input grid and the location of all red pixels in the grid and draws vertical red lines
    passing through each red pixel.

    Args:
    input_grid: A numpy array representing the input grid.
    red_loc: A tuple containing the row and column indices of all red pixels in the grid.

    Returns:
    A numpy array representing the output grid with vertical red lines passing through each red pixel.
    """
    for i in range(len(red_loc[0])):
        input_grid[:, red_loc[1][i]] = red
    return input_grid

def get_blue_pixels_location(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes an input grid and returns the location of all blue pixels in the grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple containing the row and column indices of all blue pixels in the grid.
    """
    return np.where(input_grid == blue)

def get_green_pixels_location(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes an input grid and returns the location of all green pixels in the grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple containing the row and column indices of all green pixels in the grid.
    """
    return np.where(input_grid == green)

def get_red_pixels_location(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    This function takes an input grid and returns the location of all red pixels in the grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A tuple containing the row and column indices of all red pixels in the grid.
    """
    return np.where(input_grid == red)

def main(input_grid: np.ndarray) -> np.ndarray:
    red_loc = get_red_pixels_location(input_grid)
    green_loc = get_green_pixels_location(input_grid)
    blue_loc = get_blue_pixels_location(input_grid)
    out_grid = draw_red_vertical_lines(input_grid, red_loc)
    out_grid = draw_green_horizontal_lines(out_grid, green_loc)
    out_grid = draw_blue_horizontal_lines(out_grid, blue_loc)
    return out_grid