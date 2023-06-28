import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def change_colors(input: List[List[int]], colors: Dict[int, int]) -> List[List[int]]:
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] in colors:
                input[i][j] = colors[input[i][j]]
    return input

def main(input):
    colors = {green: yellow, blue: grey, red: pink, teal: maroon, grey: blue, yellow: green, maroon: teal, pink: red}
    output = change_colors(input, colors)
    return output