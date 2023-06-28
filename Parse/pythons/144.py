import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_smallest_blocks_with_teal(output_grid: np.ndarray, smallest_blocks: List[Tuple[int, int, int, int]]) -> np.ndarray:
    """
    Replaces the smallest blocks in the output grid with teal color.
    
    Args:
    output_grid: A numpy array representing the output grid.
    smallest_blocks: A list of tuples representing the smallest blocks. Each tuple contains the coordinates of the top-left and bottom-right corners of the block.
    
    Returns:
    A numpy array representing the output grid with the smallest blocks replaced with teal color.
    """
    for block in smallest_blocks:
        output_grid[block[0]:block[2] + 1, block[1]:block[3] + 1] = teal
    return output_grid

def replace_largest_blocks_with_blue(input_grid: np.ndarray, largest_blocks: List[Tuple[int, int, int, int]]) -> np.ndarray:
    """
    Replaces the largest blocks in the input grid with blue color.
    
    Args:
    input_grid: A numpy array representing the input grid.
    largest_blocks: A list of tuples representing the largest blocks. Each tuple contains the coordinates of the top-left and bottom-right corners of the block.
    
    Returns:
    A numpy array representing the output grid with the largest blocks replaced with blue color.
    """
    output_grid = np.copy(input_grid)
    for block in largest_blocks:
        output_grid[block[0]:block[2] + 1, block[1]:block[3] + 1] = blue
    return output_grid

def find_largest_and_smallest_blocks(black_blocks: List[Tuple[int, int, int, int]]) -> Tuple[List[Tuple[int, int, int, int]], List[Tuple[int, int, int, int]]]:
    """
    Finds the largest and smallest blocks in the list of black blocks.
    
    Args:
    black_blocks: A list of tuples representing the blocks of black elements. Each tuple contains the coordinates of the top-left and bottom-right corners of the block.
    
    Returns:
    A tuple containing two lists of tuples. The first list contains the largest blocks and the second list contains the smallest blocks.
    """
    largest_blocks = []
    smallest_blocks = []
    max_area = 0
    min_area = float('inf')
    for block in black_blocks:
        area = (block[2] - block[0] + 1) * (block[3] - block[1] + 1)
        if area > max_area:
            max_area = area
            largest_blocks = [block]
        elif area == max_area:
            largest_blocks.append(block)
        if area < min_area:
            min_area = area
            smallest_blocks = [block]
        elif area == min_area:
            smallest_blocks.append(block)
    return (largest_blocks, smallest_blocks)

def find_black_blocks(input_grid: np.ndarray) -> List[Tuple[int, int, int, int]]:
    """
    Finds all the black blocks in the input grid separated by red lines.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A list of tuples representing the black blocks. Each tuple contains the coordinates of the top-left and bottom-right corners of the block.
    """
    black_blocks = []
    (rows, cols) = input_grid.shape
    for i in range(rows):
        for j in range(cols):
            if input_grid[i][j] == black:
                (top, left) = (i, j)
                (bottom, right) = (i, j)
                while bottom < rows - 1 and input_grid[bottom + 1][j] == black:
                    bottom += 1
                while right < cols - 1 and input_grid[i][right + 1] == black:
                    right += 1
                black_blocks.append((top, left, bottom, right))
                for k in range(top, bottom + 1):
                    for l in range(left, right + 1):
                        input_grid[k][l] = red
    return black_blocks

def identity(input_grid: np.ndarray) -> np.ndarray:
    """
    Returns a numpy array identical to the input grid.
    
    Args:
    input_grid: A numpy array representing the input grid.
    
    Returns:
    A numpy array identical to the input grid.
    """
    return np.copy(input_grid)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = identity(input_grid)
    black_blocks = find_black_blocks(input_grid)
    (largest_blocks, smallest_blocks) = find_largest_and_smallest_blocks(black_blocks)
    output_grid = replace_largest_blocks_with_blue(output_grid, largest_blocks)
    output_grid = replace_smallest_blocks_with_teal(output_grid, smallest_blocks)
    return output_grid