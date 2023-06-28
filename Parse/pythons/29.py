import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def overlay_grids(output_grid: np.ndarray, red_grid: np.ndarray, blue_grid: np.ndarray, yellow_grid: np.ndarray, blue_x1: int, blue_y1: int, red_y1: int, yellow_y1: int) -> np.ndarray:
    output_grid[blue_x1:blue_x1 + blue_grid.shape[0], blue_y1:blue_y1 + blue_grid.shape[1]] = blue_grid
    output_grid[blue_x1:red_grid.shape[0] + blue_x1, red_y1:red_grid.shape[1] + red_y1] = red_grid
    output_grid[blue_x1:yellow_grid.shape[0] + blue_x1, yellow_y1:yellow_grid.shape[1] + yellow_y1] = yellow_grid
    return output_grid

def create_black_image(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.zeros_like(input_grid)
    output_grid.fill(black)
    return output_grid

def extract_images(input_grid: np.ndarray, red_x1: int, red_x2: int, red_y1: int, red_y2: int, blue_x1: int, blue_x2: int, blue_y1: int, blue_y2: int, yellow_x1: int, yellow_x2: int, yellow_y1: int, yellow_y2: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    red_grid = input_grid[red_x1:red_x2 + 1, red_y1:red_y2 + 1]
    blue_grid = input_grid[blue_x1:blue_x2 + 1, blue_y1:blue_y2 + 1]
    yellow_grid = input_grid[yellow_x1:yellow_x2 + 1, yellow_y1:yellow_y2 + 1]
    return (red_grid, blue_grid, yellow_grid)

def find_block_columns(input_grid: np.ndarray) -> Tuple[int, int, int, int, int, int]:
    (red_y1, red_y2, blue_y1, blue_y2, yellow_y1, yellow_y2) = (-1, -1, -1, -1, -1, -1)
    for j in range(input_grid.shape[1]):
        for i in range(input_grid.shape[0]):
            if input_grid[i][j] == red:
                if red_y1 == -1:
                    red_y1 = j
                red_y2 = j
            elif input_grid[i][j] == blue:
                if blue_y1 == -1:
                    blue_y1 = j
                blue_y2 = j
            elif input_grid[i][j] == yellow:
                if yellow_y1 == -1:
                    yellow_y1 = j
                yellow_y2 = j
    return (red_y1, red_y2, blue_y1, blue_y2, yellow_y1, yellow_y2)

def find_block_rows(input_grid: np.ndarray) -> Tuple[int, int, int, int, int, int]:
    (red_x1, red_x2, blue_x1, blue_x2, yellow_x1, yellow_x2) = (-1, -1, -1, -1, -1, -1)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == red:
                if red_x1 == -1:
                    red_x1 = i
                red_x2 = i
            elif input_grid[i][j] == blue:
                if blue_x1 == -1:
                    blue_x1 = i
                blue_x2 = i
            elif input_grid[i][j] == yellow:
                if yellow_x1 == -1:
                    yellow_x1 = i
                yellow_x2 = i
    return (red_x1, red_x2, blue_x1, blue_x2, yellow_x1, yellow_x2)

def main(input_grid: np.ndarray) -> np.ndarray:
    (red_x1, red_x2, blue_x1, blue_x2, yellow_x1, yellow_x2) = find_block_rows(input_grid)
    (red_y1, red_y2, blue_y1, blue_y2, yellow_y1, yellow_y2) = find_block_columns(input_grid)
    (red_grid, blue_grid, yellow_grid) = extract_images(input_grid, red_x1, red_x2, red_y1, red_y2, blue_x1, blue_x2, blue_y1, blue_y2, yellow_x1, yellow_x2, yellow_y1, yellow_y2)
    output_grid = create_black_image(input_grid)
    output_grid = overlay_grids(output_grid, red_grid, blue_grid, yellow_grid, blue_x1, blue_y1, red_y1, yellow_y1)
    return output_grid