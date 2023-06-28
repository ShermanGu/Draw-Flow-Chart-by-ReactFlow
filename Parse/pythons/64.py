import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_non_monochrome_array(inputs: Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]) -> np.ndarray:
    for arr in inputs:
        if len(np.unique(arr)) > 1:
            return arr
    return None

def split_input(input: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    center_x = input.shape[0] // 2
    center_y = input.shape[1] // 2
    top_left = input[:center_x, :center_y]
    top_right = input[:center_x, center_y + 1:]
    bottom_left = input[center_x + 1:, :center_y]
    bottom_right = input[center_x + 1:, center_y + 1:]
    return (top_left, top_right, bottom_left, bottom_right)

def main(input):
    inputs = split_input(input)
    output = find_non_monochrome_array(inputs)
    return output