import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_color_at_locations(locations: List[Tuple[int, int]], color: int, grid: np.ndarray) -> np.ndarray:
    """
    Changes the color of the cells at the given locations in the grid to the given color.
    Returns the updated grid.
    """
    for (row, col) in locations:
        grid[row][col] = color
    return grid

def get_middle_locations(locations: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Returns a list of tuples representing the middle locations of the given locations.
    Each tuple contains the row and column indices of the middle cell of a group of cells
    that are either in the same row or the same column.
    """
    middle_locations = []
    for i in range(len(locations)):
        (row, col) = locations[i]
        same_row = [loc for loc in locations if loc[0] == row]
        same_col = [loc for loc in locations if loc[1] == col]
        if len(same_row) > 1:
            same_row.sort(key=lambda loc: loc[1])
            middle_col = (same_row[0][1] + same_row[-1][1]) // 2
            middle_locations.append((row, middle_col))
        elif len(same_col) > 1:
            same_col.sort(key=lambda loc: loc[0])
            middle_row = (same_col[0][0] + same_col[-1][0]) // 2
            middle_locations.append((middle_row, col))
    return middle_locations

def get_color_locations(color: int, grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Returns a list of tuples representing the locations of the given color in the grid.
    Each tuple contains the row and column indices of a cell with the given color.
    """
    return list(zip(*np.where(grid == color)))

def main(input_grid: np.ndarray) -> np.ndarray:
    out = input_grid
    for color in range(2, 10):
        loc1 = get_color_locations(color, out)
        if loc1:
            loc2 = get_middle_locations(loc1)
            out = change_color_at_locations(loc2, color, out)
    return out