import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_rows(input_grid: np.ndarray) -> np.ndarray:
    for row in input_grid:
        if np.all(row == row[0]):
            row.fill(grey)
        else:
            row.fill(black)
    return input_grid

def main(input_grid: np.ndarray) -> np.ndarray:
    paint_rows(input_grid)
    return input_grid