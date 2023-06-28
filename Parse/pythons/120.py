import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def extract_3x3_grid(input_grid: np.ndarray, special_pixels: Tuple[int, int]) -> np.ndarray:
    """
    This function takes in the input grid as a numpy array and the special pixel's indices as a tuple.
    It extracts the 3x3 grid from the input_grid whose center is the special pixel.
    It returns the extracted 3x3 grid.
    """
    (i, j) = special_pixels
    return input_grid[i - 1:i + 2, j - 1:j + 2]

def change_special_pixel_color(input_grid: np.ndarray, special_pixels: Tuple[int, int]) -> np.ndarray:
    """
    This function takes in the input grid as a numpy array and the special pixel's indices as a tuple.
    It changes the color of the special pixel to the color of its surrounding pixels, except for black.
    It returns the updated input grid.
    """
    (i, j) = special_pixels
    surrounding_pixels = get_surrounding_pixels(i, j, input_grid)
    new_color = [color for color in surrounding_pixels if color != black][0]
    input_grid[i, j] = new_color
    return input_grid

def get_surrounding_pixels(i: int, j: int, input_grid: np.ndarray) -> List[int]:
    """
    This function takes in the row index i, column index j, and the input grid as a numpy array.
    It returns a list of the surrounding pixels of the 3x3 grid in the input_grid except for itself.
    """
    return [input_grid[x, y] for x in range(i - 1, i + 2) for y in range(j - 1, j + 2) if 0 <= x < input_grid.shape[0] and 0 <= y < input_grid.shape[1] and ((x, y) != (i, j))]

def main(input_grid: np.ndarray) -> np.ndarray:
    flag = False
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            surroding_pixels = get_surrounding_pixels(i, j, input_grid)
            if surroding_pixels != [black] * 9 and input_grid[i, j] not in surroding_pixels and (not flag):
                flag = True
                special_pixels = (i, j)
    input_grid = change_special_pixel_color(input_grid, special_pixels)
    output_grid = extract_3x3_grid(input_grid, special_pixels)
    return output_grid