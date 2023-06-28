import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def colorize_grid(output_grid: np.ndarray, count_of_colors: List[Tuple[int, int]], number_of_color_types: int) -> np.ndarray:
    """
    Colors each column of the output grid with the corresponding color type according to the count of colors.

    Args:
    output_grid: A numpy array representing the empty output grid.
    count_of_colors: A list of tuples where the first element is the color type and the second element is the number of pixels of that color type in the input grid, sorted from most to least.
    number_of_color_types: An integer representing the number of unique color types in the input grid.

    Returns:
    A numpy array representing the output grid with colored columns.
    """
    for i in range(number_of_color_types):
        color_type = count_of_colors[i][0]
        count = count_of_colors[i][1]
        for j in range(count):
            output_grid[j][i] = color_type
    return output_grid

def make_empty_grid(count_of_colors: List[Tuple[int, int]], number_of_color_types: int) -> np.ndarray:
    """
    Makes an empty grid with rows equal to the most count of the color and columns equal to the number of unique color types.

    Args:
    count_of_colors: A list of tuples where the first element is the color type and the second element is the number of pixels of that color type in the input grid, sorted from most to least.
    number_of_color_types: An integer representing the number of unique color types in the input grid.

    Returns:
    A numpy array representing the empty output grid.
    """
    max_count = count_of_colors[0][1]
    return np.zeros((max_count, number_of_color_types), dtype=int)

def sort_count(count_of_colors: Dict[int, int]) -> List[Tuple[int, int]]:
    """
    Sorts the count of colors from most to least.

    Args:
    count_of_colors: A dictionary where the keys are the color types and the values are the number of pixels of that color type in the input grid.

    Returns:
    A list of tuples where the first element is the color type and the second element is the number of pixels of that color type in the input grid, sorted from most to least.
    """
    return sorted(count_of_colors.items(), key=lambda x: x[1], reverse=True)

def count_color_counts(input_grid: np.ndarray) -> Dict[int, int]:
    """
    Counts the number of pixels of each color type in the input grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    A dictionary where the keys are the color types and the values are the number of pixels of that color type in the input grid.
    """
    (unique_colors, counts) = np.unique(input_grid, return_counts=True)
    return dict(zip(unique_colors, counts))

def count_color_types(input_grid: np.ndarray) -> int:
    """
    Counts the number of unique color types in the input grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    An integer representing the number of unique color types in the input grid.
    """
    return len(np.unique(input_grid))

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you can see a input grid contains pixels of several color, you should count the number of each type of color,                                         
    sort the counts from the most to the least.                                                                                                                         
    The output grid has row equals to the most count of the color, col equals to the number of the colors.                                                              
    To make the output, color each col of same color from left to right according to the number of the counts sequence.                                                 
    """
    number_of_color_types = count_color_types(input_grid)
    count_of_colors = count_color_counts(input_grid)
    count_of_colors = sort_count(count_of_colors)
    output_grid = make_empty_grid(count_of_colors, number_of_color_types)
    output_grid = colorize_grid(output_grid, count_of_colors, number_of_color_types)
    return output_grid