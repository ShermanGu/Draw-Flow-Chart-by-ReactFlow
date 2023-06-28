import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_lines(input, colors):
    for i in range(len(colors)):
        input[i + 2] = colors[i]
    return input

def concatenate_arrays(arr1: List[int], arr2: List[int]) -> List[int]:
    return np.concatenate((arr1, arr2))

def main(input):
    colors = input[0]
    colors = concatenate_arrays(colors, colors)
    output = color_lines(input, colors)
    return output