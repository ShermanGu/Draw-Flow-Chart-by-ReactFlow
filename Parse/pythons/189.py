import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def are_arrays_equal(arr1: np.ndarray, arr2: np.ndarray) -> bool:
    return np.array_equal(arr1, arr2)

def change_neighbor(input: np.ndarray, position: Tuple[int, int]) -> np.ndarray:
    (i, j) = position
    if input[i - 1][j - 1] != black:
        input[i + 1][j + 1] = input[i - 1][j - 1]
    if input[i - 1][j + 1] != black:
        input[i + 1][j - 1] = input[i - 1][j + 1]
    if input[i + 1][j - 1] != black:
        input[i - 1][j + 1] = input[i + 1][j - 1]
    if input[i + 1][j + 1] != black:
        input[i - 1][j - 1] = input[i + 1][j + 1]
    return input

def is_valid_position(input, position):
    (i, j) = position
    if input[i][j] == black:
        return False
    neighborhood = input[i - 1:i + 2, j - 1:j + 2]
    return np.count_nonzero(neighborhood != black) == 2

def is_converged(prev_output: np.ndarray, new_output: np.ndarray) -> bool:
    return are_arrays_equal(prev_output, new_output)

def func1(input):
    output = np.copy(input)
    for i in range(1, input.shape[0] - 1):
        for j in range(1, input.shape[1] - 1):
            if is_valid_position(output, (i, j)):
                output = change_neighbor(output, (i, j))
    return output

def main(input):
    output = np.copy(input)
    while True:
        output1 = func1(output)
        if is_converged(output, output1):
            break
        else:
            output = output1
    return output