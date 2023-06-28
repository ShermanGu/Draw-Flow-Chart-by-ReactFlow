import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_pixels_between_same_color_pixels(grid: np.ndarray, pixels: List[Tuple[int, int]], color: int) -> np.ndarray:
    """
    Given a grid, a list of pixels and a color, this function turns all black pixels between any two pixels in the list
    that are in the same row or column into the given color.
    
    Args:
    1. grid: np.ndarray - A numpy array representing the input grid.
    2. pixels: List[Tuple[int, int]] - A list of tuples representing the indices of pixels.
    3. color: int - An integer representing the color to turn the pixels into.
    
    Returns:
    A numpy array representing the updated grid.
    """
    for i in range(len(pixels)):
        for j in range(i + 1, len(pixels)):
            if pixels[i][0] == pixels[j][0]:
                for k in range(min(pixels[i][1], pixels[j][1]) + 1, max(pixels[i][1], pixels[j][1])):
                    if grid[pixels[i][0]][k] == black:
                        grid[pixels[i][0]][k] = color
            elif pixels[i][1] == pixels[j][1]:
                for k in range(min(pixels[i][0], pixels[j][0]) + 1, max(pixels[i][0], pixels[j][0])):
                    if grid[k][pixels[i][1]] == black:
                        grid[k][pixels[i][1]] = color
    return grid

def find_pixels_in_color(grid: np.ndarray, color: int) -> List[Tuple[int, int]]:
    """
    Given a grid and a color, this function returns a list of tuples representing the indices of all pixels in the grid
    that have the given color.
    
    Args:
    1. grid: np.ndarray - A numpy array representing the input grid.
    2. color: int - An integer representing the color to search for.
    
    Returns:
    A list of tuples representing the indices of all pixels in the grid that have the given color.
    """
    pixels = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == color:
                pixels.append((i, j))
    return pixels

def color_between_same_color_pixels(grid: np.ndarray, line_color: int) -> np.ndarray:
    for color in range(10):
        if color != black and color != line_color:
            p = find_pixels_in_color(grid, color)
            grid = color_pixels_between_same_color_pixels(grid, p, color)
    return grid

def find_color(grid: np.ndarray) -> int:
    """
    Given a grid, this function finds the color of the line in the grid.
    
    Args:
    1. grid: np.ndarray - A numpy array representing the input grid.
    
    Returns:
    An integer representing the color of the line.
    """
    for color in range(10):
        if color != black:
            for i in range(grid.shape[0]):
                row = grid[i, :]
                col = grid[:, i]
                if np.all(row == color) or np.all(col == color):
                    return color
    return black

def main(input_grid: np.ndarray) -> np.ndarray:
    line = find_color(input_grid)
    out = color_between_same_color_pixels(input_grid, line)
    return out