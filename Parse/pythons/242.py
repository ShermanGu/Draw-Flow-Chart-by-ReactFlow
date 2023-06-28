import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_all_blue(input_grid: np.ndarray, positions: List[Tuple[int, int]]) -> np.ndarray:
    for position in positions:
        input_grid[position] = blue
    return input_grid

def get_adjacent_black_positions(input_grid: np.ndarray, position: Tuple[int, int]) -> List[Tuple[int, int]]:
    adjacent_positions = []
    (row, col) = position
    if row > 0 and input_grid[row - 1][col] == black:
        adjacent_positions.append((row - 1, col))
    if row < input_grid.shape[0] - 1 and input_grid[row + 1][col] == black:
        adjacent_positions.append((row + 1, col))
    if col > 0 and input_grid[row][col - 1] == black:
        adjacent_positions.append((row, col - 1))
    if col < input_grid.shape[1] - 1 and input_grid[row][col + 1] == black:
        adjacent_positions.append((row, col + 1))
    return adjacent_positions

def get_blue_positions(input_grid: np.ndarray) -> List[Tuple[int, int]]:
    positions = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == blue:
                positions.append((i, j))
    return positions

def main(input_grid):
    positions = get_blue_positions(input_grid)
    output = np.copy(input_grid)
    while len(positions) > 0:
        position = positions.pop()
        adjacent = get_adjacent_black_positions(output, position)
        positions += adjacent
        output = color_all_blue(output, adjacent)
    return output