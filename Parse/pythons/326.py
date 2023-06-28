import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def cover_3x3_region(output_grid: np.ndarray, input_grid: np.ndarray) -> np.ndarray:
    """
    This function takes an output grid and an input grid and covers the 3x3 region on the output grid with the input grid
    starting at the top left corner (0,0) and ending at the bottom right corner (2,2).
    
    Args:
    output_grid: A numpy array representing the output grid.
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array representing the output grid with the 3x3 region covered with the input grid.
    """
    output_grid[:3, :3] = input_grid[:3, :3]
    return output_grid

def color_bottom_right_pixels(input_grid: np.ndarray, color_pixels: List[Tuple[int, int, int]]) -> np.ndarray:
    """
    This function takes an input grid and a list of tuples containing the color and coordinates of non-black pixels.
    It colors all pixels in the bottom-right 45-degree direction from the current pixel with the same color.
    
    Args:
    input_grid: A numpy array representing the input grid.
    color_pixels: A list of tuples containing the color and coordinates of non-black pixels.
    
    Returns:
    A numpy array representing the output grid with colored pixels.
    """
    for (color, i, j) in color_pixels:
        k = 1
        while i + k < input_grid.shape[0] and j + k < input_grid.shape[1]:
            if input_grid[i + k][j + k] == black:
                input_grid[i + k][j + k] = color
            k += 1
    return input_grid

def create_black_image() -> np.ndarray:
    """
    This function creates a completely black image matrix with dimensions of 6x6.
    
    Returns:
    A numpy array representing the black image matrix.
    """
    return np.zeros((6, 6), dtype=int)

def get_color_pixels(input_grid: np.ndarray) -> List[Tuple[int, int, int]]:
    """
    This function takes an input grid and returns a list of tuples containing the color and coordinates of non-black pixels.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples containing the color and coordinates of non-black pixels.
    """
    color_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] != black:
                color_pixels.append((input_grid[i][j], i, j))
    return color_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    color_pixels = get_color_pixels(input_grid)
    output_grid = create_black_image()
    output_grid = color_bottom_right_pixels(output_grid, color_pixels)
    output_grid = cover_3x3_region(output_grid, input_grid)
    return output_grid