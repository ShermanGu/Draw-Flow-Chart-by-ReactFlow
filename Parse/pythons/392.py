import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def sort_colors_by_frequency(input: np.ndarray, colors: Set[int]) -> List[int]:
    """
    This function takes an input numpy array and a set of colors and returns a list of colors sorted by their frequency in the input array.

    Args:
    input: A numpy array of integers representing colors.
    colors: A set of unique colors present in the input array except black.

    Returns:
    A list of colors sorted by their frequency in the input array.
    """
    color_counts = [(color, np.count_nonzero(input == color)) for color in colors]
    sorted_colors = [color for (color, count) in sorted(color_counts, key=lambda x: x[1], reverse=True)]
    return sorted_colors

def find_colors(input):
    return set(np.unique(input)) - {black}

def main(input):
    colors = find_colors(input)
    sorted_colors = sort_colors_by_frequency(input, colors)
    output = np.array([sorted_colors], dtype=np.int32)
    return output.T