import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def remove_inner_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    Find all non-black pixels not in the edge line or at the corner. If at least 3 of 4 neighbors of the pixel are black, turn it to black. Return the grid.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the modified grid with inner pixels removed
    """
    (height, width) = input_grid.shape
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if input_grid[i][j] != black:
                black_neighbors = 0
                if input_grid[i - 1][j] == black:
                    black_neighbors += 1
                if input_grid[i + 1][j] == black:
                    black_neighbors += 1
                if input_grid[i][j - 1] == black:
                    black_neighbors += 1
                if input_grid[i][j + 1] == black:
                    black_neighbors += 1
                if black_neighbors >= 3:
                    input_grid[i][j] = black
    return input_grid

def remove_edge_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    Find all non-black pixels in the edge line. If at least 2 of 4 neighbors of the pixel are black, turn it to black. Return the grid.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the modified grid with edge pixels removed
    """
    (height, width) = input_grid.shape
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or (j == width - 1):
                if input_grid[i][j] != black:
                    black_neighbors = 0
                    if i > 0 and input_grid[i - 1][j] == black:
                        black_neighbors += 1
                    if i < height - 1 and input_grid[i + 1][j] == black:
                        black_neighbors += 1
                    if j > 0 and input_grid[i][j - 1] == black:
                        black_neighbors += 1
                    if j < width - 1 and input_grid[i][j + 1] == black:
                        black_neighbors += 1
                    if black_neighbors >= 2:
                        input_grid[i][j] = black
    return input_grid

def remove_corner_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    Find all non-black pixels at the corner. If any neighbor of the pixel is black, turn it to black. Return the grid.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the modified grid with corner pixels removed
    """
    (height, width) = input_grid.shape
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1:
                if j == 0 or j == width - 1:
                    if input_grid[i][j] != black:
                        if i == 0 and j == 0:
                            if input_grid[i + 1][j] == black or input_grid[i][j + 1] == black:
                                input_grid[i][j] = black
                        elif i == 0 and j == width - 1:
                            if input_grid[i + 1][j] == black or input_grid[i][j - 1] == black:
                                input_grid[i][j] = black
                        elif i == height - 1 and j == 0:
                            if input_grid[i - 1][j] == black or input_grid[i][j + 1] == black:
                                input_grid[i][j] = black
                        elif i == height - 1 and j == width - 1:
                            if input_grid[i - 1][j] == black or input_grid[i][j - 1] == black:
                                input_grid[i][j] = black
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    out1 = remove_corner_pixels(input_grid)
    out2 = remove_edge_pixels(out1)
    out = remove_inner_pixels(out2)
    return out