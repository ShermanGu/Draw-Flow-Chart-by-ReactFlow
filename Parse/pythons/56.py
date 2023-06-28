import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_smallest_rect(non_black_pixels: List[Tuple[int, int]], input_grid: np.ndarray) -> np.ndarray:
    """
    Returns the smallest rectangle which contains all of the non-black pixels in the input grid.
    
    Args:
    non_black_pixels: A list of tuples representing the non-black pixels in the input grid.
    Each tuple contains the row and column indices of a non-black pixel.
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the smallest rectangle which contains all of the non-black pixels in the input grid.
    """
    min_row = min([pixel[0] for pixel in non_black_pixels])
    max_row = max([pixel[0] for pixel in non_black_pixels])
    min_col = min([pixel[1] for pixel in non_black_pixels])
    max_col = max([pixel[1] for pixel in non_black_pixels])
    smallest_rect = input_grid[min_row:max_row + 1, min_col:max_col + 1]
    return smallest_rect

def get_non_black_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Returns a list of non-black pixels in the input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples representing the non-black pixels in the input grid.
    Each tuple contains the row and column indices of a non-black pixel.
    """
    non_black_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                non_black_pixels.append((i, j))
    return non_black_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    non_black_pixels = get_non_black_pixels(input_grid)
    smallest_rect = find_smallest_rect(non_black_pixels, input_grid)
    output_grid = np.concatenate([smallest_rect, smallest_rect], axis=1)
    return output_grid