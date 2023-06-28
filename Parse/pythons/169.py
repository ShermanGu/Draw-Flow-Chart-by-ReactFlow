import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_colors_to_black_in_large_grid(black_positions, input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    This function takes an input grid with a large pattern of the same color and a small grid pattern with many colors.                                                 
    The size of the large grid is several times larger than the small grid.                                                                                             
    The output grid size is the size of the smaller pattern with many colors.                                                                                           
    To make the output, the smaller grid is replicated and the colors are changed to black where they are black in the larger grid.                                     
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A numpy array representing the input grid                                                                                                               
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A numpy array representing the output grid with black pixels in the corresponding positions of the larger grid                                                      
    """
    for (i, j) in black_positions:
        input_grid[i, j] = black
    return input_grid

def find_position_of_small_grid_all_black_pixels(input_grid: np.ndarray, rows_of_small_grid: List[int], cols_of_small_grid: List[int], rows_of_large_grid: List[int], cols_of_large_grid: List[int], times: int):
    """                                                                                                                                                                 
    This function takes an input grid, row and column indices of small and large grids, and the number of times the small grid is replicated in the large grid.         
    It returns the corresponding position of the small grid where all pixels are black in the large grid.                                                               
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A numpy array representing the input grid                                                                                                               
    rows_of_small_grid: A list of row indices that contain more than two kinds of colors in the input grid                                                              
    cols_of_small_grid: A list of column indices that contain more than two kinds of colors in the input grid                                                           
    rows_of_large_grid: A list of row indices that contain more than two continuous same colors in the input grid                                                       
    cols_of_large_grid: A list of column indices that contain more than two continuous same colors in the input grid                                                    
    times: An integer representing the number of times the small grid is replicated in the large grid                                                                   
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A tuple representing the corresponding position of the small grid where all pixels are black in the large grid                                                      
    """
    small_grid = input_grid[rows_of_small_grid[0]:rows_of_small_grid[-1] + 1, cols_of_small_grid[0]:cols_of_small_grid[-1] + 1]
    large_grid = input_grid[rows_of_large_grid[0]:rows_of_large_grid[-1] + 1, cols_of_large_grid[0]:cols_of_large_grid[-1] + 1]
    black_indices = []
    for i in range(small_grid.shape[0]):
        for j in range(small_grid.shape[1]):
            if np.array_equal(large_grid[i * times:(i + 1) * times, j * times:(j + 1) * times], np.zeros((times, times))):
                black_indices.append((i, j))
    return black_indices

def find_cols_with_more_than_two_continuous_colors(input_grid: np.ndarray) -> List[int]:
    """                                                                                                                                                                 
    This function takes an input grid and returns a list of column indices that contain more than two continuous same colors.                                           
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A numpy array representing the input grid                                                                                                               
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A list of column indices that contain more than two continuous same colors                                                                                          
    """
    cols_with_more_than_two_continuous_colors = []
    for i in range(input_grid.shape[1]):
        col = input_grid[:, i]
        for j in range(len(col) - 2):
            if col[j] == col[j + 1] == col[j + 2] and col[j] != black:
                cols_with_more_than_two_continuous_colors.append(i)
                break
    return cols_with_more_than_two_continuous_colors

def find_rows_with_more_than_two_continuous_colors(input_grid: np.ndarray) -> List[int]:
    """                                                                                                                                                                 
    This function takes an input grid and returns a list of row indices that contain more than two continuous same colors.                                              
                                                                                                                                                                        
    Args:                                                                                                                                                               
    input_grid: A numpy array representing the input grid                                                                                                               
                                                                                                                                                                        
    Returns:                                                                                                                                                            
    A list of row indices that contain more than two continuous same colors                                                                                             
    """
    rows_with_more_than_two_continuous_colors = []
    for i in range(input_grid.shape[0]):
        row = input_grid[i]
        for j in range(len(row) - 2):
            if row[j] == row[j + 1] == row[j + 2] and row[j] != black:
                rows_with_more_than_two_continuous_colors.append(i)
                break
    return rows_with_more_than_two_continuous_colors

def find_cols_with_multiple_colors(input_grid: np.ndarray) -> List[int]:
    """
    This function takes an input grid and returns a list of column indices that contain more than two kinds of colors.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A list of column indices that contain more than two kinds of colors
    """
    cols_with_multiple_colors = []
    for i in range(input_grid.shape[1]):
        if len(set(input_grid[:, i])) > 2:
            cols_with_multiple_colors.append(i)
    return cols_with_multiple_colors

def find_rows_with_multiple_colors(input_grid: np.ndarray) -> List[int]:
    """
    This function takes an input grid and returns a list of row indices that contain more than two kinds of colors.
    
    Args:
    input_grid: A numpy array representing the input grid
    
    Returns:
    A list of row indices that contain more than two kinds of colors
    """
    rows_with_multiple_colors = []
    for i in range(input_grid.shape[0]):
        if len(set(input_grid[i])) > 2:
            rows_with_multiple_colors.append(i)
    return rows_with_multiple_colors

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                 
    In the input, you should see...A large grid with a large pattern of the same color, and a small grid pattern with many colors.                                      
    the size of the large grid is several times larger than the small grid                                                                                              
    The output grid size...The size of the grid is the size of the smaller pattern with many colors.                                                                    
    To make the output, you have to replicate the smaller grid. Change the colors to black where they are black in the larger rectangle                                 
    """
    rows_of_small_grid = find_rows_with_multiple_colors(input_grid)
    cols_of_small_grid = find_cols_with_multiple_colors(input_grid)
    output_grid = np.zeros((len(rows_of_small_grid), len(cols_of_small_grid)))
    output_grid[:, :] = input_grid[rows_of_small_grid[0]:rows_of_small_grid[-1] + 1, cols_of_small_grid[0]:cols_of_small_grid[-1] + 1]
    rows_of_large_grid = find_rows_with_more_than_two_continuous_colors(input_grid)
    cols_of_large_grid = find_cols_with_more_than_two_continuous_colors(input_grid)
    times = int(len(rows_of_large_grid) / len(rows_of_small_grid))
    black_position = find_position_of_small_grid_all_black_pixels(input_grid, rows_of_small_grid, cols_of_small_grid, rows_of_large_grid, cols_of_large_grid, times)
    output_grid = change_colors_to_black_in_large_grid(black_position, output_grid)
    return output_grid