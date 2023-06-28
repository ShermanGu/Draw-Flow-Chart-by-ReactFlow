import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_2x2_grids(input_grid: np.ndarray, locs: List[Tuple[int, int]], n: List[int]) -> np.ndarray:
    """
      This function takes in a numpy array as input_grid, a list of tuples containing the row and column indices
      of all 2x2 pixels that are not black (represented by the integer value 0), and a list of integers, where each
      integer represents the number of unique non-black colors in the corresponding 2x2 pixel. It returns a numpy array
      where for each 2x2 pixel, the n * 2 pixels just under it are changed to green.

      Args:
      - input_grid: A numpy array of shape (n, m) representing the input grid
      - locs: A list of tuples containing the row and column indices of all 2x2 pixels that are not black
      - n: A list of integers, where each integer represents the number of unique non-black colors in the corresponding 2x2 pixel

      Returns:
      - A numpy array where for each 2x2 pixel, the n * 2 pixels just under it are changed to green
      """
    out_grid = input_grid.copy()
    for (i, loc) in enumerate(locs):
        (x, y) = loc
        for j in range(n[i]):
            for k in range(2):
                out_grid[x + j + 2, y + k] = green
    return out_grid

def get_num_colors_2x2(input_grid: np.ndarray, locs: List[Tuple[int, int]]) -> List[int]:
    num_colors = []
    for loc in locs:
        (i, j) = loc
        colors = set([input_grid[i][j], input_grid[i][j + 1], input_grid[i + 1][j], input_grid[i + 1][j + 1]])
        num_colors.append(len(colors))
    return num_colors

def find_non_black_2x2_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    locs = []
    for i in range(input_grid.shape[0] - 1):
        for j in range(input_grid.shape[1] - 1):
            if input_grid[i][j] != black and input_grid[i][j + 1] != black and (input_grid[i + 1][j] != black) and (input_grid[i + 1][j + 1] != black):
                locs.append((i, j))
    return locs

def main(input_grid: np.ndarray) -> np.ndarray:
    locs = find_non_black_2x2_pixels(input_grid)
    n = get_num_colors_2x2(input_grid, locs)
    out_grid = color_2x2_grids(input_grid, locs, n)
    return out_grid