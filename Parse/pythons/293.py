import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_grey_rectangles_and_make_inside_red(input: List[List[int]]) -> List[List[int]]:
    """
    This function takes a 2D list of integers as input and finds all the grey rectangles in it.
    It then makes the inside of these rectangles red and returns the updated 2D list.
    
    Args:
    - input: A 2D list of integers representing a grid of colors.
    
    Returns:
    - A 2D list of integers representing the updated grid of colors.
    """
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == grey:
                left = j
                right = j
                while left > 0 and input[i][left - 1] == grey:
                    left -= 1
                while right < len(input[0]) - 1 and input[i][right + 1] == grey:
                    right += 1
                top = i
                bottom = i
                while top > 0 and all((x == grey for x in input[top - 1][left:right + 1])):
                    top -= 1
                while bottom < len(input) - 1 and all((x == grey for x in input[bottom + 1][left:right + 1])):
                    bottom += 1
                for x in range(top + 1, bottom):
                    for y in range(left + 1, right):
                        input[x][y] = red
    return input

def main(input):
    return find_grey_rectangles_and_make_inside_red(input)