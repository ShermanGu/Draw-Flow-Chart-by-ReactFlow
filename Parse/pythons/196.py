import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_row_with_pattern(row: np.ndarray, pattern: List[int]) -> np.ndarray:
    """
    Fills a row with a given color pattern
    Args:
        row: A numpy array representing the row to be filled
        pattern: A list of integers representing the color pattern to be used for filling the row
    Returns:
        A numpy array representing the filled row
    """
    filled_row = np.copy(row)
    color1 = None
    color2 = None
    current_color = None
    for i in range(len(pattern)):
        if pattern[i] == '0':
            if color1 == None:
                color1 = filled_row[i]
            filled_row[i] = color1
        elif pattern[i] == '1':
            if color2 == None:
                color2 = filled_row[i]
            filled_row[i] = color2
    return filled_row

def the_row_is_incomplete(row: np.ndarray) -> bool:
    """
    Checks if a row is incomplete, i.e., contains at least one black pixel
    Args:
        row: A numpy array representing the row to be checked
    Returns:
        A boolean value indicating whether the row is incomplete or not
    """
    return np.any(row == black)

def get_color_pattern(row: np.ndarray) -> List[int]:
    """                                                                                                                                                                   
    Finds the color pattern of a row that is filled in completely with colored pixels (not black)                                                                         
    Args:                                                                                                                                                                 
        row: A numpy array representing the row that is filled in completely with colored pixels (not black)                                                              
    Returns:                                                                                                                                                              
        A list of integers representing the color pattern of the row                                                                                                      
    """
    pattern = []
    color1 = None
    color2 = None
    current_color = None
    for pixel in row:
        if color1 == None:
            color1 = pixel
            pattern.append('0')
        elif color2 == None and pixel != color1:
            color2 = pixel
            pattern.append('1')
        elif pixel == color1:
            pattern.append('0')
        elif pixel == color2:
            pattern.append('1')
    return pattern

def find_complete_row(input_grid: np.ndarray) -> Tuple[np.ndarray, int]:
    """
    Finds the row that is completely filled with colored pixels (not black)
    Args:
        input_grid: A numpy array representing the input grid
    Returns:
        A tuple containing the numpy array representing the row that is completely filled with colored pixels (not black) and its row id
    """
    for i in range(input_grid.shape[0]):
        if np.all(input_grid[i] != black):
            return (input_grid[i], i)
    return (None, None)

def main(input_grid: np.ndarray) -> np.ndarray:
    """                                                                                                                                                                   
In the input, you should see... some lines filled in with colors                                                                                                          
The output grid size... is the same                                                                                                                                       
To make the output, For the line that is filled in completely with colored pixels (not black) keep these the same as input.                                               
there are two kinds of colors in this line: color1 and color2, you should get the color pattern of this line.                                                             
For any line with several color pixels filled in, use this pattern to finish the line across                                                                              
All other black squares remain black                                                                                                                                      
    """
    output_grid = np.copy(input_grid)
    (compelete_row, row_id) = find_complete_row(input_grid)
    pattern = get_color_pattern(compelete_row)
    for i in range(input_grid.shape[0]):
        if the_row_is_incomplete(input_grid[i]) and i != row_id:
            output_grid[i] = fill_row_with_pattern(input_grid[i], pattern)
    return output_grid