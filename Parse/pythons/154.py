import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def flip_vertically(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see...many pixels of various colors
    The output grid size...is the same as the input grid size
    To make the output, you have to...flip the input grid vertically
    """
    output_grid = np.flipud(input_grid)
    return output_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see...many pixels of various colors
    The output grid size...is the same as the input grid size
    To make the output, you have to...flip the input grid vertically
    """
    output_grid = flip_vertically(input_grid)
    return output_grid