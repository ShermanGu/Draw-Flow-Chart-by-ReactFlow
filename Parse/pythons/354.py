import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def get_most_common_color(color_list: List[List[int]]) -> int:
    color_counts = [0] * 10
    for neighborhood in color_list:
        for color in neighborhood:
            color_counts[color] += 1
    return color_counts.index(max(color_counts))

def collect_neighborhoods(input: List[Tuple[int, int]], positions: List[Tuple[int, int]]) -> List[List[int]]:
    neighborhoods = []
    for (x, y) in positions:
        neighborhood = []
        if x > 0:
            neighborhood.append(input[x - 1][y])
        if x < len(input) - 1:
            neighborhood.append(input[x + 1][y])
        if y > 0:
            neighborhood.append(input[x][y - 1])
        if y < len(input[0]) - 1:
            neighborhood.append(input[x][y + 1])
        neighborhoods.append(neighborhood)
    return neighborhoods

def get_positions_of_color(input: List[List[int]], color: int) -> List[Tuple[int, int]]:
    positions = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == color:
                positions.append((i, j))
    return positions

def get_color_with_fewest_locations(input: List[Tuple[int, int]]) -> int:
    color_counts = [0] * 10
    for i in input.reshape(-1):
        color_counts[i] += 1
    for i in range(len(color_counts)):
        if color_counts[i] == 0:
            color_counts[i] = 100000
    return color_counts.index(min(color_counts))

def main(input):
    color = get_color_with_fewest_locations(input)
    positions = get_positions_of_color(input, color)
    color_list = collect_neighborhoods(input, positions)
    output = get_most_common_color(color_list)
    return np.array([[output]], dtype=np.int32)