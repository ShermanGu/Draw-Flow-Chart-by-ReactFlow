import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_max_red_rect(blue_red_rects, input_grid):
    return input_grid[blue_red_rects[0][0]:blue_red_rects[1][0] + 1, blue_red_rects[0][1]:blue_red_rects[1][1] + 1]

def find_blue_rect_with_most_red_pixels(blue_red_rects: List[Tuple[Tuple[int, int], Tuple[int, int]]], input_grid: np.ndarray) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Given a list of blue rectangles (may include red pixels) and an input grid, this function finds the blue rectangle with the most red pixels.

    Args:
    - blue_red_rects (List[Tuple[Tuple[int, int], Tuple[int, int]]]): A list of tuples, where each tuple represents the top-left and bottom-right coordinates of a blue rectangle in the input grid.
    - input_grid (np.ndarray): A 2D numpy array representing the input grid.

    Returns:
    - Tuple[Tuple[int, int], Tuple[int, int]]: A tuple representing the top-left and bottom-right coordinates of the blue rectangle with the most red pixels in the input grid.
    """
    max_red_pixels = 0
    max_red_rect = None
    for rect in blue_red_rects:
        top_left = rect[0]
        bottom_right = rect[1]
        red_pixels = 0
        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                if input_grid[i][j] == red:
                    red_pixels += 1
        if red_pixels > max_red_pixels:
            max_red_pixels = red_pixels
            max_red_rect = rect
    return max_red_rect

def find_blue_rectangles(input_grid: np.ndarray) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """                                                                                                                                          
    Given an input grid, this function finds all the blue rectangles (may include red pixels) in the input_grid.                                 
                                                                                                                                                 
    Args:                                                                                                                                        
    input_grid: A numpy array representing the input grid.                                                                                       
                                                                                                                                                 
    Returns:                                                                                                                                     
    A list of tuples, where each tuple represents the top-left and bottom-right coordinates of a blue rectangle.                                 
    """
    flags = np.zeros_like(input_grid)
    blue_rects = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue and (not flags[i, j]):
                top_left = (i, j)
                bottom_right = (i, j)
                while bottom_right[1] < input_grid.shape[1] - 1 and input_grid[i][bottom_right[1] + 1] in [blue, red]:
                    bottom_right = (i, bottom_right[1] + 1)
                while bottom_right[0] < input_grid.shape[0] - 1 and input_grid[bottom_right[0] + 1][j] in [blue, red]:
                    bottom_right = (bottom_right[0] + 1, bottom_right[1])
                blue_rects.append((top_left, bottom_right))
                flags[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1] = 1
    return blue_rects

def main(input_grid: np.ndarray) -> np.ndarray:
    blue_red_rects = find_blue_rectangles(input_grid)
    max_red_rect = find_blue_rect_with_most_red_pixels(blue_red_rects, input_grid)
    output_grid = get_max_red_rect(max_red_rect, input_grid)
    return output_grid