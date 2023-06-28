import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_same_color_pixels_black(grid, coordinate, colors):
    color = colors.pop()
    col = grid[:, coordinate[1]]
    col[col == color] = black

def find_surrounding_colors(input_grid: np.ndarray, coordinate: Tuple[int, int]) -> List[int]:
    (i, j) = coordinate
    surrounding_colors = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x >= 0 and y >= 0 and (x < input_grid.shape[0]) and (y < input_grid.shape[1]) and ((x, y) != (i, j)):
                surrounding_colors.append(input_grid[x][y])
    return surrounding_colors

def find_all_black_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    black_pixels_coordinates = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == black:
                black_pixels_coordinates.append((i, j))
    return black_pixels_coordinates

def rotate_if(grid: np.ndarray, num_non_black: int) -> np.ndarray:
    """
    If the num_non_black is not 1, rotate the grid 90 degrees.
    
    Args:
    - grid (np.ndarray): The input grid to be rotated.
    - num_non_black (int): The number of non-black colors in the first row of the grid.
    
    Returns:
    - np.ndarray: The rotated grid if num_non_black is not 1, otherwise the original grid.
    """
    if num_non_black != 1:
        return np.rot90(grid)
    else:
        return grid

def find_num_non_black_in_first_row(input_grid: np.ndarray) -> int:
    return len(set(input_grid[0])) - 1

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = input_grid.copy()
    num_non_black = find_num_non_black_in_first_row(input_grid)
    output_grid = rotate_if(output_grid, num_non_black)
    black_pixels_coordinates = find_all_black_pixels(input_grid)
    for coordinate in black_pixels_coordinates:
        surrounding_colors = find_surrounding_colors(input_grid, coordinate)
        paint_same_color_pixels_black(output_grid, coordinate, surrounding_colors)
    output_grid = rotate_if(output_grid, num_non_black)
    return output_grid