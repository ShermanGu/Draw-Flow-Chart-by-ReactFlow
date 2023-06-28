import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    color the yellow pixels that in the column that can mod 3 to pink.
    """
    output_grid = input_grid.copy()
    for col in range(input_grid.shape[1]):
        for row in range(input_grid.shape[0]):
            if col % 3 == 0:
                if output_grid[row, col] == yellow:
                    output_grid[row, col] = pink
    return output_grid