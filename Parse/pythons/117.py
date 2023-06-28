import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_color_list(input, positions):
    (i, j) = positions
    return [input[i][j], input[i - 2][j], input[i + 2][j], input[i][j - 2], input[i][j + 2]]

def change_cross_to_teal(input_grid: List[List[int]], centers: List[Tuple[int, int]]) -> List[List[int]]:
    """
    Change the non-red positions of the cross with radius 3 to teal for each position in the input centers.

    Args:
    input_grid: A 2D list of integers representing the initial color grid.
    centers: A list of tuples representing the positions of the red centers.

    Returns:
    A 2D list of integers representing the updated color grid after changing the non-red positions of the cross with radius 3 to teal for each position in the input centers.
    """
    for center in centers:
        (i, j) = center
        for k in range(1, 3):
            if input_grid[i - k][j] != red:
                input_grid[i - k][j] = teal
            if input_grid[i + k][j] != red:
                input_grid[i + k][j] = teal
            if input_grid[i][j - k] != red:
                input_grid[i][j - k] = teal
            if input_grid[i][j + k] != red:
                input_grid[i][j + k] = teal
        if input_grid[i][j] != red:
            input_grid[i][j] = teal
    return input_grid

def find_red_centers(input_grid):
    centers = []
    for i in range(2, len(input_grid) - 2):
        for j in range(2, len(input_grid[0]) - 2):
            color_list2 = get_color_list(input_grid, (i, j))
            if color_list2.count(red) >= 3:
                centers.append((i, j))
    return centers

def main(input_grid):
    centers = find_red_centers(input_grid)
    output = change_cross_to_teal(input_grid, centers)
    return output