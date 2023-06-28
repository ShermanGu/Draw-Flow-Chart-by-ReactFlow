import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def map_3x3_to_9x9(input_square: np.ndarray) -> np.ndarray:
    """
    Maps the input 3x3 square to a 9x9 grid, where if a pixel in the input square is black, then the corresponding
    pixels in the output grid are also black. Otherwise, the input square is copied to the corresponding location in
    the output grid.

    Args:
    input_square: A numpy array of shape (3, 3) representing the input square.

    Returns:
    A numpy array of shape (9, 9) representing the output grid.
    """
    output_grid = np.zeros((9, 9))
    for i in range(3):
        for j in range(3):
            if input_square[i][j] != black:
                output_grid[3 * i:3 * i + 3, 3 * j:3 * j + 3] = input_square
    return output_grid

def has_color_pixel(square: np.ndarray) -> bool:
    """
    Checks if the given square has at least one pixel of color other than black.

    Args:
    square: A numpy array of shape (3, 3) representing the input square.

    Returns:
    A boolean value indicating whether the square has at least one pixel of color other than black.
    """
    return np.any(square != black)

def split_grid(input_grid: np.ndarray) -> List[np.ndarray]:
    """
    Splits the input grid into 9 small squares of size 3x3.

    Args:
    input_grid: A numpy array of shape (9, 9) representing the input grid.

    Returns:
    A list of 9 numpy arrays, each of shape (3, 3), representing the small squares.
    """
    squares = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = input_grid[i:i + 3, j:j + 3]
            squares.append(square)
    return squares

def main(input_grid: np.ndarray):
    squares = split_grid(input_grid)
    colorful_square = None
    for square in squares:
        if has_color_pixel(square):
            colorful_square = square
    output_grid = map_3x3_to_9x9(colorful_square)
    return output_grid