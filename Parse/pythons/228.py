import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def turn_other_colors_to_grey(color: int, input_grid: np.ndarray) -> np.ndarray:
    """
    Given an input grid and a color, this function turns all pixels in colors other than the given color to grey.

    Args:
    color: An integer representing the color to keep.
    input_grid: A numpy array representing the input grid.

    Returns:
    A numpy array representing the output grid with all pixels in colors other than the given color turned to grey.
    """
    output_grid = np.copy(input_grid)
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i][j] != color and output_grid[i][j] != black:
                output_grid[i][j] = grey
    return output_grid

def find_max_color(color_counts: Dict[int, int]) -> int:
    """
    Given a dictionary of color counts, this function returns the color with the maximum number of pixels.

    Args:
    color_counts: A dictionary where the keys are the colors of non-black patterns and the values are the number of pixels in the color.

    Returns:
    The color with the maximum number of pixels.
    """
    max_color = None
    max_count = 0
    for (color, count) in color_counts.items():
        if count > max_count:
            max_color = color
            max_count = count
    return max_color

def record_colors(input_grid: np.ndarray) -> Dict[int, int]:
    """
    Given an input grid, this function records the colors of all non-black patterns on the grid and the number of pixels
    in the color.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A dictionary where the keys are the colors of non-black patterns and the values are the number of pixels in the color.
    """
    color_counts = {}
    for row in input_grid:
        for pixel in row:
            if pixel != black:
                if pixel in color_counts:
                    color_counts[pixel] += 1
                else:
                    color_counts[pixel] = 1
    return color_counts

def main(input_grid: np.ndarray) -> np.ndarray:
    Record = record_colors(input_grid)
    p = find_max_color(Record)
    out = turn_other_colors_to_grey(p, input_grid)
    return out