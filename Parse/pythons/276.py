import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def dfs(input, i, j, visited, domain):
    if i < 0 or i >= len(input) or j < 0 or (j >= len(input[0])) or ((i, j) in visited) or (input[i][j] != teal):
        return
    visited.add((i, j))
    domain.append((i, j))
    dfs(input, i + 1, j, visited, domain)
    dfs(input, i - 1, j, visited, domain)
    dfs(input, i, j + 1, visited, domain)
    dfs(input, i, j - 1, visited, domain)
    dfs(input, i + 1, j + 1, visited, domain)
    dfs(input, i - 1, j - 1, visited, domain)
    dfs(input, i + 1, j - 1, visited, domain)
    dfs(input, i - 1, j + 1, visited, domain)

def color_positions(input: List[List[int]], positions: List[Tuple[int, int]], color: int) -> List[List[int]]:
    """
    This function takes a 2D list of integers as input, a list of positions to be colored and a color integer.
    It returns the input list with the specified positions colored with the specified color.
    """
    for pos in positions:
        input[pos[0]][pos[1]] = color
    return input

def find_teal_domains(input: List[List[int]]) -> List[List[Tuple[int, int]]]:
    """
    This function takes a 2D list of integers as input and returns a list of three teal eight-connected domains in the input.
    """
    domains = []
    visited = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == teal and (i, j) not in visited:
                domain = []
                dfs(input, i, j, visited, domain)
                domains.append(domain)
    return domains

def main(input):
    connected_domains = find_teal_domains(input)
    connected_domains = sorted(connected_domains, key=lambda x: len(x))
    for domain in connected_domains:
        input = color_positions(input, domain, blue)
    input = color_positions(input, connected_domains[0], red)
    return input