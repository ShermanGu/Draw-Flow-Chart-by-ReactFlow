import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_non_black(input: np.ndarray, color: int) -> np.ndarray:
    """
    Given a 2D numpy array and a color, this function colors all the positions in the input array which is not black with the color.
    """
    input[input != black] = color
    return input

def find_middle_color(input: np.ndarray) -> int:
    """
    Given a 2D numpy array representing a grid of colors, this function finds the color which is not black inside of input.
    It eliminates the outermost circle and returns the color of the remaining cells.
    """
    inner_input = input[1:-1, 1:-1]
    unique_colors = np.unique(inner_input[inner_input != black])
    if len(unique_colors) == 1:
        return unique_colors[0]
    else:
        return black

def clip_rectangle(input: List[List[int]], rectangle: Tuple[Tuple[int, int], Tuple[int, int]]) -> np.ndarray:
    """
    Given a 2D list of integers representing a grid of colors and a tuple representing the coordinates of the top-left and bottom-right corners of a rectangle,
    this function clips the rectangle from the input and returns it as a numpy array.
    """
    ((x1, y1), (x2, y2)) = rectangle
    return np.array(input[x1:x2 + 1, y1:y2 + 1])

def find_max_rectangle(hollow_rectangles: List[Tuple[Tuple[int, int], Tuple[int, int]]]) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Given a list of tuples representing the coordinates of the top-left and bottom-right corners of hollow rectangles,
    this function returns the maximum rectangle among them.
    """
    max_area = 0
    max_rectangle = None
    for rectangle in hollow_rectangles:
        ((x1, y1), (x2, y2)) = rectangle
        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        if area > max_area:
            max_area = area
            max_rectangle = rectangle
    return max_rectangle

def find_hollow_rectangles(input: List[List[int]]) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Given a 2D list of integers representing a grid of colors, this function finds all the hollow rectangles in the grid.
    A hollow rectangle is defined as a rectangle with non-black cells on the border and black cells in the interior.
    The function returns a list of tuples, where each tuple represents the coordinates of the top-left and bottom-right corners of a hollow rectangle.
    """
    hollow_rectangles = []
    (rows, cols) = (len(input), len(input[0]))
    for i in range(rows):
        for j in range(cols):
            if input[i][j] != black:
                if (i == 0 or input[i - 1][j] == black) and (j == 0 or input[i][j - 1] == black):
                    k = j
                    while k < cols and input[i][k] != black:
                        k += 1
                    l = i
                    while l < rows and input[l][j] != black:
                        l += 1
                    hollow_rectangles.append(((i, j), (l - 1, k - 1)))
    return hollow_rectangles

def main(input):
    hollow_rectangles = find_hollow_rectangles(input)
    max_hollow_rectangle = find_max_rectangle(hollow_rectangles)
    output = clip_rectangle(input, max_hollow_rectangle)
    color = find_middle_color(output)
    output = color_non_black(output, color)
    return output