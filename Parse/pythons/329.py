import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def dfs(grid: np.ndarray, visited: np.ndarray, i: int, j: int) -> np.ndarray:
    """
    This function performs depth-first search to find all the grey pixels in a grey shape.
    """
    if i < 0 or i >= grid.shape[0] or j < 0 or (j >= grid.shape[1]) or (visited[i][j] == 1) or (grid[i][j] != grey):
        return np.zeros_like(grid)
    visited[i][j] = 1
    shape = np.zeros_like(grid)
    shape[i][j] = 1
    shape += dfs(grid, visited, i + 1, j)
    shape += dfs(grid, visited, i - 1, j)
    shape += dfs(grid, visited, i, j + 1)
    shape += dfs(grid, visited, i, j - 1)
    return shape

def color_grey_shape(grid: np.ndarray, grey_shape: np.ndarray, color: int) -> np.ndarray:
    """
    This function takes a grid, a grey shape, and a color, and colors the pixels of the grid to give color where its value equals 1 in grey shape.
    """
    grid[grey_shape == 1] = color
    return grid

def count_pixels(gs: np.ndarray) -> int:
    """                                                                                                                                                                 
    This function takes a grey shape and returns the number of grey pixels in it.                                                                                       
    """
    return np.sum(gs)

def find_grey_shapes(grid: np.ndarray) -> List[np.ndarray]:
    """
    This function takes an input grid and returns a list of the indices of the grey shapes, each grey shape contains some grey pixels.
    """
    grey_shapes = []
    visited = np.zeros_like(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == grey and visited[i][j] == 0:
                grey_shape = dfs(grid, visited, i, j)
                grey_shapes.append(grey_shape)
    return grey_shapes

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see a black grid, it has some grey shapes.
    the output grid is the same size as the input grid.
    To make the output, you should color the grey shapes to red that has six grey pixels, and color the grey shapes to blue that do not have six grep pixels.
    """
    output_grid = input_grid.copy()
    grey_shapes = find_grey_shapes(input_grid)
    for gs in grey_shapes:
        if count_pixels(gs) == 6:
            output_grid = color_grey_shape(output_grid, gs, red)
        else:
            output_grid = color_grey_shape(output_grid, gs, blue)
    return output_grid