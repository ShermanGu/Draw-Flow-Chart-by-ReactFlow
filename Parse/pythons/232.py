import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def match(grid1: np.ndarray, grid2: np.ndarray) -> bool:
    for i in range(grid1.shape[0]):
        for j in range(grid1.shape[1]):
            if grid1[i][j] == red and grid2[i][j] == red:
                return False
            elif grid1[i][j] == black and grid2[i][j] != red:
                return False
    return True

def rotate_square(square: np.ndarray) -> List[np.ndarray]:
    rotated_squares = []
    for i in range(4):
        rotated_squares.append(np.rot90(square, i))
    return rotated_squares

def have_other_colors(square: np.ndarray) -> bool:
    unique_colors = np.unique(square)
    if len(unique_colors) == 2 and black in unique_colors and (red in unique_colors):
        return False
    return True

def match_and_color(grid: np.ndarray, i: int, j: int, square: np.ndarray):
    square_to_match = grid[i:i + 3, j:j + 3]
    if have_other_colors(square_to_match):
        return
    rotated_squares = rotate_square(square)
    for rotated_square in rotated_squares:
        if match(square_to_match, rotated_square):
            grid[i:i + 3, j:j + 3] = rotated_square
            return

def extract_red_shape(grid: np.ndarray, top_left: Tuple[int, int], bottom_right: Tuple[int, int]) -> np.ndarray:
    return grid[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]

def find_red_shape(grid: np.ndarray) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    red_indices = np.where(grid == red)
    top_left = (np.min(red_indices[0]), np.min(red_indices[1]))
    bottom_right = (np.max(red_indices[0]), np.max(red_indices[1]))
    return (top_left, bottom_right)

def paint_black_3x3(grid: np.ndarray, coordinates: List[Tuple[int, int]]) -> np.ndarray:
    for (i, j) in coordinates:
        grid[i:i + 3, j:j + 3] = black
    return grid

def extract_squares(grid, coordinates):
    return [grid[x:x + 3, y:y + 3].copy() for (x, y) in coordinates]

def find_two_color_grids(coordinates: List[Tuple[int, int]], grid: np.ndarray) -> List[Tuple[int, int]]:
    two_color_grids = []
    for (i, j) in coordinates:
        square = grid[i:i + 3, j:j + 3]
        unique_colors = np.unique(square)
        if len(unique_colors) == 2 and black not in unique_colors:
            two_color_grids.append((i, j))
    return two_color_grids

def get_coordinates(grid: np.ndarray) -> List[Tuple[int, int]]:
    coordinates = []
    for i in range(grid.shape[0] - 2):
        for j in range(grid.shape[1] - 2):
            coordinates.append((i, j))
    return coordinates

def main(input_grid: np.ndarray) -> np.ndarray:
    coordinates = get_coordinates(input_grid)
    squares_coordinates = find_two_color_grids(coordinates, input_grid)
    squares = extract_squares(input_grid, squares_coordinates)
    input_grid = paint_black_3x3(input_grid, squares_coordinates)
    (top_left, bottom_right) = find_red_shape(input_grid)
    output_grid = extract_red_shape(input_grid, top_left, bottom_right)
    for (x, y) in get_coordinates(output_grid):
        for square in squares:
            match_and_color(output_grid, x, y, square)
    return output_grid