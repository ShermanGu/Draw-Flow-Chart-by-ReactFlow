import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def paint_red(input_grid: np.ndarray, ans_list: List[Tuple[int, int, int, int]]) -> np.ndarray:
    """
    Traversing the ans_list for each item (x, y, lengtha, lengthb), the inputgrid (x+1, y+1) pixel is the upper left corner, 
    and the shape is the child of (lengthb-1, lengtha -a) All the grids are painted red and return to the modified grid
    """
    for item in ans_list:
        (x, y, lengtha, lengthb) = item
        input_grid[x + 1:x + lengthb, y + 1:y + lengtha] = red
    return input_grid

def find_yellow_pixels(input_grid: np.ndarray) -> List[Tuple[int, int, int, int]]:
    """
    Traverse all the pixels in the inputgrid, if a pixel (x, y) is yellow. Traverse all pixels in the same column, 
    if there is another yellow pixel (ax, ay) and ax>x, record cnt1 = ax - x; traverse all pixels in the same row, 
    if there is another yellow pixel (bx,by) and bx> x, remember cnt2=by-y. If cnt1 and cnt2 are non-none, 
    add (x, y, cnt1, cnt2) to the answer list.
    """
    ans_list = []
    for x in range(input_grid.shape[0]):
        for y in range(input_grid.shape[1]):
            if input_grid[x][y] == yellow:
                cnt1 = None
                cnt2 = None
                for ax in range(x + 1, input_grid.shape[0]):
                    if input_grid[ax][y] == yellow:
                        cnt1 = ax - x
                        break
                for by in range(y + 1, input_grid.shape[1]):
                    if input_grid[x][by] == yellow:
                        cnt2 = by - y
                        break
                if cnt1 is not None and cnt2 is not None:
                    ans_list.append((x, y, cnt1, cnt2))
    return ans_list

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    In the input, you should see a n*n grid with multiple color pixels.
    """
    ans_list = find_yellow_pixels(input_grid)
    ans_grid = paint_red(input_grid, ans_list)
    return ans_grid