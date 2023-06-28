import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def replace_non_black_color_with_gray(inp: np.ndarray) -> np.ndarray:
    out = inp.copy()
    non_black_mask = out[:, 5] != black
    out[non_black_mask, 5] = grey
    return out

def replace_last_five_columns_with_last_column(inp: np.ndarray) -> np.ndarray:
    out = inp.copy()
    out[:, -5:] = out[:, -1:]
    return out

def replace_first_six_columns_with_first_column(inp: np.ndarray) -> np.ndarray:
    out = inp.copy()
    out[:, :6] = out[:, :1]
    return out

def replace_middle_color_with_gray(inp: np.ndarray) -> np.ndarray:
    out = replace_non_black_color_with_gray(inp)
    return out

def copy_first_column_to_next_four_columns(inp: np.ndarray) -> np.ndarray:
    out = replace_last_five_columns_with_last_column(inp)
    return out

def copy_first_column(inp: np.ndarray) -> np.ndarray:
    out = replace_first_six_columns_with_first_column(inp)
    return out

def main(inp: np.ndarray) -> np.ndarray:
    out = copy_first_column(inp)
    out = copy_first_column_to_next_four_columns(out)
    out = replace_middle_color_with_gray(out)
    return out