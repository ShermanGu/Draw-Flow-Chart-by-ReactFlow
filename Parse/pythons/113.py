import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def border_pixels_to_adjacent_pixels(output_grid: np.ndarray, h: int, w: int) -> np.ndarray:
    for j in range(1, w + 1):
        output_grid[0][j] = output_grid[1][j]
        output_grid[h + 1][j] = output_grid[h][j]
    for i in range(1, h + 1):
        output_grid[i][0] = output_grid[i][1]
        output_grid[i][w + 1] = output_grid[i][w]
    return output_grid

def overlay_input_grid(output_grid: np.ndarray, input_grid: np.ndarray, h: int, w: int) -> np.ndarray:
    output_grid[1:h + 1, 1:w + 1] = input_grid[0:h, 0:w]
    return output_grid

def create_black_image(h: int, w: int) -> np.ndarray:
    output_grid = np.zeros((h + 2, w + 2), dtype=np.uint8)
    return output_grid

def get_height_width(image: np.ndarray) -> Tuple[int, int]:
    (h, w) = image.shape[:2]
    return (h, w)

def main(input_grid: np.ndarray) -> np.ndarray:
    (h, w) = get_height_width(input_grid)
    output_grid = create_black_image(h, w)
    output_grid = overlay_input_grid(output_grid, input_grid, h, w)
    output_grid = border_pixels_to_adjacent_pixels(output_grid, h, w)
    return output_grid