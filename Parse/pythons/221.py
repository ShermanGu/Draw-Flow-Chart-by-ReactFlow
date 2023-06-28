import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def find_max_rectangle(rectangles: List[Tuple[int, int, int, int]]) -> Tuple[int, int, int, int]:
    max_area = 0
    max_rectangle = None
    for rectangle in rectangles:
        (i, j, width, height) = rectangle
        area = width * height
        if area > max_area:
            max_area = area
            max_rectangle = rectangle
    return max_rectangle

def find_rectangles(input: np.ndarray) -> List[Tuple[int, int, int, int]]:
    rectangles = []
    (rows, cols) = input.shape
    visited = np.zeros(input.shape, dtype=bool)
    for i in range(rows):
        for j in range(cols):
            if input[i, j] != black and (not visited[i, j]):
                color = input[i, j]
                width = 1
                height = 1
                visited[i, j] = True
                for k in range(j + 1, cols):
                    if input[i, k] == color and (not visited[i, k]):
                        width += 1
                        visited[i, k] = True
                    else:
                        break
                for k in range(i + 1, rows):
                    if all(input[k, j:j + width] == color) and (not any(visited[k, j:j + width])):
                        height += 1
                        visited[k, j:j + width] = True
                    else:
                        break
                rectangles.append((i, j, width, height))
    return rectangles

def main(input):
    rectangles = find_rectangles(input)
    max_rectangle = find_max_rectangle(rectangles)
    output = np.zeros(input.shape, dtype=np.int32)
    (i, j, width, height) = max_rectangle
    output[i:i + height, j:j + width] = input[i:i + height, j:j + width]
    return output