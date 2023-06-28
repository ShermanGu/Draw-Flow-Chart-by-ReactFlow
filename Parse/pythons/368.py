import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_single_black_area_blue(input_grid: np.ndarray, i: int, j: int) -> None:
    """                                                                                                                                                  
    This function takes in a numpy array and two integers i and j representing the indices of a point in the array.                                      
    It performs a floodfill algorithm to color the black area of the given point blue.                                                                   
    """
    if input_grid[i][j] != yellow:
        return
    input_grid[i][j] = blue
    if i > 0:
        fill_single_black_area_blue(input_grid, i - 1, j)
    if i < len(input_grid) - 1:
        fill_single_black_area_blue(input_grid, i + 1, j)
    if j > 0:
        fill_single_black_area_blue(input_grid, i, j - 1)
    if j < len(input_grid[0]) - 1:
        fill_single_black_area_blue(input_grid, i, j + 1)

def fill_single_black_area_red(input_grid: np.ndarray, i: int, j: int) -> None:
    """                                                                                                                                                  
    This function takes in a numpy array and two integers i and j representing the indices of a point in the array.                                      
    It performs a floodfill algorithm to color the black area of the given point blue.                                                                   
    """
    if input_grid[i][j] != yellow:
        return
    input_grid[i][j] = red
    if i > 0:
        fill_single_black_area_red(input_grid, i - 1, j)
    if i < len(input_grid) - 1:
        fill_single_black_area_red(input_grid, i + 1, j)
    if j > 0:
        fill_single_black_area_red(input_grid, i, j - 1)
    if j < len(input_grid[0]) - 1:
        fill_single_black_area_red(input_grid, i, j + 1)

def fill_single_black_area(input_grid: np.ndarray, i: int, j: int) -> None:
    """                                                                                                                                                  
    This function takes in a numpy array and two integers i and j representing the indices of a point in the array.                                      
    It performs a floodfill algorithm to color the black area of the given point blue.                                                                   
    """
    if input_grid[i][j] != yellow:
        return
    input_grid[i][j] = green
    if i > 0:
        fill_single_black_area(input_grid, i - 1, j)
    if i < len(input_grid) - 1:
        fill_single_black_area(input_grid, i + 1, j)
    if j > 0:
        fill_single_black_area(input_grid, i, j - 1)
    if j < len(input_grid[0]) - 1:
        fill_single_black_area(input_grid, i, j + 1)

def count_connected_black_points(input_grid: np.ndarray, i: int, j: int) -> int:
    """                                                                                                                                                  
    This function takes in a numpy array and two integers i and j representing the indices of a point in the array.                                      
    It performs a floodfill algorithm to count how many black points are connected to the given point.                                                   
    It returns the count of connected black points.                                                                                                      
    """
    if input_grid[i][j] != black:
        return 0
    count = 1
    input_grid[i][j] = yellow
    if i > 0:
        count += count_connected_black_points(input_grid, i - 1, j)
    if i < len(input_grid) - 1:
        count += count_connected_black_points(input_grid, i + 1, j)
    if j > 0:
        count += count_connected_black_points(input_grid, i, j - 1)
    if j < len(input_grid[0]) - 1:
        count += count_connected_black_points(input_grid, i, j + 1)
    return count

def main(input_grid: np.ndarray) -> np.ndarray:
    for i in range(len(input_grid)):
        for j in range(len(input_grid[0])):
            count = count_connected_black_points(input_grid, i, j)
            if count == 1:
                fill_single_black_area(input_grid, i, j)
            elif count == 2:
                fill_single_black_area_red(input_grid, i, j)
            elif count == 3:
                fill_single_black_area_blue(input_grid, i, j)
    return input_grid