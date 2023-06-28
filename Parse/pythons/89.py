import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_square_to_pink(grid: np.ndarray, square: Tuple[int, int, int]) -> np.ndarray:
    """
    Given a grid and a tuple containing the row index, column index, and size of a square,
    color the square area in the grid pink instead of black.
    Returns the updated grid.
    """
    (row, col, size) = square
    for i in range(row, row + size):
        for j in range(col, col + size):
            grid[i][j] = pink
    return grid

def find_biggest_black_square(grid: np.ndarray) -> Tuple[int, int, int]:
    """
    Given a grid, find the biggest square that can be created with only black boxes.
    Returns a tuple containing the row index, column index, and size of the biggest square.
    """
    (rows, cols) = grid.shape
    max_size = 0
    (max_row, max_col) = (0, 0)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == black:
                size = 1
                extend = True
                while extend and i + size < rows and (j + size < cols):
                    for k in range(j, j + size + 1):
                        if grid[i + size][k] != black:
                            extend = False
                            break
                    for k in range(i, i + size + 1):
                        if grid[k][j + size] != black:
                            extend = False
                            break
                    if extend:
                        size += 1
                if size > max_size:
                    max_size = size
                    (max_row, max_col) = (i, j)
    return (max_row, max_col, max_size)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    find in the input the biggest square or rectangle that can be created with only black boxes. Then make that box area in the output pink instead of black.
    """
    output_grid = np.copy(input_grid)
    biggest_black_square = find_biggest_black_square(output_grid)
    output_grid = color_square_to_pink(output_grid, biggest_black_square)
    return output_grid