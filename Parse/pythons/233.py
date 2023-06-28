import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def move_rectangle(rectangle_positions: Tuple[Tuple[int, int], Tuple[int, int]], direction: str, steps: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Given the top-left and bottom-right coordinates of a rectangle, the direction of movement, and the number of steps,
    move the rectangle accordingly and return its new coordinates.
    
    Args:
    rectangle_positions: A tuple containing the top-left and bottom-right coordinates of the rectangle
    direction: A string representing the direction of movement ('up', 'down', 'left', or 'right')
    steps: An integer representing the number of steps to move the rectangle
    
    Returns:
    A tuple containing the top-left and bottom-right coordinates of the rectangle after movement
    """
    (top_left, bottom_right) = rectangle_positions
    if direction == 'up':
        top_left = (top_left[0] - steps, top_left[1])
        bottom_right = (bottom_right[0] - steps, bottom_right[1])
    elif direction == 'down':
        top_left = (top_left[0] + steps, top_left[1])
        bottom_right = (bottom_right[0] + steps, bottom_right[1])
    elif direction == 'left':
        top_left = (top_left[0], top_left[1] - steps)
        bottom_right = (bottom_right[0], bottom_right[1] - steps)
    else:
        top_left = (top_left[0], top_left[1] + steps)
        bottom_right = (bottom_right[0], bottom_right[1] + steps)
    return (top_left, bottom_right)

def get_direction_and_steps(rectangle_positions: Tuple[Tuple[int, int], Tuple[int, int]], flag_position: Tuple[int, int]) -> Tuple[str, int]:
    """
    Given the top-left and bottom-right coordinates of a rectangle and the position of a flag, 
    determine the direction and number of steps needed to move the rectangle to cover the flag.
    
    Args:
    rectangle_positions: A tuple containing the top-left and bottom-right coordinates of the rectangle
    flag_position: A tuple containing the row and column index of the flag
    
    Returns:
    A tuple containing the direction ('up', 'down', 'left', or 'right') and number of steps needed to move the rectangle
    """
    (top_left, bottom_right) = rectangle_positions
    (flag_row, flag_col) = flag_position
    if flag_row < top_left[0]:
        direction = 'up'
        steps = top_left[0] - flag_row
    elif flag_row > bottom_right[0]:
        direction = 'down'
        steps = flag_row - bottom_right[0]
    elif flag_col < top_left[1]:
        direction = 'left'
        steps = top_left[1] - flag_col
    else:
        direction = 'right'
        steps = flag_col - bottom_right[1]
    return (direction, steps)

def get_rectangle_coordinates(input_grid: List[List[int]], color: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """
    Traverse the input, return the top-left and bottom-right coordinates of the rectangle corresponding to the color
    
    Args:
    input_grid: A list of lists representing the grid of colors
    color: An integer representing the color of the rectangle
    
    Returns:
    A tuple containing the top-left and bottom-right coordinates of the rectangle
    """
    (rows, cols) = (len(input_grid), len(input_grid[0]))
    top_left = None
    bottom_right = None
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == color:
                if top_left is None:
                    top_left = (i, j)
                else:
                    top_left = (min(top_left[0], i), min(top_left[1], j))
                if bottom_right is None:
                    bottom_right = (i, j)
                else:
                    bottom_right = (max(bottom_right[0], i), max(bottom_right[1], j))
    return (top_left, bottom_right)

def move_rectangle_to_cover_flag(input, color, flag):
    positions = get_rectangle_coordinates(input, color)
    (direction, steps) = get_direction_and_steps(positions, flag)
    output_positions = move_rectangle(positions, direction, steps)
    output = np.copy(input)
    output[positions[0][0]:positions[1][0] + 1, positions[0][1]:positions[1][1] + 1] = black
    output[output_positions[0][0]:output_positions[1][0] + 1, output_positions[0][1]:output_positions[1][1] + 1] = color
    return output

def black_positions_with_two_black_neighbors(input_grid: List[List[int]]) -> List[List[int]]:
    """
    Traverse the input, black the position, two opposite connected positions of which are black
    
    Args:
    input_grid: A list of lists representing the grid of colors
    
    Returns:
    A list of lists with the updated grid of colors
    """
    (rows, cols) = (len(input_grid), len(input_grid[0]))
    output = np.copy(input_grid)
    for i in range(rows):
        for j in range(cols):
            if i > 0 and i < rows - 1 and (j > 0) and (j < cols - 1):
                if input_grid[i][j] != black and input_grid[i - 1][j] == black and (input_grid[i + 1][j] == black):
                    output[i][j] = black
                elif input_grid[i][j] != black and input_grid[i][j - 1] == black and (input_grid[i][j + 1] == black):
                    output[i][j] = black
    return output

def find_position_with_three_different_colors(input_grid: List[List[int]]) -> Tuple[int, int]:
    """
    Traverse the input, return the position, the four connected positions of which have three different colors and this position is not black
    
    Args:
    input_grid: A list of lists representing the grid of colors
    
    Returns:
    A tuple containing the row and column index of the position
    """
    (rows, cols) = (len(input_grid), len(input_grid[0]))
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] != black:
                colors = set()
                if i > 0:
                    colors.add(input_grid[i - 1][j])
                if i < rows - 1:
                    colors.add(input_grid[i + 1][j])
                if j > 0:
                    colors.add(input_grid[i][j - 1])
                if j < cols - 1:
                    colors.add(input_grid[i][j + 1])
                if len(colors) == 3:
                    return (i, j)
    return None

def main(input_grid):
    flag = find_position_with_three_different_colors(input_grid)
    color = input_grid[flag]
    output = np.copy(input_grid)
    output = black_positions_with_two_black_neighbors(output)
    output = move_rectangle_to_cover_flag(output, color, flag)
    return output