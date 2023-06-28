import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_pixels_in_same_col_to_teal(indices_of_blue_pixels: List[Tuple[int, int]], output_grid: np.ndarray, ibp1: int, ibp2: int) -> np.ndarray:
    """Colors the black pixels to teal between the two blue pixels in the same column."""
    col = indices_of_blue_pixels[ibp1][1]
    start_row = indices_of_blue_pixels[ibp1][0]
    end_row = indices_of_blue_pixels[ibp2][0]
    if start_row > end_row:
        (start_row, end_row) = (end_row, start_row)
    for row in range(start_row + 1, end_row):
        if output_grid[row][col] == black:
            output_grid[row][col] = teal
    return output_grid

def color_pixels_in_same_row_to_teal(indices_of_blue_pixels: List[Tuple[int, int]], output_grid: np.ndarray, ibp1: int, ibp2: int) -> np.ndarray:
    """Colors the black pixels to teal between the two blue pixels in the same row."""
    row = indices_of_blue_pixels[ibp1][0]
    start_col = indices_of_blue_pixels[ibp1][1]
    end_col = indices_of_blue_pixels[ibp2][1]
    if start_col > end_col:
        (start_col, end_col) = (end_col, start_col)
    for col in range(start_col + 1, end_col):
        if output_grid[row][col] == black:
            output_grid[row][col] = teal
    return output_grid

def find_blue_pixels(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """Returns a list of tuples containing the indices of blue pixels in the input grid."""
    blue_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                blue_pixels.append((i, j))
    return blue_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see blue pixels on the black grid                                                                                                          
    if two blue pixels are in same row or same col, color the black pixels to teal between the two blue pixels.                                                         
    """
    output_grid = input_grid.copy()
    indices_of_blue_pixels = find_blue_pixels(output_grid)
    for ibp1 in range(len(indices_of_blue_pixels) - 1):
        for ibp2 in range(ibp1, len(indices_of_blue_pixels)):
            if indices_of_blue_pixels[ibp1][0] == indices_of_blue_pixels[ibp2][0]:
                output_grid = color_pixels_in_same_row_to_teal(indices_of_blue_pixels, output_grid, ibp1, ibp2)
            if indices_of_blue_pixels[ibp1][1] == indices_of_blue_pixels[ibp2][1]:
                output_grid = color_pixels_in_same_col_to_teal(indices_of_blue_pixels, output_grid, ibp1, ibp2)
    return output_grid