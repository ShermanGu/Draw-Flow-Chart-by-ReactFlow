import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_non_blue_pixels_to_pink(input_grid: np.ndarray, centers: List[Tuple[int, int]]) -> np.ndarray:
    """
    Traverse the recorded center coordinates of the squares obtained in Step 1
    (assuming the current coordinate is (i,j)).
    Change the color of non-blue pixels in the same row and column as the current pixel to pink.
    """
    output_grid = input_grid.copy()
    for center in centers:
        (i, j) = (center[0], center[1])
        for x in range(input_grid.shape[0]):
            if output_grid[x][j] != blue:
                output_grid[x][j] = pink
        for y in range(input_grid.shape[1]):
            if output_grid[i][y] != blue:
                output_grid[i][y] = pink
    return output_grid

def find_blue_squares_centers(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    """
    Traverse the entire image. If the color of the pixel (at coordinate (i, j)) and the color of the pixel below (at coordinate (i+1, j)) and the pixel to the right (at coordinate (i, j+1)) of the current pixel (assumed to have coordinate (i,j)) are both blue, then record the coordinate (i+2, j+2) as the center coordinate of a square.
    """
    centers = []
    for i in range(input_grid.shape[0] - 1):
        for j in range(input_grid.shape[1] - 1):
            if input_grid[i][j] == blue and input_grid[i + 1][j] == blue and (input_grid[i][j + 1] == blue):
                centers.append((i + 2, j + 2))
    return centers

def main(input_grid: np.ndarray) -> np.ndarray:
    centers = find_blue_squares_centers(input_grid)
    output_grid = change_non_blue_pixels_to_pink(input_grid, centers)
    return output_grid