import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_black_to_red(grid: np.ndarray, point: Tuple[int, int]) -> np.ndarray:
    (x, y) = point
    if grid[x][y] == black:
        grid[x][y] = red
    return grid

def generate_blue_coordinates(grid: np.ndarray) -> List[Tuple[int, int]]:
    (rows, cols) = grid.shape
    blue_coordinates = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == blue:
                blue_coordinates.append((i, j))
    return blue_coordinates

def find_first_and_last_blue_points(grid: np.ndarray) -> Tuple[int, int, int, int]:
    (rows, cols) = grid.shape
    (x1, y1, x2, y2) = (-1, -1, -1, -1)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == blue:
                if x1 == -1:
                    (x1, y1) = (i, j)
                (x2, y2) = (i, j)
    return (x1, y1, x2, y2)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.copy(input_grid)
    (x1, y1, x2, y2) = find_first_and_last_blue_points(output_grid)
    listb = generate_blue_coordinates(output_grid)
    for (x, y) in listb:
        (x3, y3) = (x1 + x2 - x, y1 + y2 - y)
        output_grid = turn_black_to_red(output_grid, (x3, y3))
    return output_grid