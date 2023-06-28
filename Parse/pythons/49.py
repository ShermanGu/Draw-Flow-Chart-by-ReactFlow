import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_pixels_to_green_between_teal_pixels_in_same_column(input_grid: np.ndarray, teal_pixels: List[Tuple[int, int]]) -> np.ndarray:
    """
    Given an input grid and a list of tuples representing the (row, column) indices of all teal pixels in the grid,
    changes the pixels to green between each pair of teal pixels which are in the same column.

    Args:
    - input_grid (np.ndarray): A 2D numpy array representing the input grid.
    - teal_pixels (List[Tuple[int, int]]): A list of tuples representing the (row, column) indices of all teal pixels in the grid.

    Returns:
    - np.ndarray: A 2D numpy array representing the output grid with pixels changed to green between each pair of teal pixels which are in the same column.
    """
    for i in range(len(teal_pixels)):
        for j in range(i + 1, len(teal_pixels)):
            if teal_pixels[i][1] == teal_pixels[j][1]:
                start_row = teal_pixels[i][0]
                end_row = teal_pixels[j][0]
                if start_row > end_row:
                    (start_row, end_row) = (end_row, start_row)
                for k in range(start_row + 1, end_row):
                    input_grid[k][teal_pixels[i][1]] = green
    return input_grid

def change_pixels_to_green_between_teal_pixels(input_grid: np.ndarray, teal_pixels: List[Tuple[int, int]]) -> np.ndarray:
    """
    Given an input grid and a list of tuples representing the (row, column) indices of all teal pixels in the grid,
    changes the pixels to green between each pair of teal pixels which are in the same row.
    
    Args:
    - input_grid (np.ndarray): A 2D numpy array representing the input grid.
    - teal_pixels (List[Tuple[int, int]]): A list of tuples representing the (row, column) indices of all teal pixels in the grid.
    
    Returns:
    - np.ndarray: A 2D numpy array representing the output grid with pixels changed to green between each pair of teal pixels which are in the same row.
    """
    for i in range(len(teal_pixels)):
        for j in range(i + 1, len(teal_pixels)):
            if teal_pixels[i][0] == teal_pixels[j][0]:
                start_col = teal_pixels[i][1]
                end_col = teal_pixels[j][1]
                if start_col > end_col:
                    (start_col, end_col) = (end_col, start_col)
                for k in range(start_col + 1, end_col):
                    input_grid[teal_pixels[i][0]][k] = green
    return input_grid

def find_teal_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Given an input grid, returns a list of tuples representing the (row, column) indices of all teal pixels in the grid.
    
    Args:
    - input_grid (np.ndarray): A 2D numpy array representing the input grid.
    
    Returns:
    - List[Tuple[int, int]]: A list of tuples representing the (row, column) indices of all teal pixels in the grid.
    """
    teal_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == teal:
                teal_pixels.append((i, j))
    return teal_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    locs = find_teal_pixels(input_grid)
    out_grid = change_pixels_to_green_between_teal_pixels(input_grid, locs)
    out_grid = change_pixels_to_green_between_teal_pixels_in_same_column(out_grid, locs)
    return out_grid