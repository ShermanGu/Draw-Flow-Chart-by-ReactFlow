import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_bottom_right_position(input: np.ndarray, color: int) -> Tuple[int, int]:
    """
    This function takes in a numpy array representing a grid of integers and a color.
    It returns the most bottom right position with a different color than the given color.
    """
    for i in range(len(input) - 1, -1, -1):
        for j in range(len(input[0]) - 1, -1, -1):
            if input[i][j] != color:
                return (i, j)
    return (-1, -1)

def find_top_left_position(input: np.ndarray, color: int) -> Tuple[int, int]:
    """
    This function takes in a numpy array representing a grid of integers and a color.
    It returns the most top left position with a different color than the given color.
    """
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != color:
                return (i, j)
    return (-1, -1)

def all_positions_same_color(input: np.ndarray) -> bool:
    """
    This function takes in a numpy array representing a grid of integers.
    It returns True if all positions in the input are the same color, False otherwise.
    """
    return (input == input[0, 0]).all()

def color_output(output: np.ndarray, colors: List[int]) -> np.ndarray:
    """
    This function takes in a numpy array representing an output grid and a list of colors.
    It colors the output in a spiral pattern, starting from the outside and moving inwards, changing one circle at a time.
    """
    color_index = 0
    row_start = col_start = 0
    row_end = col_end = output.shape[0] - 1
    while row_start <= row_end and col_start <= col_end:
        for j in range(col_start, col_end + 1):
            output[row_start][j] = colors[color_index]
        row_start += 1
        for i in range(row_start, row_end + 1):
            output[i][col_end] = colors[color_index]
        col_end -= 1
        if row_start <= row_end:
            for j in range(col_end, col_start - 1, -1):
                output[row_end][j] = colors[color_index]
            row_end -= 1
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                output[i][col_start] = colors[color_index]
            col_start += 1
        color_index += 1
    return output

def find_and_sort_colors(input):
    color = []
    while True:
        color.append(input[0, 0])
        if all_positions_same_color(input):
            break
        position_1 = find_top_left_position(input, color[-1])
        position_2 = find_bottom_right_position(input, color[-1])
        input = input[position_1[0]:position_2[0], position_1[1]:position_2[1]]
    return color

def main(input_grid):
    exist_colors = find_and_sort_colors(input_grid)
    number_colors = len(exist_colors)
    output = np.zeros((2 * number_colors - 1, 2 * number_colors - 1), dtype=np.int32)
    output = color_output(output, exist_colors)
    return output