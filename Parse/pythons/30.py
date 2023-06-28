import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_smallest_rect(non_black_pixels: Tuple[np.ndarray, np.ndarray], input_grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    Given a numpy array _hole13 and a tuple of numpy arrays _hole15 containing the indices of non-black pixels,
    this function returns the smallest rectangle that contains all the non-black pixels in the input grid.
    
    Args:
    - non_black_pixels (Tuple[np.ndarray, np.ndarray]): A tuple of numpy arrays containing the row and column indices of non-black pixels.
    - input_grid (np.ndarray): A numpy array representing the input grid.
    
    Returns:
    - A tuple of integers (top, left, bottom, right) representing the smallest rectangle that contains all the non-black pixels in the input grid.
    """
    top = np.min(non_black_pixels[0])
    left = np.min(non_black_pixels[1])
    bottom = np.max(non_black_pixels[0])
    right = np.max(non_black_pixels[1])
    return (top, left, bottom + 1, right + 1)

def main(input_grid: np.ndarray) -> np.ndarray:
    non_black_pixels = np.where(input_grid != black)
    smallest_rect = find_smallest_rect(non_black_pixels, input_grid)
    output_grid = input_grid[smallest_rect[0]:smallest_rect[2], smallest_rect[1]:smallest_rect[3]]
    return output_grid