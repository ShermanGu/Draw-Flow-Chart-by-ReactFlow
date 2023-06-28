import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def mirror_diagonal(input_grid: np.ndarray) -> np.ndarray:
    return np.transpose(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = mirror_diagonal(input_grid)
    return output_grid