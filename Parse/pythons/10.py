import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def add_grey_lines(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.zeros((11, 11))
    for i in range(11):
        for j in range(11):
            if i % 4 == 3 or j % 4 == 3:
                output_grid[i][j] = grey
            else:
                output_grid[i][j] = input_grid[i - i // 4][j - j // 4]
    return output_grid

def set_block_colors(output_grid: np.ndarray, output_block: np.ndarray) -> np.ndarray:
    for (i, element) in enumerate(output_block.flatten()):
        if element != black:
            row = i // 3 * 3
            col = i % 3 * 3
            output_grid[row:row + 3, col:col + 3] = element
    return output_grid

def find_block_with_4_non_black_elements(sub_blocks: List[np.ndarray]) -> np.ndarray:
    for block in sub_blocks:
        if np.count_nonzero(block != black) == 4:
            return block
    return np.zeros((3, 3))

def separate_sub_blocks(input_grid: np.ndarray) -> List[np.ndarray]:
    sub_blocks = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_blocks.append(input_grid[i:i + 3, j:j + 3])
    return sub_blocks

def remove_rows_cols(input_grid: np.ndarray) -> np.ndarray:
    return np.delete(np.delete(input_grid, [3, 7], axis=1), [3, 7], axis=0)

def main(input_grid: np.ndarray) -> np.ndarray:
    output_grid = np.zeros((9, 9))
    remove_grey_input_grid = remove_rows_cols(input_grid)
    sub_blocks = separate_sub_blocks(remove_grey_input_grid)
    output_block = find_block_with_4_non_black_elements(sub_blocks)
    output_grid = set_block_colors(output_grid, output_block)
    output_grid = add_grey_lines(output_grid)
    return output_grid