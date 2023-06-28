import numpy as np
from typing import *
(black, blue, red, green, yellow, grey, pink, orange, teal, maroon) = range(10)

def make_neighbors_black(input: np.ndarray, positions: List[Tuple[int, int]]) -> np.ndarray:
    """
    This function takes a 2-dimensional numpy array and a list of positions as input and makes the 3x3 neighborhood of each
    position in the input list black.

    Args:
    - input: a 2-dimensional numpy array representing the input image
    - positions: a list of tuples representing the positions to be evaluated

    Returns:
    - A numpy array with the 3x3 neighborhood of each position in the input list set to black.
    """
    for position in positions:
        input[position[0] - 1:position[0] + 2, position[1] - 1:position[1] + 2] = black
    return input

def make_neighbors_yellow(input: np.ndarray, positions: List[Tuple[int, int]]) -> np.ndarray:
    """
    This function takes a 2-dimensional numpy array and a list of positions as input and makes the 3x3 neighborhood of each
    position in the input list yellow.

    Args:
    - input: a 2-dimensional numpy array representing the input image
    - positions: a list of tuples representing the positions to be evaluated

    Returns:
    - A numpy array with the 3x3 neighborhood of each position in the input list set to yellow.
    """
    for position in positions:
        input[position[0] - 1:position[0] + 2, position[1] - 1:position[1] + 2] = yellow
    return input

def get_max_score_center(centers: List[Tuple[int, int]], scores: np.ndarray) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """
    This function takes a list of positions and a numpy array of scores as input and returns two lists of positions:
    - A list of positions with the maximum score
    - A list of positions with a score less than the maximum score

    Args:
    - centers: a list of tuples representing the positions to be evaluated
    - scores: a numpy array representing the number of yellow pixels in the 3x3 neighborhood of each position in the input list.

    Returns:
    - A tuple of two lists of tuples representing the positions with the maximum score and the positions with a score less than the maximum score.
    """
    max_score = np.max(scores)
    max_centers = [centers[i] for i in range(len(centers)) if scores[i] == max_score]
    other_centers = [centers[i] for i in range(len(centers)) if scores[i] < max_score]
    return (max_centers, other_centers)

def count_yellow_neighbors(input: np.ndarray, centers: List[Tuple[int, int]]) -> np.ndarray:
    """
    This function takes a 2-dimensional numpy array and a list of positions as input and counts the number of yellow pixels
    in the 3x3 neighborhood of each position in the input list.

    Args:
    - input: a 2-dimensional numpy array representing the input image
    - centers: a list of tuples representing the positions to be evaluated

    Returns:
    - A numpy array representing the number of yellow pixels in the 3x3 neighborhood of each position in the input list.
    """
    scores = np.zeros(len(centers))
    for (i, position) in enumerate(centers):
        scores[i] = np.sum(input[position[0] - 1:position[0] + 2, position[1] - 1:position[1] + 2] == yellow)
    return scores

def find_positions_without_grey_neighbors(input: np.ndarray) -> List[Tuple[int, int]]:
    """
    This function takes a 2-dimensional numpy array as input and returns a list of positions where there is no grey color
    in its 3x3 neighborhood.

    Args:
    - input: a 2-dimensional numpy array representing the input image

    Returns:
    - A list of tuples representing the positions where there is no grey color in its 3x3 neighborhood.
    """
    positions = []
    for i in range(1, input.shape[0] - 1):
        for j in range(1, input.shape[1] - 1):
            if np.all(input[i - 1:i + 2, j - 1:j + 2] != grey):
                positions.append((i, j))
    return positions

def main(input):
    centers = find_positions_without_grey_neighbors(input)
    scores = count_yellow_neighbors(input, centers)
    (center_yellow, center_black) = get_max_score_center(centers, scores)
    output = make_neighbors_yellow(input, center_yellow)
    output = make_neighbors_black(output, center_black)
    return output