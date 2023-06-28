import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def fill_subgrid_colors(sub_grids: List[np.ndarray], output_grid: np.ndarray) -> np.ndarray:
    for (i, sub_grid) in enumerate(sub_grids):
        (unique, counts) = np.unique(sub_grid, return_counts=True)
        color_counts = dict(zip(unique, counts))
        if black in color_counts:
            del color_counts[black]
        if color_counts:
            max_color = max(color_counts, key=color_counts.get)
            output_grid[i // output_grid.shape[1], i % output_grid.shape[1]] = max_color
    return output_grid

def create_output_grid(rows: List[int], columns: List[int]) -> np.ndarray:
    return np.zeros((len(rows) - 1, len(columns) - 1), dtype=int)

def divide_subgrids(rows: List[int], columns: List[int], input_grid: np.ndarray) -> List[np.ndarray]:
    sub_grids = []
    for i in range(len(rows) - 1):
        for j in range(len(columns) - 1):
            sub_grid = input_grid[rows[i]:rows[i + 1], columns[j]:columns[j + 1]]
            sub_grids.append(sub_grid)
    return sub_grids

def add_border(rows: List[int], columns: List[int], input_grid: np.ndarray) -> Tuple[List[int], List[int]]:
    (max_row, max_col) = input_grid.shape
    rows = [0] + [r + 1 for r in rows] + [max_row]
    columns = [0] + [c + 1 for c in columns] + [max_col]
    return (rows, columns)

def find_all_black_rows_and_columns(input_grid: np.ndarray) -> Tuple[List[int], List[int]]:
    (rows, columns) = (np.where(np.all(input_grid == black, axis=1)), np.where(np.all(input_grid == black, axis=0)))
    return (rows[0].tolist(), columns[0].tolist())

def main(input_grid: np.ndarray) -> np.ndarray:
    (rows, colomns) = find_all_black_rows_and_columns(input_grid)
    (rows, colomns) = add_border(rows, colomns, input_grid)
    sub_grids = divide_subgrids(rows, colomns, input_grid)
    output_grid = create_output_grid(rows, colomns)
    output_grid = fill_subgrid_colors(sub_grids, output_grid)
    return output_grid