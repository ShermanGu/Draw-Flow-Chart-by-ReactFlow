import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_teal_pixels(o: np.ndarray) -> np.ndarray:
    """
    This function replaces teal pixels in o based on their position relative to the diagonal of o.

    Args:
    - o: a numpy array representing the copy of l with the square area s copied to the black area in the middle

    Returns:
    - out: a numpy array representing the copy of l with the square area s copied to the black area in the middle and teal pixels replaced based on their position relative to the diagonal of o
    """
    (height, width) = o.shape
    diagonal = np.diag(np.full(height, True))
    (rows, cols) = np.where((o == teal) & (diagonal == False))
    for (row, col) in zip(rows, cols):
        if row > col and row + col < height - 1:
            o[row, col] = o[:, 0][row]
        elif row > col and row + col > height - 1:
            o[row, col] = o[-1, :][col]
        elif row < col and row + col < height - 1:
            o[row, col] = o[0, :][col]
        elif row < col and row + col > height - 1:
            o[row, col] = o[:, -1][row]
    return o

def copy_square_to_middle(s: np.ndarray, l: np.ndarray) -> np.ndarray:
    """
    This function creates a copy of l, finds the inner black area in l, and copies the square area s to the black area in the copy of l.

    Args:
    - s: a numpy array representing the smallest rectangle that covers all teal pixels in the input grid
    - l: a numpy array representing the smallest rectangle that covers all non-black teal pixels in the input grid

    Returns:
    - out: a numpy array representing the copy of l with the square area s copied to the black area in the middle
    """
    out = np.copy(l)
    (rows, cols) = np.where(l == black)
    (min_row, max_row) = (np.min(rows), np.max(rows))
    (min_col, max_col) = (np.min(cols), np.max(cols))
    (height, width) = l.shape
    (s_height, s_width) = s.shape
    row_offset = (height - s_height) // 2
    col_offset = (width - s_width) // 2
    out[min_row + row_offset:min_row + row_offset + s_height, min_col + col_offset:min_col + col_offset + s_width] = s
    return out

def find_smallest_covering_area(input_grid: np.ndarray, p: np.ndarray) -> np.ndarray:
    """
    This function finds the smallest rectangle that covers all non-black teal pixels in the input grid.

    Args:
    - input_grid: a numpy array representing the input grid
    - p: a numpy array representing the non-black teal pixels in the input grid

    Returns:
    - l: a numpy array representing the smallest rectangle that covers all non-black teal pixels in the input grid
    """
    (rows, cols) = np.where(p == 1)
    (min_row, max_row) = (np.min(rows), np.max(rows))
    (min_col, max_col) = (np.min(cols), np.max(cols))
    l = input_grid[min_row:max_row + 1, min_col:max_col + 1]
    return l

def find_smallest_area(input_grid: np.ndarray, t: np.ndarray) -> np.ndarray:
    """
    This function finds the smallest rectangle that covers all teal pixels in the input grid.

    Args:
    - input_grid: a numpy array representing the input grid
    - t: a numpy array representing the teal pixels in the input grid

    Returns:
    - s: a numpy array representing the smallest rectangle that covers all teal pixels in the input grid
    """
    (rows, cols) = np.where(t == 1)
    (min_row, max_row) = (np.min(rows), np.max(rows))
    (min_col, max_col) = (np.min(cols), np.max(cols))
    s = input_grid[min_row:max_row + 1, min_col:max_col + 1]
    return s

def find_teal_pixels(input_grid: np.ndarray) -> np.ndarray:
    teal_pixels = np.where(input_grid == teal, 1, 0)
    return teal_pixels

def find_non_black_teal_pixels(input_grid: np.ndarray) -> np.ndarray:
    non_black_teal_pixels = np.where((input_grid != black) & (input_grid != teal), 1, 0)
    return non_black_teal_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    p = find_non_black_teal_pixels(input_grid)
    t = find_teal_pixels(input_grid)
    s = find_smallest_area(input_grid, t)
    l = find_smallest_covering_area(input_grid, p)
    o = copy_square_to_middle(s, l)
    out = replace_teal_pixels(o)
    return out