import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_adjacent_points(i: int, j: int, rows: int, cols: int) -> List[Tuple[int, int]]:
    """
    This function takes in the row and column indices of a point in a grid and returns a list of tuples representing the row and column indices of its adjacent points.
    
    Args:
    - i: An integer representing the row index of the point.
    - j: An integer representing the column index of the point.
    - rows: An integer representing the number of rows in the grid.
    - cols: An integer representing the number of columns in the grid.
    
    Returns:
    - adjacent_points: A list of tuples representing the row and column indices of the adjacent points.
    """
    adjacent_points = []
    if i > 0:
        adjacent_points.append((i - 1, j))
    if i < rows - 1:
        adjacent_points.append((i + 1, j))
    if j > 0:
        adjacent_points.append((i, j - 1))
    if j < cols - 1:
        adjacent_points.append((i, j + 1))
    return adjacent_points

def process_grid(input_grid: np.ndarray) -> np.ndarray:
    """
    This function takes in a numpy array representing a grid of colors and processes it according to the following rules:
    - For every red point in the grid, if it has green adjacent points, turn that green adjacent point to teal and turn the red point to black.
    - Return the processed grid.
    
    Args:
    - input_grid: A numpy array representing a grid of colors. Each element in the array is an integer representing a color.
    
    Returns:
    - output_grid: A numpy array representing the processed grid of colors.
    """
    output_grid = np.copy(input_grid)
    (rows, cols) = input_grid.shape
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == red:
                adjacent_points = get_adjacent_points(i, j, rows, cols)
                for point in adjacent_points:
                    if input_grid[point[0]][point[1]] == green:
                        output_grid[point[0]][point[1]] = teal
                        output_grid[i][j] = black
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = process_grid(input_grid)
    return output_grid