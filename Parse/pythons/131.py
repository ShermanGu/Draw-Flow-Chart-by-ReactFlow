import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def generate_rectangles(grid: np.ndarray, color: int) -> np.ndarray:
    points = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == color:
                points.append((i, j))
                if len(points) == 2:
                    break
        if len(points) == 2:
            break
    (x1, y1) = points[0]
    (x2, y2) = points[1]
    x_min = min(x1, x2)
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    y_max = max(y1, y2)
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            grid[i][j] = color
    return grid

def get_non_black_colors(grid: np.ndarray) -> List[int]:
    colors = set()
    for row in grid:
        for cell in row:
            if cell != black:
                colors.add(cell)
    return list(colors)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.copy(input_grid)
    listc = get_non_black_colors(output_grid)
    for color in listc:
        output_grid = generate_rectangles(output_grid, color)
    return output_grid