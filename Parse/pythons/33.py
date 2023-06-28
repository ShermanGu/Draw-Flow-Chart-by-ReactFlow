import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def drawline(grid: np.ndarray, start: Tuple[int, int], direction: Tuple[int, int], color: int) -> np.ndarray:
    """
    Extend from the starting point in the specified direction until the grid boundary using the specific color.

    Parameters:
    grid (np.ndarray): The input grid as a numpy array.
    start (Tuple[int, int]): The starting point of the line as a tuple of integers representing x and y coordinates.
    direction (Tuple[int, int]): The direction of the line as a tuple of integers representing the change in x and y coordinates for each step.
    color (int): The color to use for drawing the line.

    Returns:
    np.ndarray: The updated grid as a numpy array with the drawn line.
    """
    (x, y) = start
    (dx, dy) = direction
    while 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:
        grid[x, y] = color
        x += dx
        y += dy
    return grid

def find_colors(input_grid: np.ndarray) -> List[int]:
    colors = set()
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] != red and input_grid[i, j] != black:
                colors.add(input_grid[i, j])
    return list(colors)

def find_red_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    red_coordinates = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] == red:
                red_coordinates.append((i, j))
    return red_coordinates

def main(input_grid: np.ndarray) -> np.ndarray:
    grid = input_grid.copy()
    red_coordinates = find_red_pixels(input_grid)
    color = find_colors(input_grid)[0]
    for (x, y) in red_coordinates:
        if input_grid[x + 1, y] != black and input_grid[x, y + 1] != black:
            grid = drawline(grid, (x, y), (-1, -1), color)
            grid = drawline(grid, (x + 1, y), (-1, -1), color)
            grid = drawline(grid, (x, y + 1), (-1, -1), color)
        elif input_grid[x + 1, y] != black and input_grid[x, y - 1] != black:
            grid = drawline(grid, (x, y), (-1, 1), color)
            grid = drawline(grid, (x + 1, y), (-1, 1), color)
            grid = drawline(grid, (x, y - 1), (-1, 1), color)
        elif input_grid[x - 1, y] != black and input_grid[x, y + 1] != black:
            grid = drawline(grid, (x, y), (1, -1), color)
            grid = drawline(grid, (x - 1, y), (1, -1), color)
            grid = drawline(grid, (x, y + 1), (1, -1), color)
        elif input_grid[x - 1, y] != black and input_grid[x, y - 1] != black:
            grid = drawline(grid, (x, y), (1, 1), color)
            grid = drawline(grid, (x - 1, y), (1, 1), color)
            grid = drawline(grid, (x, y - 1), (1, 1), color)
    return grid