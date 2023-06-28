import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_grey_rect_size(input_grid: np.ndarray) -> Tuple[int, int]:
    grey_rows = []
    for (i, row) in enumerate(input_grid):
        if grey in row:
            grey_rows.append(i)
    top_grey_row = min(grey_rows)
    bottom_grey_row = max(grey_rows)
    left_grey_col = np.where(input_grid[top_grey_row] == grey)[0][0]
    right_grey_col = np.where(input_grid[bottom_grey_row] == grey)[0][-1]
    height = bottom_grey_row - top_grey_row + 1
    width = right_grey_col - left_grey_col + 1
    return (height, width)

def get_row_colors(input_grid: np.ndarray) -> List[int]:
    colors = []
    for row in input_grid:
        for color in row:
            if color not in [black, grey] and color not in colors:
                colors.append(color)
    return colors

def main(input_grid: np.ndarray) -> np.ndarray:
    colors = get_row_colors(input_grid)
    (height, width) = get_grey_rect_size(input_grid)
    output_grid = np.zeros([height, width], dtype=np.int32)
    output_grid = output_grid.copy()
    for i in range(output_grid.shape[0]):
        output_grid[i, :] = colors[i]
    return output_grid