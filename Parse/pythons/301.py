import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_subgrid(input_grid: np.ndarray, x: int, y: int, length: int, color: int) -> np.ndarray:
    """
    Given the input grid, the upper left corner (x, y) and the length of the sub-grid, color the sub-grid with the given color.
    """
    for i in range(x, x + length - 1):
        for j in range(y, y + length - 1):
            input_grid[i][j] = color
    return input_grid

def color_by_length(length: int) -> int:
    """
    Given the length of the sub-grid, return the corresponding color.
    """
    if length == 2:
        return pink
    elif length == 3:
        return orange
    elif length == 4:
        return teal
    else:
        return maroon

def color_gray_pixels(input_grid: np.ndarray, target_list: List[Tuple[int, int, int]]) -> np.ndarray:
    """
    Traverse the target_list, for each item (x, y, length), take (x+1, y+1) in the inputgrid as the upper left corner, 
    and color the sub-grid whose shape is (length-1, length-1): if length If the length is 2, the sub-grid will be painted in pink; 
    if the length is 3, the sub-grid will be painted in orange; if the length is 4, the sub-grid will be painted in teal.
    """
    for target in target_list:
        (x, y, length) = target
        color = color_by_length(length)
        input_grid = color_subgrid(input_grid, x + 1, y + 1, length, color)
    return input_grid

def find_gray_pixels(input_grid: np.ndarray) -> List[Tuple[int, int, int]]:
    """
    Iterate over all pixels in the input grid, if a pixel (x, y) is gray, and the pixels below and to the right of it are also gray. 
    Then traverse all the pixels in the same line, if there is a gray pixel (bx,by) and the pixel on the right side of the pixel is black, 
    record cnt=by-y. If cnt is not None, add (x, y, cnt) to the answer list.
    """
    gray_pixels = []
    n = input_grid.shape[0]
    for i in range(n - 1):
        for j in range(n - 1):
            if input_grid[i][j] == grey and input_grid[i + 1][j] == grey and (input_grid[i][j + 1] == grey):
                cnt = None
                for k in range(j + 1, n):
                    if input_grid[i][k] == black:
                        break
                    if input_grid[i][k] == grey:
                        if input_grid[i + 1][k] == grey:
                            cnt = k - j
                            break
                if cnt is not None:
                    gray_pixels.append((i, j, cnt))
    return gray_pixels

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    target_list = find_gray_pixels(input_grid)
    ans_grid = color_gray_pixels(input_grid, target_list)
    return ans_grid