import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def overwrite_pixels(input_grid: np.ndarray, target_grid: np.ndarray, mask_grid: np.ndarray) -> np.ndarray:
    """
    Traverse all the elements in the input_grid, match each pixel with a grid same as mask_grid, 
    if the current pixel is matched, overwrite the position with a grid same as target_grid
    """
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if np.array_equal(input_grid[i:i + mask_grid.shape[0], j:j + mask_grid.shape[1]], mask_grid):
                input_grid[i:i + target_grid.shape[0], j:j + target_grid.shape[1]] = target_grid
    return input_grid

def generate_teal_mask(target_grid: np.ndarray) -> np.ndarray:
    """
    Generate a new grid with the same size as the target_grid. If the pixel in the subgrid is non-black, the value in the new grid is teal; otherwise, it is black
    """
    return np.where(target_grid != black, teal, black)

def extract_subgrid(grid: np.ndarray, minx: int, miny: int, maxx: int, maxy: int) -> np.ndarray:
    """
    Extract the subgrid with (minx, miny) as the upper left corner and (maxx, maxy) as the lower right corner, and return the grid
    """
    return grid[minx:maxx + 1, miny:maxy + 1]

def find_bounding_box(grid: np.ndarray) -> Tuple[int, int, int, int]:
    """
    Define four variables (minx, miny, maxx, maxy) as the smallest x, the smallest y, the largest x, and the largest y. 
    Traverse all the pixels in the new grid, if a pixel (x, y) is not black, use the pixel to update the above four variables
    """
    (minx, miny, maxx, maxy) = (float('inf'), float('inf'), -float('inf'), -float('inf'))
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if grid[x, y] != black:
                minx = min(minx, x)
                miny = min(miny, y)
                maxx = max(maxx, x)
                maxy = max(maxy, y)
    return (minx, miny, maxx, maxy)

def blacken_teal_pixels(input_grid: np.ndarray) -> np.ndarray:
    """
    Generate a new grid, exactly the same as input_grid. Blacken all the teal pixels.
    """
    return np.where(input_grid == teal, black, input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    ans_grid = blacken_teal_pixels(input_grid)
    (minx, miny, maxx, maxy) = find_bounding_box(ans_grid)
    target_grid = extract_subgrid(ans_grid, minx, miny, maxx, maxy)
    mask_grid = generate_teal_mask(target_grid)
    input_grid[minx:maxx + 1, miny:maxy + 1] = black
    ans = overwrite_pixels(input_grid, target_grid, mask_grid)
    return ans