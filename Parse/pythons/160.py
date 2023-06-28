import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_columns_to_color(input_grid: np.ndarray, color: int, columns: List[int]) -> np.ndarray:
    """
    Given a 2D numpy array, a color, and a list of columns, changes all the cells in the specified columns to the input color.
    
    Parameters:
    input_grid (np.ndarray): A 2D numpy array representing the input grid.
    color (int): An integer representing the color to change to.
    columns (List[int]): A list of integers representing the columns to change.
    
    Returns:
    np.ndarray: A 2D numpy array with the specified columns changed to the input color.
    """
    for column in columns:
        input_grid[:, column] = color
    return input_grid

def change_rows_to_color(input_grid: np.ndarray, color: int, rows: List[int]) -> np.ndarray:
    """
    Given a 2D numpy array, a color, and a list of rows, changes all the cells in the specified rows to the input color.
    
    Parameters:
    input_grid (np.ndarray): A 2D numpy array representing the input grid.
    color (int): An integer representing the color to change to.
    rows (List[int]): A list of integers representing the rows to change.
    
    Returns:
    np.ndarray: A 2D numpy array with the specified rows changed to the input color.
    """
    for row in rows:
        input_grid[row, :] = color
    return input_grid

def find_columns_with_color_in_first_row(input_grid: np.ndarray, color: int) -> List[int]:
    """
    Given a 2D numpy array and a color, returns a list of columns where the color is present in the first row.
    
    Parameters:
    input_grid (np.ndarray): A 2D numpy array representing the input grid.
    color (int): An integer representing the color to search for.
    
    Returns:
    List[int]: A list of integers representing the columns where the color is present in the first row.
    """
    columns_with_color = []
    for i in range(input_grid.shape[1]):
        if input_grid[0][i] == color:
            columns_with_color.append(i)
    return columns_with_color

def find_rows_with_color_in_first_column(input_grid: np.ndarray, color: int) -> List[int]:
    """
    Given a 2D numpy array and a color, returns a list of rows where the color is present in the first column.
    
    Parameters:
    input_grid (np.ndarray): A 2D numpy array representing the input grid.
    color (int): An integer representing the color to search for.
    
    Returns:
    List[int]: A list of integers representing the rows where the color is present in the first column.
    """
    rows_with_color = []
    for i in range(input_grid.shape[0]):
        if input_grid[i][0] == color:
            rows_with_color.append(i)
    return rows_with_color

def find_least_color(input_grid: np.ndarray) -> int:
    """
    Given a 2D numpy array, returns the least occurring color in the array.
    
    Parameters:
    input_grid (np.ndarray): A 2D numpy array representing the input grid.
    
    Returns:
    int: An integer representing the least occurring color in the array.
    """
    (colors, counts) = np.unique(input_grid, return_counts=True)
    least_color = colors[np.argmin(counts)]
    return least_color

def main(input_grid: np.ndarray) -> np.ndarray:
    color = find_least_color(input_grid)
    list1 = find_rows_with_color_in_first_column(input_grid, color)
    list2 = find_columns_with_color_in_first_row(input_grid, color)
    row = input_grid.shape[0]
    column = input_grid.shape[1]
    output_grid = np.zeros((row, column), dtype=int)
    output_grid = change_rows_to_color(output_grid, color, list1)
    output_grid = change_columns_to_color(output_grid, color, list2)
    return output_grid