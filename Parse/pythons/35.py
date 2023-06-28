import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_block(input_grid: np.ndarray, positions: List[Tuple[int, int]]) -> np.ndarray:
    min_pos = np.min(positions, axis=0)
    max_pos = np.max(positions, axis=0)
    block = input_grid[min_pos[0]:max_pos[0] + 1, min_pos[1]:max_pos[1] + 1]
    return block

def collect_positions(input_grid: np.ndarray, element: int) -> List[Tuple[int, int]]:
    positions = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == element:
                positions.append((i, j))
    return positions

def find_min_element(input_grid: np.ndarray) -> int:
    """
    This function finds the element with the minimum amount in the input grid.

    Args:
    input_grid: A numpy array representing the input grid.

    Returns:
    The element with the minimum amount in the input grid.
    """
    (unique_elements, counts) = np.unique(input_grid, return_counts=True)
    min_element = unique_elements[np.argmin(counts)]
    return min_element

def main(input_grid: np.ndarray) -> np.ndarray:
    element = find_min_element(input_grid)
    positions = collect_positions(input_grid, element)
    block = find_block(input_grid, positions)
    return block