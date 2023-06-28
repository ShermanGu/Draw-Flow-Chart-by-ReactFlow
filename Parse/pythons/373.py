import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def color_select_line(grid: np.ndarray, line_coords: Tuple[int, int], color: int) -> np.ndarray:
    """
    Colors the given line in the grid with the specified color.
    """
    (start_coord, end_coord) = line_coords
    if start_coord[0] == end_coord[0]:
        for j in range(start_coord[1], end_coord[1] + 1):
            grid[start_coord[0]][j] = color
    else:
        for i in range(start_coord[0], end_coord[0] + 1):
            grid[i][start_coord[1]] = color
    return grid

def find_mid_length_grey_line(input_grid: np.ndarray) -> Tuple[int, int]:
    longest_length = 1 + max(find_longest_grey_line(input_grid)[1][0] - find_longest_grey_line(input_grid)[0][0], find_longest_grey_line(input_grid)[1][1] - find_longest_grey_line(input_grid)[0][1])
    shortest_length = 1 + max(find_shortest_grey_line(input_grid)[1][0] - find_shortest_grey_line(input_grid)[0][0], find_shortest_grey_line(input_grid)[1][1] - find_shortest_grey_line(input_grid)[0][1])
    start_coord = (0, 0)
    end_coord = (0, 0)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if i > start_coord[0] and i < end_coord[0]:
                continue
            if j > start_coord[1] and j < end_coord[1]:
                continue
            if input_grid[i - 1][j] == grey and i > 0 or (input_grid[i][j - 1] == grey and j > 0):
                continue
            if input_grid[i][j] == grey:
                length = 1
                for k in range(j + 1, input_grid.shape[1]):
                    if input_grid[i][k] == grey:
                        length += 1
                    else:
                        break
                if length > shortest_length and length < longest_length:
                    start_coord = (i, j)
                    end_coord = (i, j + length - 1)
                length = 1
                for k in range(i + 1, input_grid.shape[0]):
                    if input_grid[k][j] == grey:
                        length += 1
                    else:
                        break
                if length > shortest_length and length < longest_length:
                    start_coord = (i, j)
                    end_coord = (i + length - 1, j)
    return (start_coord, end_coord)

def find_shortest_grey_line(input_grid: np.ndarray) -> Tuple[int, int]:
    min_length = float('inf')
    start_coord = (0, 0)
    end_coord = (0, 0)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if i > start_coord[0] and i < end_coord[0]:
                continue
            if j > start_coord[1] and j < end_coord[1]:
                continue
            if input_grid[i - 1][j] == grey and i > 0 or (input_grid[i][j - 1] == grey and j > 0):
                continue
            if input_grid[i][j] == grey:
                length = 1
                for k in range(j + 1, input_grid.shape[1]):
                    if input_grid[i][k] == grey:
                        length += 1
                    else:
                        break
                if length < min_length and length > 1:
                    min_length = length
                    start_coord = (i, j)
                    end_coord = (i, j + length - 1)
                length = 1
                for k in range(i + 1, input_grid.shape[0]):
                    if input_grid[k][j] == grey:
                        length += 1
                    else:
                        break
                if length < min_length and length > 1:
                    min_length = length
                    start_coord = (i, j)
                    end_coord = (i + length - 1, j)
    return (start_coord, end_coord)

def find_longest_grey_line(input_grid: np.ndarray) -> Tuple[int, int]:
    """
    Finds the longest grey line in the input grid and returns its starting and ending coordinates.
    """
    max_length = 0
    start_coord = (0, 0)
    end_coord = (0, 0)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i][j] == grey:
                length = 1
                for k in range(j + 1, input_grid.shape[1]):
                    if input_grid[i][k] == grey:
                        length += 1
                    else:
                        break
                if length > max_length:
                    max_length = length
                    start_coord = (i, j)
                    end_coord = (i, j + length - 1)
                length = 1
                for k in range(i + 1, input_grid.shape[0]):
                    if input_grid[k][j] == grey:
                        length += 1
                    else:
                        break
                if length > max_length:
                    max_length = length
                    start_coord = (i, j)
                    end_coord = (i + length - 1, j)
    return (start_coord, end_coord)

def main(input_grid: np.ndarray) -> np.ndarray:
    """
    color the lines based on their length: longest is blue, medium is yellow, and smallest is red.
    """
    output_grid = input_grid.copy()
    longest_line = find_longest_grey_line(input_grid)
    shortest_line = find_shortest_grey_line(input_grid)
    mid_line = find_mid_length_grey_line(input_grid)
    output_grid = color_select_line(output_grid, longest_line, blue)
    output_grid = color_select_line(output_grid, shortest_line, red)
    output_grid = color_select_line(output_grid, mid_line, yellow)
    return output_grid