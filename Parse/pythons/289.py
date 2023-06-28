import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def exchange_colors(grid: np.ndarray, color1: int, color2: int) -> np.ndarray:
    """
    Given a grid and two colors, exchanges the positions of the two colors in the grid.
    
    Args:
    grid: A numpy array representing the grid.
    color1: An integer representing the first color.
    color2: An integer representing the second color.
    
    Returns:
    A numpy array representing the grid with the two colors exchanged.
    """
    output_grid = np.copy(grid)
    output_grid[grid == color1] = color2
    output_grid[grid == color2] = color1
    return output_grid

def get_colors(grid: np.ndarray) -> Tuple[int, int]:
    colors = np.unique(grid)
    return (colors[0], colors[1])

def crop_grid(input_grid: np.ndarray) -> np.ndarray:
    non_black_indices = np.where(input_grid != black)
    (min_x, max_x) = (np.min(non_black_indices[0]), np.max(non_black_indices[0]))
    (min_y, max_y) = (np.min(non_black_indices[1]), np.max(non_black_indices[1]))
    return input_grid[min_x:max_x + 1, min_y:max_y + 1]

def main(input_grid: np.ndarray) -> np.ndarray:
    grid1 = crop_grid(input_grid)
    (color1, color2) = get_colors(grid1)
    output_grid = exchange_colors(grid1, color1, color2)
    return output_grid