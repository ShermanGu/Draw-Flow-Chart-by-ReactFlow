import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def dfs(i: int, j: int, grid: np.ndarray, visited: np.ndarray, pattern: List[Tuple[int, int]]):
    """
    A helper function for find_green_patterns that performs a depth-first search to find all connected pixels of the same color.
    """
    visited[i][j] = True
    pattern.append((i, j))
    for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1] and (grid[x][y] == green) and (not visited[x][y]):
            dfs(x, y, grid, visited, pattern)

def color_patterns(p: List[List[Tuple[int, int]]], record: Dict[int, int], grid: np.ndarray) -> np.ndarray:
    """
    Given a list of patterns, a dictionary of their 90 degree sides count, and a 2D numpy array representing a grid of pixels,
    this function colors the patterns based on their 90 degree sides count and returns the updated grid.
    A pattern with 1 90 degree side is colored blue, a pattern with 2 90 degree sides is colored pink, and a pattern with 3 90 degree sides is colored red.
    """
    for (i, pattern) in enumerate(p):
        if record[i] == 1:
            color = blue
        elif record[i] == 2:
            color = pink
        elif record[i] == 3:
            color = red
        else:
            color = green
        for (x, y) in pattern:
            grid[x][y] = color
    return grid

def count_90_degree_sides(patterns: List[List[Tuple[int, int]]], grid: np.ndarray) -> Dict[int, int]:
    """
    For every pattern in patterns, count how many 90 degree sides in it by traversing pixels in the pattern,
    a 90 degree sides means if 2 adjacent neighbors of a pixels are both in the pattern but the pixel along the diagonal direction and adjacent to the 2 neighbors is not in the pattern,
    for example, the left and top is in pattern and the left top pixel along the diagonal direction is not.
    Returns a dictionary where the keys are the indices of the patterns and the values are the number of 90 degree sides in the pattern.
    """
    sides_count = {}
    for (i, pattern) in enumerate(patterns):
        count = 0
        for (x, y) in pattern:
            if x > 0 and y > 0 and (x < grid.shape[0] - 1) and (y < grid.shape[1] - 1):
                if (x - 1, y) in pattern and (x, y - 1) in pattern and ((x - 1, y - 1) not in pattern):
                    count += 1
                if (x - 1, y) in pattern and (x, y + 1) in pattern and ((x - 1, y + 1) not in pattern):
                    count += 1
                if (x + 1, y) in pattern and (x, y - 1) in pattern and ((x + 1, y - 1) not in pattern):
                    count += 1
                if (x + 1, y) in pattern and (x, y + 1) in pattern and ((x + 1, y + 1) not in pattern):
                    count += 1
        sides_count[i] = count
    return sides_count

def find_green_patterns(grid: np.ndarray) -> List[List[Tuple[int, int]]]:
    """
    Given a 2D numpy array representing a grid of pixels, this function returns a list of all green patterns.
    A pattern is defined as a set of connected pixels of the same color.
    Each pattern is represented as a list of tuples, where each tuple contains the row and column indices of a pixel in the pattern.
    """
    green_patterns = []
    visited = np.zeros_like(grid, dtype=bool)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i][j] == green and (not visited[i][j]):
                pattern = []
                dfs(i, j, grid, visited, pattern)
                green_patterns.append(pattern)
    return green_patterns

def main(input_grid: np.ndarray) -> np.ndarray:
    p = find_green_patterns(input_grid)
    record = count_90_degree_sides(p, input_grid)
    out = color_patterns(p, record, input_grid)
    return out