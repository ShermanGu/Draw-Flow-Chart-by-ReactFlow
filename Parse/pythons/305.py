import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def separate_input_into_parts(input: np.ndarray, x: int, y: int) -> List[np.ndarray]:
    """
    Separates the input numpy array into x * y parts.
    
    Args:
    input: A numpy array representing the input image.
    x: An integer representing the number of parts in the horizontal direction.
    y: An integer representing the number of parts in the vertical direction.
    
    Returns:
    A list of numpy arrays representing the separated input.
    """
    (height, width) = input.shape
    (part_height, part_width) = (height // y, width // x)
    parts = []
    for i in range(y):
        for j in range(x):
            part = input[i * part_height:(i + 1) * part_height, j * part_width:(j + 1) * part_width]
            parts.append(part)
    return parts

def remove_yellow_rows_and_columns(input: np.ndarray) -> np.ndarray:
    """
    Removes all yellow rows and columns from the input numpy array.
    
    Args:
    input: A numpy array representing the input image.
    
    Returns:
    A numpy array representing the output image with yellow rows and columns removed.
    """
    return input[~np.all(input == yellow, axis=1)][:, ~np.all(input == yellow, axis=0)]

def count_yellow_in_first_row(input: np.ndarray) -> int:
    """
    Counts the number of yellow positions in the first row of the input numpy array.
    
    Args:
    input: A numpy array representing the input image.
    
    Returns:
    An integer representing the number of yellow positions in the first row.
    """
    return np.count_nonzero(input[0, :] == yellow)

def count_yellow_in_first_column(input: np.ndarray) -> int:
    """
    Counts the number of yellow positions in the first column of the input numpy array.
    
    Args:
    input: A numpy array representing the input image.
    
    Returns:
    An integer representing the number of yellow positions in the first column.
    """
    return np.count_nonzero(input[:, 0] == yellow)

def repeat_pattern_and_add_dividing_lines(pattern: np.ndarray, a: int, b: int) -> np.ndarray:
    """
    Repeats the pattern in a * b, and adds yellow dividing lines.
    
    Args:
    pattern: A numpy array representing the pattern to be repeated.
    a: An integer representing the number of times the pattern should be repeated in the vertical direction.
    b: An integer representing the number of times the pattern should be repeated in the horizontal direction.
    
    Returns:
    A numpy array representing the output image with repeated pattern and yellow dividing lines.
    """
    repeated_pattern = np.tile(pattern, (a, b))
    (i, j) = pattern.shape
    for k in range(1, a):
        repeated_pattern = np.insert(repeated_pattern, k * i + k - 1, yellow, axis=0)
    for k in range(1, b):
        repeated_pattern = np.insert(repeated_pattern, k * j + k - 1, yellow, axis=1)
    return repeated_pattern

def find_different_color(inputs: List[np.ndarray]) -> np.ndarray:
    """
    Finds the numpy array in the list of inputs that has different colors than the others.
    
    Args:
    inputs: A list of numpy arrays representing the separated input.
    
    Returns:
    A numpy array representing the pattern with different colors.
    """
    for i in range(len(inputs)):
        if np.unique(inputs[i]).size > 1:
            return inputs[i]
    return None

def separate_input(input):
    x = count_yellow_in_first_column(input)
    y = count_yellow_in_first_row(input)
    input = remove_yellow_rows_and_columns(input)
    inputs = separate_input_into_parts(input, y + 1, x + 1)
    return inputs

def main(input):
    inputs = separate_input(input)
    pattern = find_different_color(inputs)
    (i_s, js) = input.shape
    (i, j) = pattern.shape
    a = i_s // i
    b = js // j
    output = repeat_pattern_and_add_dividing_lines(pattern, a, b)
    return output