import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_rectangle(grid: np.ndarray, rectangle: Tuple[int, int, int, int], color: int) -> np.ndarray:
    (i, j, k, l) = rectangle
    grid[i:k + 1, j:l + 1] = color
    return grid

def find_black_rectangles(grid: np.ndarray) -> List[Tuple[int, int, int, int]]:
    black_rectangles = []
    (rows, cols) = grid.shape
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == black:
                k = i
                while k < rows and grid[k][j] == black:
                    k += 1
                l = j
                while l < cols and grid[i][l] == black:
                    l += 1
                black_rectangles.append((i, j, k - 1, l - 1))
                grid[i:k, j:l] = teal
    return black_rectangles

def copy_grid(input_grid: np.ndarray) -> np.ndarray:
    return np.copy(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output = copy_grid(input_grid)
    BLACK_block_list = find_black_rectangles(input_grid)
    output = color_rectangle(output, BLACK_block_list[1], red)
    output = color_rectangle(output, BLACK_block_list[3], yellow)
    output = color_rectangle(output, BLACK_block_list[4], pink)
    output = color_rectangle(output, BLACK_block_list[5], green)
    output = color_rectangle(output, BLACK_block_list[7], blue)
    return output