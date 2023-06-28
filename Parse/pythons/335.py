import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_above_black_with_teal(grid: np.ndarray, c: int) -> np.ndarray:
    """
    This function replaces all black pixels above the grey pixel in column c with teal.
    
    Args:
    grid: A numpy array representing the input grid
    c: An integer value indicating the index of the column with only one grey pixel
    
    Returns:
    A numpy array representing the modified grid
    """
    grey_pixels = np.where(grid == grey)
    row = grey_pixels[0][np.where(grey_pixels[1] == c)][0]
    grid[:row, c][grid[:row, c] == black] = teal
    return grid

def replace_below_black_with_teal(grid: np.ndarray, c: int) -> np.ndarray:
    """
    This function replaces all black pixels below the grey pixel in column c with teal.
    
    Args:
    grid: A numpy array representing the input grid
    c: An integer value indicating the index of the column with only one grey pixel
    
    Returns:
    A numpy array representing the modified grid
    """
    grey_pixels = np.where(grid == grey)
    row = grey_pixels[0][np.where(grey_pixels[1] == c)][0]
    grid[row + 1:, c][grid[row + 1:, c] == black] = teal
    return grid

def is_pixel_above_black(grid: np.ndarray, c: int, r: int) -> bool:
    """
    This function checks if the pixel above the gray pixel in column c and row r is black.
    
    Args:
    grid: A numpy array representing the input grid
    c: An integer value indicating the index of the column with only one grey pixel
    r: An integer value indicating the index of the row with only one grey pixel
    
    Returns:
    A boolean value indicating whether the pixel above the gray pixel in column c and row r is black
    """
    if r > 0 and grid[r - 1, c] == black:
        return True
    return False

def get_single_grey_column(grid: np.ndarray) -> Optional[int]:
    """
    This function returns the index of the column that contains only one grey pixel.
    
    Args:
    grid: A numpy array representing the input grid
    
    Returns:
    An integer value indicating the index of the column with only one grey pixel. If no such column exists, returns None.
    """
    for (i, col) in enumerate(grid.T):
        if np.count_nonzero(col == grey) == 1:
            return i
    return None

def replace_right_black_with_teal(grid: np.ndarray, r: int) -> np.ndarray:
    """
    This function replaces all black pixels to the right of the grey pixel in row r with teal.
    
    Args:
    grid: A numpy array representing the input grid
    r: An integer value indicating the index of the row with only one grey pixel
    
    Returns:
    A numpy array representing the modified grid
    """
    grey_pixels = np.where(grid == grey)
    col = grey_pixels[1][np.where(grey_pixels[0] == r)][0]
    grid[r, col + 1:][grid[r, col + 1:] == black] = teal
    return grid

def replace_left_black_with_teal(grid: np.ndarray, r: int) -> np.ndarray:
    """
    This function replaces all black pixels to the left of the grey pixel in row r with teal.
    
    Args:
    grid: A numpy array representing the input grid
    r: An integer value indicating the index of the row with only one grey pixel
    
    Returns:
    A numpy array representing the modified grid
    """
    grey_pixels = np.where(grid == grey)
    col = grey_pixels[1][np.where(grey_pixels[0] == r)][0]
    grid[r, :col][grid[r, :col] == black] = teal
    return grid

def is_pixel_to_right_black(grid: np.ndarray, r: int) -> bool:
    """
    This function checks if the pixel to the right of the gray pixel in row r is black.
    
    Args:
    grid: A numpy array representing the input grid
    r: An integer value indicating the index of the row with only one grey pixel
    
    Returns:
    A boolean value indicating whether the pixel to the right of the gray pixel in row r is black
    """
    grey_pixels = np.where(grid == grey)
    col = grey_pixels[1][np.where(grey_pixels[0] == r)][0]
    if col < grid.shape[1] - 1 and grid[r, col + 1] == black:
        return True
    return False

def get_single_grey_row(grid: np.ndarray) -> Optional[int]:
    """
    This function returns the index of the row that contains only one grey pixel.
    
    Args:
    grid: A numpy array representing the input grid
    
    Returns:
    An integer value indicating the index of the row with only one grey pixel. If no such row exists, returns None.
    """
    for (i, row) in enumerate(grid):
        if np.count_nonzero(row == grey) == 1:
            return i
    return None

def is_single_grey_row(grid: np.ndarray) -> bool:
    """
    This function checks if there is a row in the input grid that contains only one grey pixel.
    
    Args:
    grid: A numpy array representing the input grid
    
    Returns:
    A boolean value indicating whether there is a row with only one grey pixel
    """
    for row in grid:
        if np.count_nonzero(row == grey) == 1:
            return True
    return False

def find_smallest_matrix(input_grid: np.ndarray) -> np.ndarray:
    """
    This function finds the smallest matrix with all grey pixels in the input grid, 
    replaces all black pixels inside it (excluding boundaries) with teal, and returns the modified matrix.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A numpy array representing the modified grid
    """
    out = np.copy(input_grid)
    grey_pixels = np.where(out == grey)
    (min_row, max_row) = (np.min(grey_pixels[0]), np.max(grey_pixels[0]))
    (min_col, max_col) = (np.min(grey_pixels[1]), np.max(grey_pixels[1]))
    out[min_row + 1:max_row, min_col + 1:max_col][out[min_row + 1:max_row, min_col + 1:max_col] == black] = teal
    return out

def main(input_grid: np.ndarray) -> np.ndarray:
    out = find_smallest_matrix(input_grid)
    flag = is_single_grey_row(out)
    if flag:
        r = get_single_grey_row(out)
        flag2 = is_pixel_to_right_black(out, r)
        if flag2:
            out = replace_left_black_with_teal(out, r)
        else:
            out = replace_right_black_with_teal(out, r)
    else:
        c = get_single_grey_column(out)
        flag2 = is_pixel_above_black(out, c)
        if flag2:
            out = replace_below_black_with_teal(out, c)
        else:
            out = replace_above_black_with_teal(out, c)
    return out