import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def draw_pixel(grid: np.ndarray, coordinate):
    (x, y) = coordinate
    grid[x - 1][y - 1] = blue
    grid[x - 1][y + 2] = red
    grid[x + 2][y - 1] = green
    grid[x + 2][y + 2] = yellow

def find_grey_squares(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    coordinates = []
    for i in range(input_grid.shape[0] - 1):
        for j in range(input_grid.shape[1] - 1):
            if input_grid[i][j] == grey and input_grid[i][j + 1] == grey and (input_grid[i + 1][j] == grey) and (input_grid[i + 1][j + 1] == grey):
                coordinates.append((i, j))
    return coordinates

def main(input_grid: np.ndarray) -> np.ndarray:
    coordinates = find_grey_squares(input_grid)
    for coordinate in coordinates:
        draw_pixel(input_grid, coordinate)
    return input_grid