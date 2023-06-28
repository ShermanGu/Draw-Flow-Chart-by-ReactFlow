import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_inside(input: np.ndarray, rectangle: Tuple[int, int, int, int], color: int) -> np.ndarray:
    """
    This function takes a 2-dimensional numpy array as input, a tuple representing a rectangle in the input, and a color.
    It colors the inside of the rectangle with the given color and returns the modified numpy array.
    """
    (x, y, w, h) = rectangle
    for i in range(x + 1, x + h - 1):
        for j in range(y + 1, y + w - 1):
            input[i][j] = color
    return input

def get_max_min_area_rectangles(rectangles: List[Tuple[int, int, int, int]]) -> Tuple[Tuple[int, int, int, int], Tuple[int, int, int, int]]:
    """
    This function takes a list of tuples, where each tuple represents a yellow rectangle in the input. The tuple contains
    the coordinates of the top-left corner of the rectangle and its width and height. It returns a tuple of two tuples,
    where the first tuple represents the rectangle with the maximum area and the second tuple represents the rectangle
    with the minimum area.
    """
    max_area = 0
    min_area = float('inf')
    max_rectangle = None
    min_rectangle = None
    for rectangle in rectangles:
        area = rectangle[2] * rectangle[3]
        if area > max_area:
            max_area = area
            max_rectangle = rectangle
        if area < min_area:
            min_area = area
            min_rectangle = rectangle
    return (max_rectangle, min_rectangle)

def black_rectangle(input: np.ndarray, rectangle: Tuple[int, int, int, int]) -> np.ndarray:
    """
    This function takes a 2-dimensional numpy array as input and a tuple representing a rectangle in the input.
    It colors the inside of the rectangle with black color and returns the modified numpy array.
    """
    (x, y, w, h) = rectangle
    for i in range(x, x + h):
        for j in range(y, y + w):
            input[i][j] = black
    return input

def find_largest_yellow_rectangles(input: np.ndarray) -> List[Tuple[int, int, int, int]]:
    """
    This function takes a 2-dimensional numpy array as input and returns a list of tuples, where each tuple represents a
    yellow rectangle in the input. The tuple contains the coordinates of the top-left corner of the rectangle and its
    width and height. If there are multiple rectangles with the same largest size, all of them should be included in the
    output list.
    """
    rectangles = []
    for i in range(input.shape[0]):
        for j in range(input.shape[1]):
            if input[i][j] == yellow:
                width = 1
                height = 1
                while i + height < input.shape[0] and input[i + height][j] == yellow:
                    height += 1
                while j + width < input.shape[1] and input[i][j + width] == yellow:
                    width += 1
                rectangles.append((i, j, width, height))
    max_size = max([w * h for (_, _, w, h) in rectangles])
    return [(i, j, w, h) for (i, j, w, h) in rectangles if w * h == max_size]

def main(input):
    rectangles1 = find_largest_yellow_rectangles(input)
    output = np.copy(input)
    output = black_rectangle(output, rectangles1[0])
    rectangles2 = find_largest_yellow_rectangles(output)
    (max_rectangle, min_rectangle) = get_max_min_area_rectangles([rectangles1[0], rectangles2[0]])
    output = np.copy(input)
    output = color_inside(output, max_rectangle, red)
    output = color_inside(output, min_rectangle, blue)
    return output