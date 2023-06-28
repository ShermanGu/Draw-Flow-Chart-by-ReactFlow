import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def clip_input(input1: List[List[int]], input2: List[List[int]]) -> List[List[int]]:
    """
    Clips the input1 to have the same number of rows as input2.

    Args:
    input1: A list of lists containing integers.
    input2: A list of lists containing integers.

    Returns:
    A list of lists containing integers, with the same number of rows as input2.
    """
    clipped_input = input1[:len(input2)]
    return clipped_input

def repeat_rows(input: List[List[int]]) -> List[List[int]]:
    """
    Repeats the rows of the input six times vertically.

    Args:
    input: A list of lists containing integers.

    Returns:
    A list of lists containing integers, with each row repeated six times vertically.
    """
    clipped_input = input[3:6]
    repeated_input = [clipped_input] * 6
    return np.array(repeated_input).reshape(-1, len(input[0])).tolist()

def main(input):
    output = repeat_rows(input)
    output = clip_input(output, input)
    return output