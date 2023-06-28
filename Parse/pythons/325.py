import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_upper_left_2x2(input_grid: List[List[int]]) -> List[List[int]]:
    return [row[:2] for row in input_grid[:2]]

def main(input_grid):
    return get_upper_left_2x2(input_grid)